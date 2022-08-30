from django.urls import path, include
from .views import UserCreate
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserCreate, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]