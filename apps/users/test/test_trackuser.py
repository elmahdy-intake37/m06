import enum
import json

import requests
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from apps.users.models import User, TrackUser




class TrackUserTest(APITestCase):
    """
    Happy Scenario simulates how user interact with M06
    - register and get token to be authorized
    - fetch user most usage
    """

    def setUp(self):
        API_PREFIX = '/api/v1'
        self.register_url = API_PREFIX + '/auth/register'
        self.get_product_one = API_PREFIX + '/product/one/'
        self.get_product_two = API_PREFIX + '/product/two/'
        self.most_usage_url = API_PREFIX +  '/most_usage/'
        self.client = APIClient(raise_request_exception=True)
        data = {
            'email': 'test@example.com',
            'first_name':'test',
            'last_name':'test2',
            'password': 'test@12345'
        }
        # Hitting register endpoint and get token
        response = self.client.post(self.register_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        token = response.data.get('auth_token')
        self.authorization = 'Token ' + token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.authorization
        }

        # Authorize any upcomming requests with current token
        self.client.credentials(HTTP_AUTHORIZATION=self.authorization)

    def test_track_user(self):
        data = {'title': 'test'}
        self.client.post(self.get_product_one, data=data)
        self.client.post(self.get_product_two, data=data)
        self.client.get(self.get_product_one)
        self.client.get(self.get_product_one)
        self.client.get(self.get_product_two)
        response = self.client.get(self.most_usage_url)
        self.assertEqual(response.data[0]['count'], 2)
        self.assertEqual(response.data[1]['count'], 1)