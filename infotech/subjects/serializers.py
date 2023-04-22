from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subject
from students.models import Student


class SubjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'code', 'year_level', 'semester')
        read_only_fields = ['id']
