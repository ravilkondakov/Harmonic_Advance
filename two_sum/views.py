from rest_framework import viewsets
from rest_framework.settings import api_settings

from two_sum.models import Numbers
from two_sum.serializers import CostingSerializer, NumbersListSerializer


class CostingViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = CostingSerializer
    '''
    allow only this method
    '''
    http_method_names = ['post']

    '''
    create new record in db for calculate
    '''
    def perform_create(self, serializer):
        return serializer.save(numbers=self.request.data['numbers'], target=self.request.data['target'])


class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersListSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    '''
    allow only this methods
    '''
    http_method_names = ['get', 'delete', 'retrieve']


