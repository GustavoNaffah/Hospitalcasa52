from dataclasses import fields
from pyexpat import model
from authApp.models.histclinica import Historia_clinica
from rest_framework import serializers

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historia_clinica
        fields=('id_paciente','sugerencias','diagnostico','entorno','fecha_sugerencia''descripcion')