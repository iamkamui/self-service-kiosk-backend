from django.contrib import admin  # noqa

from core.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
