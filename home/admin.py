from django.contrib import admin
from .models import Dress,Category,Variant

class VarInline(admin.StackedInline):
    model = Variant
    
    extra = 3

class DressAdmin(admin.ModelAdmin):
    inlines = [VarInline]
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Dress, DressAdmin)
# admin.site.register(Variant)