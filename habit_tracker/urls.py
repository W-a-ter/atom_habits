from django.urls import path
from rest_framework.routers import DefaultRouter

from habit_tracker.views import HabitViewSet

app_name = 'habit_tracker'

router = DefaultRouter()
router.register(prefix=r'habit', viewset=HabitViewSet, basename='habit')

urlpatterns = [
    
] + router.urls


