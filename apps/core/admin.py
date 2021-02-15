from django.contrib import admin

from apps.core.models import Account




@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ['user_last_name','user_first_name','email']