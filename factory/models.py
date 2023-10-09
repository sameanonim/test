# Импортируем необходимые модули
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NetworkNode(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='customers')
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    level = models.IntegerField()

    def set_level(self):
        if self.supplier is None:
            self.level = 0
        else:
            self.level = self.supplier.level + 1

    def validate_level(self):
        if self.level > 2:
            raise ValueError('Уровень иерархии не может быть больше 2')
        if self.level == 2 and not isinstance(self, IndividualEntrepreneur):
            raise ValueError('Звено с уровнем 2 должно быть индивидуальным предпринимателем')
        if self.level == 1 and not isinstance(self, RetailNetwork):
            raise ValueError('Звено с уровнем 1 должно быть розничной сетью')
        if self.level == 0 and not isinstance(self, Factory):
            raise ValueError('Звено с уровнем 0 должно быть заводом')

    def save(self, *args, **kwargs):
        self.set_level()
        self.validate_level()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.supplier:
            return f'{self.name} (уровень {self.level}, поставщик: {self.supplier.name})'
        else:
            return f'{self.name} (уровень {self.level})'
    
    class Meta:
        ordering = ['level', 'name']


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    release_date = models.DateField()


class Factory(NetworkNode):
    products = models.ManyToManyField(Product)


class RetailNetwork(NetworkNode):
    website = models.URLField()
    products = models.ManyToManyField(Product)


class IndividualEntrepreneur(NetworkNode):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
