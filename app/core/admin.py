from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('personal info'), {'fields': ('name',)}),
        (
            _('permission'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('important'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
