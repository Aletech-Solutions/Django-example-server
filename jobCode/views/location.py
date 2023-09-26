from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from jobCode.model.location import LocationModel
from jobCode.serializers import LocationSerializer

class LocationView(APIView):
    def post(self, request):
        location = request.data.get('location')

        if location is not None:
            location_instance = LocationModel(location=location)
            location_instance.save()

            return Response({'message': 'Location received successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Missing or invalid data in the request payload'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        location_id = request.query_params.get('location_id')
        
        if location_id is None:
            locations = LocationModel.objects.all()
            serializer = LocationSerializer(locations, many=True)
            return Response(serializer.data)
        
        try:
            location = LocationModel.objects.get(id=location_id)
        except LocationModel.DoesNotExist:
            raise Http404

        serializer = LocationSerializer(location)
        return Response(serializer.data)