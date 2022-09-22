from django.contrib import admin
from .models import Product, Offers


class OfferAdmin(admin. ModelAdmin):
    list_display = ('code', 'description', 'discount')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock') 


admin.site.register(Offers, OfferAdmin)
admin.site.register(Product, ProductAdmin)