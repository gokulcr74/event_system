
from django.db import models
from django.conf import settings

from apps.core.models import AccountDetail


class StripePayment(models.Model):
    created_by = models.ForeignKey(AccountDetail, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(verbose_name="email", max_length=60,unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.description