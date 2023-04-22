from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('subjects.urls')),
    path('', include('students.urls')),
    path('', include('professors.urls')),
    path('', include('schedules.urls')),
    path('', include('daytimes.urls')),
    path('accounts/', include('accounts.urls')),
]
