from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from jobCode.model.logger import LoggerModel
from django.urls import resolve

class LoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        endpoint = request.path_info
        payload = None
        if resolve(request.path_info).url_name == 'logs-list':
            return

        if request.method == "GET":
            payload = request.GET.urlencode()
        elif request.method == "POST":
            payload = request.body.decode("utf-8")

        method = request.method

        LoggerModel.objects.create(
            endpoint=endpoint,
            payload=payload,
            method=method,
            timestamp=datetime.now(),
        )