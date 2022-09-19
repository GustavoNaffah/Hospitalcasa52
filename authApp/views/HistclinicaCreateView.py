from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.histclinicaserializer import HistoriaClinicaSerializer


class CrearHistclinicaView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = HistoriaClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
