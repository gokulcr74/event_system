from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View 
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from apps.core.forms import FormLogin,UserMasterForm,UserDetailForm
from apps.core.models import Account,AccountDetail
from apps.core.tokens import account_activation_token
class Loginview(View):

    def get(self,request):
      form_login= FormLogin()
      return render(request, 'loginpage.html', {"form_login": form_login})

    def post(self,request):
       form_data=FormLogin(request.POST)
       if form_data.is_valid():
            username=form_data.cleaned_data.get('username')
            password=form_data.cleaned_data.get('password')
            try:
                user = authenticate(email=username, password=password)
            except Exception as e:
                return HttpResponse(e)
            if user == None:
                messages.error(request, 'Incorrect Username or Password')
                return self.get(request)
            else:
                request.session['USER_EMAIL'] = user.email
                request.session['IS_SUPER_USER'] = user.is_superuser
                try:
                   user_detail=AccountDetail.objects.get(account_id=user.id)
                   request.session['USER_ID']=user_detail.id
                except Exception as e:
                    return HttpResponse(e)
                request.session['USER_NAME'] = user_detail.user_first_name
                return redirect("user_home")


def signup(request):
    form_user_master=UserMasterForm(request.POST or None)
    form_user_detail=UserDetailForm(request.POST or None)
    if form_user_master.is_valid() and form_user_detail.is_valid():
        account_obj = form_user_master.save(commit=False)
        account_obj.is_active = False
        account_obj.password_reset = True
        account_obj.type_of_user = 2
        account_obj.set_password(form_user_master.cleaned_data.get('password'))
        account_obj.save()
        account_detail_obj = form_user_detail.save(commit=False)
        account_detail_obj.account = account_obj
        account_detail_obj.save()
        to_email=account_obj.email
        mail_subject = 'Welcome to '+settings.SITE_NAME+'!'
        mail_template ='email/acc_active_email.html'
        site_url1 = settings.SITE_URL
        site_url1 = site_url1[:-1]
        mail_contents = {
        'user': account_detail_obj.user_first_name+' '+account_detail_obj.user_last_name,
        'uid':urlsafe_base64_encode(force_bytes(account_obj.pk)),
        'token':account_activation_token.make_token(account_obj),
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
        email.send()
        messages.success(request, 'Please verify or email')
        return redirect('Renders Login Page')
    return render(request, 'add_user.html', {"form_user_master":form_user_master,"form_user_detail":form_user_detail})


def activate(request, uidb64, token):
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
        request.session['username'] = user.email
        messages.success(request, 'Please login to continue')
        return redirect('Renders Login Page')
    else:
        messages.error(request, 'Invalid Verification link')
    return redirect("Renders Login Page")

