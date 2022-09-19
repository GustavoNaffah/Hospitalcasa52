from dataclasses import fields
from pyexpat import model
from authApp.models.sigvitales import Signos_vitales
from rest_framework import serializers

class SignosVitalesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Signos_vitales
        fields=('id_paciente','oximetria','frecuenciaRespiratoria','frecuenciaCardiaca','temperatura','glicemias','presionArterial','fechaHora')