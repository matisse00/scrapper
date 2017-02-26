import re
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import MainSerializer
from models import Main
from collections import Counter


class MainView(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class StatView(APIView):
    def get(self, request, format=None):
        string = ""
        for e in Main.objects.all():
            string += e.text
        words = re.findall(r'\w+', string.lower())
        return Response(Counter(words).most_common(10))


class StatViewAuthor(APIView):
    def get(self, request, *args, **kwargs):
        string = ""
        print kwargs.get('pk', None)
        name = '{"' + kwargs.get('pk', None) + '"}'
        print name
        for e in Main.objects.filter(author=name):
            string += e.text
        words = re.findall(r'\w+', string.lower())
        return Response(Counter(words).most_common(10))
