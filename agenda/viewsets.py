from rest_framework import viewsets
from agenda import serializers, models


class AgendaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AgendaSerializer
    queryset = models.Agenda.objects.all()
