from sys import implementation
from rest_framework import viewsets, permissions
from .calSerializers import BasicCalSerializer, FullCalSerializer
from .models import Cal

class IsAuthorizedToRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner_class == Cal.ROOM:
            ### need to implement
            return True
        return obj.owner == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CalendarView(viewsets.ModelViewSet):
    queryset = Cal.objects.all()
    
    def get_permissions(self):
        if self.action in ('list', 'retrive', 'update'):
            if self.action == 'list':
                raise NotImplementedError()
            permission_classes = ['IsAuthorizedToRead&IsOwnerOrReadOnly'] ### ['~|IsAdmin']
        else:
            permission_classes = ['IsAdmin']
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return FullCalSerializer
        return BasicCalSerializer