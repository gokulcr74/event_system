import stripe

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect

from apps.core.models import Account
from apps.payment.models import StripePayment


stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
	return render(request, 'home.html')


def charge(request): # new
    if request.method == 'POST':
        try:
            stripe.Customer.modify(
                request.user.stripe_id,
                source=request.POST['stripeToken']
            )
            charge = stripe.Charge.create(
                amount=500,
                currency='inr',
                description='A Django charge',
                customer=request.user.stripe_id
            )
            user_obj=Account.objects.get(id=request.user.id)
            user_obj.paid_user=True
            user_obj.save()
            try:
                pay_stripe=StripePayment(created_by=request.user.id,
                                         email=charge.email
                                         )
                pay_stripe.save()
            except Exception as e:
                pass
            messages.success(request, "Payment has been done. you can post now")
            return redirect('user_home')
        except Exception as e:
            return HttpResponse(e)
