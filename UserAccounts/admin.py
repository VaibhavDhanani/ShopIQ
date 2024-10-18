from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, UserAddress

class UserAddressInline(admin.StackedInline):
    model = UserAddress
    can_delete = True
    verbose_name_plural = 'Address'
    max_num = 1

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'name', 'type', 'phone_number', 'is_active', 'is_staff', 'date_joined']
    list_filter = ['type', 'is_active', 'is_staff', 'date_joined']
    search_fields = ['email', 'name', 'phone_number']
    ordering = ['-date_joined']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('name', 'phone_number', 'date_of_birth')
        }),
        (_('User Type & Status'), {
            'fields': ('type', 'is_active')
        }),
        (_('Business Info'), {
            'fields': ('business_name', 'business_registration_number'),
            'classes': ('collapse',),
            'description': "Only applicable for seller accounts"
        }),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
            'description': "Advanced permissions settings"
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
        (_('User Type'), {
            'fields': ('type',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )
    
    readonly_fields = ['date_joined', 'last_login']
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.type != 'seller':
            # Remove business info fieldset for non-seller users
            return tuple(fs for fs in fieldsets if fs[0] != _('Business Info'))
        return fieldsets

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['get_user_email', 'street_no', 'street_name', 'city', 'state', 'country', 'pincode']
    search_fields = ['users__email', 'city', 'state', 'country']
    list_filter = ['city', 'state', 'country']

    def get_user_email(self, obj):
        return obj.users.first().email if obj.users.exists() else '-'
    get_user_email.short_description = 'User Email'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserAddress, UserAddressAdmin)