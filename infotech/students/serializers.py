from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student
from schedules.models import Schedule
from subjects.models import Subject


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    schedules = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), many=True, slug_field='name', allow_null=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'first_name', 'middle_name', 'last_name',
                  'age', 'sex', 'birthdate',
                  'address', 'birthplace',
                  'mother_name', 'father_name',
                  'registrar_done', 'clearance_done', 'pta_done',
                  'schedules', 'year_level', 'current_semester'
                  ]
        read_only_fields = ['id', 'full_name']
