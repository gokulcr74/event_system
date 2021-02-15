
import stripe

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect

from apps.core.models import AccountDetail
from apps.payment.models import StripePayment

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
	return render(request, 'home.html')

def charge(request): # new
    if request.method == 'POST':
        try:
            stripe.Customer.modify(
                request.session["STRIPE_ID"],
                source=request.POST['stripeToken']
            )
            charge = stripe.Charge.create(
                amount=500,
                currency='inr',
                description='A Django charge',
                customer=request.session["STRIPE_ID"]
            )
            user_obj=AccountDetail.objects.get(id=request.session["USER_ID"])
            user_obj.paid_user=True
            user_obj.save()
            try:
                pay_stripe=StripePayment(created_by=request.session["USER_ID"],
                                         email=charge.email
                                         )
                pay_stripe.save()
            except Exception as e:
                pass
            request.session["PAID_USER"]=True
            messages.success(request, "Payment has been done. you can post now")
            return redirect('user_home')
        except Exception as e:
            return HttpResponse(e)
        

      