from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'schedules', views.ScheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('first_year_schedules/', views.FirstYearScheduleViewSet.as_view()),
    path('second_year_schedules/', views.SecondYearScheduleViewSet.as_view()),
    path('third_year_schedules/', views.ThirdYearScheduleViewSet.as_view()),
    path('fourth_year_schedules/', views.FourthYearScheduleViewSet.as_view()),
]
