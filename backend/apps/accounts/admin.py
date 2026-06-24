from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "external_subject", "created_at")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "external_subject")

