from dataclasses import fields
from pyexpat import model
from authApp.models.usuario import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('username','password','perfil','nombre','apellidos','telefono','generos')