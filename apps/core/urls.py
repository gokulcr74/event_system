from django.urls import path
from . import views
urlpatterns = [
 path('',views.Loginview.as_view(), name="Renders Login Page"),
 path('signup',views.signup,name="signup"),
 path('signup/<int:id>',views.signup,name="signup"),
 path('sssss',views.signup,name="Clears the session and redirects to login page"),
]