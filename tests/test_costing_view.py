import json

from django.test import Client
from django.test import TestCase


class CostingViewTest(TestCase):
    def setUp(self):
        '''
        create a pseudo-user
        '''
        self.client = Client()

    def test_valid_post_costing(self):
        '''
        create data for dumps into request
        '''
        data = {
            'numbers': [1, 2, 3, 4, 5],
            'target': 8
        }
        response = self.client.post('http://127.0.0.1:8000/api/', json.dumps(data), content_type='application/json')
        result_data = {"costing": (2, 4)}
        self.assertEqual(result_data, response.data)

    def test_invalid_post_costing(self):
        data = {
            'numbers': [1, 2, 3, 4, 5],
            'target': 10
        }
        response = self.client.post('http://127.0.0.1:8000/api/', json.dumps(data), content_type='application/json')
        result_data = {
            "costing": {
                "error": "no data satisfying the conditions"
            }
        }
        self.assertEqual(result_data, response.data)
