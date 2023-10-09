from rest_framework import viewsets
from .permissions import IsActiveEmployee
from factory.validators import NetworkNodeFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Factory, RetailNetwork, IndividualEntrepreneur
from .serializers import FactorySerializer, MyTokenObtainPairSerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_class = NetworkNodeFilter
    permission_classes = [IsActiveEmployee]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_class = NetworkNodeFilter
    permission_classes = [IsActiveEmployee]


class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    filter_class = NetworkNodeFilter
    permission_classes = [IsActiveEmployee]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
