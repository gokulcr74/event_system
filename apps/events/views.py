
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render,redirect
from django.views import generic

from apps.events.forms import UploadForm
from apps.events.models import UserPost



class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Endpoint for Recipe Admin Category Dashboard
    """
    template_name = 'user_home.html'
    form_class = UploadForm
    paginate_by = 5
    login_url = 'Renders Login Page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_posts = UserPost.objects.all().order_by('-created_date')
        context['form_upload'] = UploadForm
        context['user_posts'] = list_posts
        return context

    def form_valid(self, form):
        upload_obj = form.save(commit=False)
        upload_obj.created_by_id = self.request.user.id
        upload_obj.save()
        return redirect('user_home')



