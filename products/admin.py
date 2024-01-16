from django.contrib import admin

from .models import Product, Inventary, Production

admin.site.register(Product)
admin.site.register(Inventary)
admin.site.register(Production)


