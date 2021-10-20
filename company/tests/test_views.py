from company.api.serializers import CompanySerializer
from django.test import TestCase
from rest_framework import status
from company.models import Company
import json

class CompanyListViewTest(TestCase):
    @classmethod
    def setUpTestDataCompany(cls):
        # Create 13 comapnies for pagination tests
        number_of_companies = 13

        for company_id in range(number_of_companies):
            Company.objects.create(
                name=f'Teste',
                cnpj=f'12345678912345',
            )
        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('TESTE URL COMPANY -> OK | STATUS: ',response.status_code)

    def test_get_all_companies(self):
        # get API response
        response = self.client.get('/company/')
        # get data from db
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        print('Listando todas as empresas:' , company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('TESTE GET COMPANY -> OK| STATUS: ',response.status_code)

class CreateNewCompanyTest(TestCase):
    """ Test module for inserting a new company """
    def setUp(self):
        self.valid_company = {
            'name': 'Hero',
            'cnpj':'55630289000386',
        }
    def test_create_valid_company(self):
        response = self.client.post(
            ('/company/'),
            data= json.dumps(self.valid_company),
            content_type='application/json'
        )
        print(response.data)
        print('TESTE POST COMPANY -> OK', '| STATUS: ',response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

