from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .calSerializers import BasicCalSerializer, FullCalSerializer, CalPermissionSerializer
from rest_framework.decorators import action
from .models import Cal, CalPermissionTable
from django.shortcuts import get_object_or_404


# Permission Classes
class IsAuthorizedToRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ### queryset filter permission?
        ### Use the Permission Table!
        return obj.owner == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# Calendar View
class CalendarView(viewsets.ModelViewSet):
    queryset = Cal.objects.all()
    lookup_field = 'uuid'

    def get_permissions(self):
        if self.action in ('list', 'retrive', 'update'):
            if self.action == 'list':
                raise NotImplementedError()
            permission_classes = [IsAuthorizedToRead&IsOwnerOrReadOnly] ### [~|IsAdminUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullCalSerializer
        return BasicCalSerializer

    @action(methods=['post'], detail=True, permission_classes=['IsOwner'], url_path='allow-user')
    def allow_user(self, request, uuid=None):
        serializer = CalPermissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, permission_classes=['IsOwner'], url_path='ban-user')
    def ban_user(self, request, uuid=None):
        queryset = CalPermissionTable.objects.all()
        row = get_object_or_404(queryset, request.data.user_uuid)
        row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)