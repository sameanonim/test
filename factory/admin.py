# Импортируем необходимые модули
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Product


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt', 'created_at', 'level')
    list_display_links = ('name',)
    list_filter = ('city',)
    search_fields = ('name', 'email')
    fields = ('name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt')
    raw_id_fields = ('supplier',)
    

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        city = request.GET.get('city')
        if city:
            qs = qs.filter(city=city)
        return qs

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

admin.site.register(Factory, NetworkNodeAdmin)
admin.site.register(RetailNetwork, NetworkNodeAdmin)
admin.site.register(IndividualEntrepreneur, NetworkNodeAdmin)
admin.site.register(Product)
