from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def index(request):
    logout(request)
    if request.session.get('USER_ID'):
        del(request.session['USER_ID'])
    if request.session.get('USER_NAME'):
        del(request.session['USER_NAME'])
    if request.session.get('USER_EMAIL'):
        del(request.session['USER_EMAIL'])
    
    messages.success(request,"Successfully Signed Out")
    return redirect('Renders Login Page')