from company import models
from rest_framework import viewsets
from company.api import serializers
from company import models

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all().order_by('id')

