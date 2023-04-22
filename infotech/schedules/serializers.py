from rest_framework import serializers
from .models import Schedule
from professors.models import Professor
from subjects.models import Subject
from daytimes.models import DayTime
from students.models import Student


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    date_created = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M%p", read_only=True)

    students_assigned = serializers.SlugRelatedField(
        queryset=Student.objects.all(), many=True, slug_field='full_name', allow_null=True)

    professor = serializers.SlugRelatedField(
        queryset=Professor.objects.all(), slug_field='full_name', allow_null=True)

    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(), slug_field='code', allow_null=True)

    daytimes = serializers.SlugRelatedField(
        queryset=DayTime.objects.all(), slug_field='name', allow_null=True)

    class Meta:
        model = Schedule
        fields = ('id', 'name', 'max_slots', 'subject', 'year_level', 'semester', 'daytimes', 'students_assigned',
                  'professor', 'date_created')
        read_only_fields = ('id', 'date_created', 'name',
                            'year_level', 'semester')

    def validate(self, attrs):
        students = attrs.get('students')
        max_slots = attrs.get('max_slots')
        if students and students.count() > max_slots:
            raise serializers.ValidationError(
                'Too many students for this subject')
        return attrs
