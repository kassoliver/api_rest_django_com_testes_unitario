from django.contrib.auth.models import User
from rest_framework import viewsets
from user.api import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all().order_by('id')

    def retrieve(self, request, pk=None):
        print(pk)
        queryset = User.objects.filter(username=pk)
        user = get_object_or_404(queryset, username=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)
    
    