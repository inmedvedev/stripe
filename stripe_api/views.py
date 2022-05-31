from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from django.http import JsonResponse
from .models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyView(View):
    def get(self, request, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount_decimal': item.price

                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://0.0.0.0:8000/success',
            cancel_url='https://0.0.0.0:8000/cancel',
        )
        return JsonResponse({
            'id': session.id,
        }, status=200)


class ItemView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = get_object_or_404(Item, id=kwargs['id'])
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'
