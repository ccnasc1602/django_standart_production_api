from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from . import models
from . import serializers



class CompanyView(ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def get(self, request):
        return Response(request.data, status=status.HTTP_200_OK)


class OperatorView(ModelViewSet):
    queryset = models.Operator.objects.all()
    serializer_class = serializers.OperatorSerializer

    def get(self, request):
        return Response(request.data, status=status.HTTP_200_OK)


class PersonView(ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def get(self, request):
        return Response(request.data, status=status.HTTP_200_OK)


class GroupProductsView(ModelViewSet):
    queryset = models.GroupProduct.objects.all()
    serializer_class = serializers.GroupProductSerializer

    def get(self, request):
        return Response(request.data, status=status.HTTP_200_OK)
