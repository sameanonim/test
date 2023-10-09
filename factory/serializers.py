from rest_framework import serializers
from .models import NetworkNode, Product, Factory, RetailNetwork, IndividualEntrepreneur
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=NetworkNode.objects.all(), allow_null=True)
    products = ProductSerializer(many=True)

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)

    class Meta:
        model = NetworkNode
        fields = ['name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt', 'created_at', 'level', 'products']


class FactorySerializer(NetworkNodeSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = Factory


class RetailNetworkSerializer(NetworkNodeSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = RetailNetwork
        fields = NetworkNodeSerializer.Meta.fields + ['website']


class IndividualEntrepreneurSerializer(NetworkNodeSerializer):
    class Meta(NetworkNodeSerializer.Meta):
        model = IndividualEntrepreneur
        fields = NetworkNodeSerializer.Meta.fields + ['user']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data