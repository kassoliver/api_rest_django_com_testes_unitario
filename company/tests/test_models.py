from django.test import TestCase
from company.models import Company

class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='Teste Teste', cnpj=12345678912345)

    def test_name_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        print('TESTE LABEL NAME - COMPANY -> OK')

    def test_cnpj_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('cnpj').verbose_name
        self.assertEquals(field_label, 'cnpj')
        print('TESTE LABEL CNPJ - COMPANY -> OK')
        
    def test_name_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
        print('TESTE MAX_LENGTH NAME - COMPANY -> OK')

    def test_cnpj_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('cnpj').max_length
        self.assertEquals(max_length, 14)
        print('TESTE MAX_LENGTH CNPJ - COMPANY -> OK')

