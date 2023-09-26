from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from jobCode.model.logger import LoggerModel  
from jobCode.serializers import LoggerSerializer 

class LoggerView(APIView):
    def get(self, request):
        logs = LoggerModel.objects.all()

        serializer = LoggerSerializer(logs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)