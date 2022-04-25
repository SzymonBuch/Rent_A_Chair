from django.contrib import admin

from .models import Storage, Worker, Product

admin.site.register(Storage)
admin.site.register(Worker)
admin.site.register(Product)