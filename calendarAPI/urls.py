from django.urls import path, include
from .views import calViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r'calendars', calViewSet, basename='calendars')

urlpatterns = [
    path('', include(router.urls)),
]