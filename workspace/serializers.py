from rest_framework import serializers

from . import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('code', 'name', 'email',)


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Operator
        fields = ('code', 'name', 'email', 'turn')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class GroupProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupProduct
        fields = '__all__'
