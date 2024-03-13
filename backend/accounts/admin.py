from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Partner

class PartnerInline(admin.StackedInline):
    model = Partner
    can_delete = False
    verbose_name_plural = 'Partner'

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'active_job')


class CustomUserAdmin(BaseUserAdmin):
    inlines = (PartnerInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_company_name')

    def get_company_name(self, obj):
        return obj.partner.company_name if hasattr(obj, 'partner') else None

    get_company_name.short_description = 'Company Name'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Partner, PartnersAdmin)
