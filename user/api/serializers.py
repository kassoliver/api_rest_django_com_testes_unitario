import company
from company.api.serializers import CompanySerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','username', 'email','companies')
        extra_kwargs = {'companies': {'required': False}}

        

