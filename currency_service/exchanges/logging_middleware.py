import logging
import time


logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(
            f"Incoming request: {request.method} {request.get_full_path()}")

        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time

        logger.info(
            f"Response: {response.status_code} {response.reason_phrase} - Duration: {duration:.2f}s"
        )

        return response
