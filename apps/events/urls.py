from django.urls import path
from . import views
urlpatterns = [
 path('home',views.user_home, name="user_home"),
 path('upload',views.upload_post,name="upload_post"),

]