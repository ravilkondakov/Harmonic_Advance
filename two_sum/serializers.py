from rest_framework import serializers

from two_sum.models import Numbers


class CostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('costing',)


class NumbersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ('numbers', 'target',)
