from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "role", "email_verified_at", "created_at")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "subject")
    readonly_fields = ("subject", "created_at", "updated_at")
