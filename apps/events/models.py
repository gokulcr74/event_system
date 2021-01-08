from django.db import models
from django.conf import settings
from apps.core.models import AccountDetail
# Create your models here.
class UserPost(models.Model):
    created_by=models.ForeignKey(AccountDetail, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    description=models.TextField(max_length=400,null=True)
    status= models.SmallIntegerField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now_add=True)
    event_start_date=models.DateTimeField()
    event_end_date=models.DateTimeField()
    event_place=models.TextField(max_length=400,null=True)
    def __str__(self):
        return self.description