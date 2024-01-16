from django.db import models
from django.utils import timezone
from .utils import generate_code


from employees.models import Operator


class Product(models.Model):
    """
    Produtos de venda final
    """
    ITEM_TYPE = {
        'HEAT SHIELD' : "HEAT SHIELD",
        "BRACKET" : "BRACKET",
        "EXHAUST VALVE" : "EXHAUST VALVE",
    }
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=ITEM_TYPE, blank=True)
    price = models.FloatField(help_text = 'euros each')
    image = models.ImageField(upload_to="products", default='default.png')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name} - {self.category}'

class Production(models.Model):
    production_id = models.CharField(max_length=12, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, blank=True)

    date = models.DateField(blank=True)
    quantity = models.IntegerField(blank=True)
    hours_taken = models.IntegerField(blank=True)
    notes = models.TextField(default='No Notes')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.operator.first_name} - {self.quantity}'

    def save(self, *args, **kwargs):
        if self.production_id == "":
            self.production_id = generate_code()
        if self.date is None:
            self.date = timezone.now()
        return super().save(*args, **kwargs)        

class Inventary(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productions = models.ManyToManyField(Production)
    total_quantity = models.IntegerField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.total_quantity} available stock'


