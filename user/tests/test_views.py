from user.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase
import json

class UserListViewTest(TestCase):
    @classmethod
    def setUpTestDataUser(cls):
        number_of_users = 13

        for user_id in range(number_of_users):
            User.objects.create(
                first_name=f'Teste',
                last_name=f'Teste',
                username=f'testeste',
                email=f'teste@gmail.com',
                companies = 1
            )
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)
        print('TESTE URL USER -> OK | STATUS: ',response.status_code)

    def test_get_all_user(self):
        # get API response
        response = self.client.get('/user/')
        # get data from db
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('TESTE GET USER -> OK', response.data, '| STATUS: ',response.status_code)

class CreateNewUserTest(TestCase):
    """ Test module for inserting a new comapny """
    def setUp(self):
        self.valid_user = {
            'first_name': 'Teste',
            'last_name':'Teste',
            'username':'testeste',
            'email':'teste@gmail.com',
            'companies':[]
        }
    def test_create_valid_user(self):
        response = self.client.post(
            ('/user/'),
            data= json.dumps(self.valid_user),
            content_type='application/json'
        )
        print('TESTE POST USER -> OK | STATUS: ',response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
