from rest_framework import viewsets, generics
from .models import DayTime
from .serializers import DayTimeSerializer

# Create your views here.


class DayTimeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = DayTimeSerializer
    queryset = DayTime.objects.all()
