from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DayTime


class DayTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DayTime
        fields = ('id', 'name', 'day', 'time_start', 'time_end')
        read_only_fields = ['id', 'name']
