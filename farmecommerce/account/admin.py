from django.contrib import admin
from .models import products,Cart,Orders
# Register your models here.

admin.site.register(products)
admin.site.register(Cart)
admin.site.register(Orders)
