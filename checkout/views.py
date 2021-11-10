from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's is nothing in your bag at the moment!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JuHvAIwlcZhoWVt0Bz8CxK8kGiTNkRnaj3XqnuFLG62nGhkPC9MoNSJ4UKhIxAXFwiwoJnvpffgCxSgbEHQ8orT00gm2RQli6',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)