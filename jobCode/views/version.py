from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jobCode.serializers import VersionSerializer

class VersionView(APIView):
    def get(self, request):
        version = "1.0" 

        serializer = VersionSerializer({'version': version})

        return Response(serializer.data, status=status.HTTP_200_OK)