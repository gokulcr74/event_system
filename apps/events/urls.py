from django.urls import path
from . import views
urlpatterns = [
 path('home',views.PostCreateView.as_view(), name="user_home"),

]