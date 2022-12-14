from django.urls import path, include
from .views import CalendarView
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r'calendars', CalendarView, basename='calendars')

urlpatterns = [
    path('', include(router.urls)),
]