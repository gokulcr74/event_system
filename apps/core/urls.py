from django.urls import path
from . import views
urlpatterns = [
path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
 path('',views.Loginview.as_view(), name="Renders Login Page"),
 path('signup',views.signup,name="signup"),
 path('signup/<int:id>',views.signup,name="signup"),
]