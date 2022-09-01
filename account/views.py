from .serializers import FullUserSerializer, BasicUserSerializer
from .models import User
from rest_framework import viewsets

class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullUserSerializer
        return BasicUserSerializer

    # def get_permissions(self):
    #     pass
   