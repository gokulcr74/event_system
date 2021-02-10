from django.contrib import admin
from apps.events.models import UserPost
# Register your models here.


@admin.register(UserPost)
class AccountAdmin(admin.ModelAdmin):
    raw_id_fields = ['created_by']
    search_fields = ['created_date','created_by__account__email']
