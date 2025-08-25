import random
import string
from django.db import models
from home.models import Dress
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
def get_order_item(order):

    return OrderItem.objects.filter(order = order)

def get_ref_code(date):

    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"ORD-{date}-{rand}"
    

# class cart(models.Model):


# MODEL FOR EACH ORDER(MAY CONTAIN MANY ITEMS)
class Order(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    ref_code = models.CharField(max_length=20)
    ordered_date = models.DateField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    # shipping_address = models.OneToOneField(
    #     ShippingAddress, on_delete=models.SET_NULL, null=True)
    # payment = models.ForeignKey(
    #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    # 'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    order_note = models.TextField(max_length=200, blank=True)
    total_quantity = models.IntegerField()
    total_amount = models.IntegerField()

# TO GET TOTAL QUANTITIY OF THE ORDER
    def get_total_quantity(self):
      total = 0
      for orderitem in get_order_item(self):
          total += orderitem.quantity

      return total

# TO GET TOTAL AMOUNT (SUM AMOUNT OF ALL ITEMS)
    def get_total_amount(self):
      total = 0
      for orderitem in get_order_item(self):
          total += orderitem.item_amount()


      return total

    def save(self, *args, **kwargs):

        self.ref_code = get_ref_code(self.ordered_date)

        self.total_quantity = self.get_total_quantity()
        self.total_amount = self.get_total_amount()
        return super().save(*args,**kwargs)
    
# MODEL FOR EACH ITEM IN A ORDER
class OrderItem(models.Model):
    
    item = models.ForeignKey(Dress, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name
    
    def increment(self,by=1):
        self.quantity += by
        self.save()

    def decrement(self,by=1):
        self.quantity -= by
        self.save()

    def item_amount(self):
        return self.quantity * self.item.price

# MODEL FOR ALL DATA OF SHIPPING ADDRESS    
class ShippingAddress(models.Model):

    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    house_no = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.IntegerField(blank=True)

    def __str__(self):
        return '/'.join([self.house_no, self.block, self.area, self.city, self.state])

    class Meta:
      verbose_name_plural = 'Shipping Addresses'

# MODEL FOR DATA OF PAYMENT
class Payment(models.Model):
    
    JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

    MONTH_CHOICES = [(JANUARY, 'January'), (FEBRUARY, 'February'), (MARCH, 'March'), (APRIL, 'April'), (MAY, 'May'), (JUNE, 'June'), (JULY, 'July'), (AUGUST, 'August'), (SEPTEMBER, 'September'), (OCTOBER, 'October'), (NOVEMBER, 'November'), (DECEMBER, 'December')]
    
    YEAR_CHOICES = [(datetime.now().year+i, datetime.now().year+i) for i in range(0,35)]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    card_holder_name = models.CharField(max_length=40)
    expiration_month = models.CharField(choices=MONTH_CHOICES, max_length=9)
    expiration_year = models.IntegerField(choices=YEAR_CHOICES)
    security_code = models.IntegerField()
    
# MODEL FOR COUPON IF ANY
class Coupon(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True)
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    
    def __str__(self):
        return self.code