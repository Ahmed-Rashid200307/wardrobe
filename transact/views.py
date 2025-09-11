from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from home.models import Dress
from transact.models import Order, OrderItem
from django.contrib.auth.models import User
from user.views import register
# Create your views here.

class CartAction(View):


    def post(self, request):

        if request.user.is_authenticated:

            if self.add_to_cart(request):

                return JsonResponse({'success': True})
            
            else:
                
                return JsonResponse({'success': False})
            
        else:
            
            return JsonResponse({'success': False})


    def add_to_cart(self, req):

        valid_ordered_dress = self.validate_product(req.POST)
        quantity = int(req.POST.get('productQuantity'))

        if valid_ordered_dress:

            order, order_created = Order.objects.get_or_create(
                user = req.user, ordered = False
            )

            order_item, item_created = OrderItem.objects.get_or_create(
                order = order, item = valid_ordered_dress
            )

            if item_created:

                order_item.quantity = quantity

            else:

                order_item.quantity += quantity

            order_item.save()
            order.save()

            return order_item
        
    
    def validate_product(self, post):
        
        dress = Dress.objects.get(name = post.get('productName'))

        if dress.price == int(post.get('productPrice')):
            
            return dress
    


