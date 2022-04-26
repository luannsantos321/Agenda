from rest_framework import serializers
from agenda import models




class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agenda
        fields = '__all__'