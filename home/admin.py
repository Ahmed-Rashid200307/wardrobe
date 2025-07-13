from django.contrib import admin
from .models import Dress,Category,Variant

# Register your models here.
admin.site.register(Dress)
admin.site.register(Category)
admin.site.register(Variant)