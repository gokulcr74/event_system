
import stripe

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from apps.core.forms import FormLogin, UserMasterForm
from apps.core.models import Account
from apps.core.tokens import account_activation_token

stripe.api_key = settings.STRIPE_SECRET_KEY


class Loginview(View):
    """ End point for login user """

    def get(self, request):
      form_login = FormLogin()
      return render(request, 'loginpage.html', {
          "form_login": form_login
          })

    def post(self,request):
       form_data = FormLogin(request.POST)
       if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            try:
                user = authenticate(email=username, password=password)
            except Exception as e:
                return HttpResponse(e)
            if user == None:
                messages.error(request, 'Incorrect Username or Password')
                return self.get(request)
            else:
                login(request, user)
                return redirect("user_home")


def signup(request):
    form_user_master = UserMasterForm(request.POST or None)
    if form_user_master.is_valid():
        account_obj = form_user_master.save(commit=False)
        account_obj.is_active = True
        account_obj.password_reset = True
        account_obj.type_of_user = 2
        account_obj.set_password(form_user_master.cleaned_data.get('password'))
        account_obj.save()
        to_email=account_obj.email  # fetching email address for sending verification link
        customer = stripe.Customer.create(
            description="My First Test Customer (created for API docs)",
            email=account_obj.email,
            name= account_obj.user_first_name
            )
        account_obj.stripe_id=customer.id
        account_obj.save()
        # creating contents for sending mail for account verifcation
        mail_subject = 'Welcome to '+settings.SITE_NAME+'!'
        mail_template ='email/acc_active_email.html'
        site_url1 = settings.SITE_URL
        site_url1 = site_url1[:-1]
        mail_contents = {
        'user': account_obj.user_first_name+
        ' '+account_obj.user_last_name,
        'uid': urlsafe_base64_encode(force_bytes(account_obj.pk)),
        'token': account_activation_token.make_token(account_obj),
        'site_url1': site_url1
        }
        from_name = settings.EMAIL_FROM_NAME
        mail_contents['site_name'] = settings.SITE_NAME
        mail_contents['site_url'] = settings.SITE_URL
        email_message = render_to_string(mail_template, mail_contents)
        email = EmailMessage(
            mail_subject, email_message, from_name, to=[to_email]
        )
        email.content_subtype = 'html'
        try:
            email.send()  #sending email for verification
        except Exception as e:
            pass
        messages.success(request, 'Please verify or email')
        return redirect('Renders Login Page')
    return render(request, 'add_customer.html', {
        "form_user_master":form_user_master,
        })


def activate(request, uidb64, token):
    """Checking the validity of a link"""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if not user.password_reset:
          messages.error(
            request, 'Invalid verification link!')
          return redirect("Renders Login Page")
    if user is not None and account_activation_token.check_token(user, token):      
        user.is_active = True
        user.password_reset = False
        user.save()
        messages.success(request, 'Please login to continue')
        return redirect('Renders Login Page')
    else:
        messages.error(request, 'Invalid Verification link')
    return redirect("Renders Login Page")

