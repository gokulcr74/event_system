from django.urls import path

from . import views

urlpatterns = [
 path('',views.PostCreateView.as_view(), name="user_home"),

]