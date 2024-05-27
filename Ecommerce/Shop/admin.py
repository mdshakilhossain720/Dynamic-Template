from django.contrib import admin

# Register your models here.
from .models import (
    Customer,
    Product,
    OrderPlaced,
)

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price','description','brand ','category',' product_image']

admin.site.register(Product)
