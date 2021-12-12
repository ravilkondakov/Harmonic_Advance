from django.test import Client
from django.test import TestCase
from django.urls import reverse

from two_sum.models import Numbers
from two_sum.serializers import NumbersListSerializer


class NumbersViewSetTest(TestCase):
    '''
    create queryset for testing
    '''
    def setUp(self):
        first_data = Numbers.objects.create(numbers=[9, 9], target=18)
        second_data = Numbers.objects.create(numbers=[9, 8, 7, 10], target=19)
        third_data = Numbers.objects.create(numbers=[1, 8, 7, 10], target=9)
        self.client = Client()

    def test_valid_list(self):
        queryset = Numbers.objects.all()
        response = self.client.get(reverse('numbers-list'))
        serializer_data = NumbersListSerializer(queryset, many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_valid_retrieve(self):
        queryset = Numbers.objects.first()
        response = self.client.get('http://127.0.0.1:8000/api/numbers/6/')
        serializer_data = NumbersListSerializer(queryset).data
        self.assertEqual(response.data, serializer_data)
