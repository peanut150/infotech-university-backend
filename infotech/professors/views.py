from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ProfessorSerializer
from .models import Professor


class ProfessorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all().order_by('date_joined')
