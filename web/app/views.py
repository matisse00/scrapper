from django.shortcuts import render
from rest_framework import viewsets
from serializers import MainSerializer
from models import Main


class MainViewset(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

# Create your views here.
