from dataclasses import fields
from pyexpat import model
from authApp.models.psalud import Personal_salud
from rest_framework import serializers

class PersonalSaludSerializers(serializers.ModelSerializer):
    class Meta:
        model=Personal_salud
        fields=('username','rol','especialidad')