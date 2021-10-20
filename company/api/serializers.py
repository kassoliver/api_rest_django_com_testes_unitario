from rest_framework import serializers
from company import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['id']
        model = models.Company
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}