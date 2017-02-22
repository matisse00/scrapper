from rest_framework import serializers
from models import Main


class MainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'text', 'author')

