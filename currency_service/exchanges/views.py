import zlib
from datetime import timedelta

import requests
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


BASE_API_URL = "https://api.nbrb.by/exrates/rates"


def colculate_crc32(data):
    return str(zlib.crc32(data.encode("utf-8")) & 0xFFFFFFFF)


@api_view(['GET'])
def load_exchange_rates(request):
    date = request.query_params.get("date")

    if not date:
        return Response(
            {"error": "The date parameter is missing"},
            status=status.HTTP_400_BAD_REQUEST
        )

    date = timezone.datetime.strptime(date, "%Y-%m-%d").date()

    params = {
        "ondate": date,
        "periodicity": 0
    }

    response = requests.get(BASE_API_URL, params=params)

    if response.status_code != 200:
        return Response(
            {"error": "Data receipt error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    rates = response.json()

    for rate in rates:
        ExchangeRate.objects.update_or_create(
            date=date,
            currency_id=rate["Cur_ID"],
            currency_name=rate["Cur_Abbreviation"],
            defaults={
                "scale": rate["Cur_Scale"],
                "rate": rate["Cur_OfficialRate"]
            }
        )

    response_data = "Data successfully downloaded"
    response = Response(
        {
            "message": response_data,
            "title": colculate_crc32(response_data)
        }
    )

    return response


@api_view(['GET'])
def get_exchange_rate(request):
    date = request.query_params.get("date")
    currency = request.query_params.get("currency")

    if not date or not currency:
        return Response(
            {"error": "The 'date' or 'currency' parameter is missing"},
            status=status.HTTP_400_BAD_REQUEST
        )

    exchange_rate = get_object_or_404(
        ExchangeRate,
        date=date,
        currency_name=currency
    )

    serializer = ExchangeRateSerializer(exchange_rate)
    response_data = serializer.data

    prev_date = timezone.datetime.strptime(
        date, "%Y-%m-%d") - timedelta(days=1)

    try:
        previous_rate = ExchangeRate.objects.get(
            date=prev_date,
            currency_name=currency
        )
        rate_difference = exchange_rate.rate - previous_rate.rate
        response_data["change_course"] = "Declined" if rate_difference < 0 else "Increased"
        response_data["rate_difference"] = rate_difference

    except ExchangeRate.DoesNotExist:
        response_data["change_course"] = None
        response_data["rate_difference"] = None

    response_data['title'] = colculate_crc32(str(response_data))

    return Response(response_data)
