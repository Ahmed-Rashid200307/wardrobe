from django.contrib import admin
from .models import Order,OrderItem,Coupon,ShippingAddress,Payment
# Register your models here.

class PaymentInLine(admin.StackedInline):
    model = Payment
    extra = 0
class CouponInLine(admin.StackedInline):
    model = Coupon

class ShippingInLine(admin.StackedInline):
    model = ShippingAddress
    extra = 0
    
class ItemInline(admin.StackedInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline,ShippingInLine,CouponInLine,PaymentInLine]
    

# admin.site.register(Order, OrderAdmin)