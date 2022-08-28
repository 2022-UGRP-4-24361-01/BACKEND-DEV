# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.response import Response
# from django.http import Http404
from rest_framework import status
from .calSerializers import CalSerializer
from .models import Cal
from rest_framework import viewsets
from django.shortcuts import get_object_or_404 #, get_list_or_404

class calViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Cal.objects.all()
        serializer = CalSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None):
        queryset = Cal.objects.all()
        cal = get_object_or_404(queryset, pk=pk)
        serializer = CalSerializer(cal)
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = Cal.objects.all()
        cal = get_object_or_404(queryset, pk=pk)
        serializer = CalSerializer(cal, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def partial_update(self, request, pk=None):
        self.update(request, pk, partial=True)

    def destroy(self, request, pk=None):
        queryset = Cal.objects.all()
        cal = get_object_or_404(queryset, pk=pk)
        cal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
