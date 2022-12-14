from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.familiarserializer import FamiliarSerializer

class CrearFamiliarView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
