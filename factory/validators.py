import django_filters
from factory.models import NetworkNode


class NetworkNodeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = NetworkNode
        fields = ['country']
