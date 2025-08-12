from django.contrib import admin
from .models import Dress,Category,Variant, Size

class sizeInTab(admin.ModelAdmin):
    pass
    

class VarInline(admin.StackedInline):
    model = Variant
    
    extra = 3

class DressAdmin(admin.ModelAdmin):
    inlines = [VarInline]
    list_display = ("name", "available_sizes")

    def available_sizes(self, obj):
        return ", ".join([s.name for s in obj.size.all()])
    available_sizes.short_description = "Sizes"

    actions_selection_counter =False
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Dress, DressAdmin)
# admin.site.register(Variant)