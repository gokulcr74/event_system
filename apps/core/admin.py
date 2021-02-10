from django.contrib import admin

from apps.core.models import Account,AccountDetail

admin.site.register(Account)


@admin.register(AccountDetail)
class AccountAdmin(admin.ModelAdmin):
    raw_id_fields = ['account']
    search_fields = ['user_last_name','user_first_name','account__email']