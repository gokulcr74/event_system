from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import json
from apps.events.models import UserPost
from apps.events.forms import UploadForm

def upload_post(request):
    form_data=UploadForm(request.POST,request.FILES)
    if form_data.is_valid():
        upload_obj=form_data.save(commit=False)
        upload_obj.created_by_id=request.session['USER_ID']
        upload_obj.save()
        messages.success(request, 'Posted successfully') 
        return redirect('user_home')
def user_home(request):
    upload_form=UploadForm()
    #query="SELECT up.*,pl.liked_by_id FROM  home_user_post AS up LEFT JOIN home_post_like AS pl ON pl.user_post_id=up.id AND pl.liked_by_id={} order by up.id desc"
    #query=query.format(request.session['USER_ID'])
    #posts_data=User_post.objects.raw(query)
    posts_data=UserPost.objects.all()
    return render(request,'user_home.html',{'form_upload':upload_form,"user_posts":posts_data})
