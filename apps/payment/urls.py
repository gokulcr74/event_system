from django.urls import path
from . import views

urlpatterns = [
    path('account_creation',views.index, name="stripe_account_creation"),
    path('payment',views.charge,name='charge')
]