from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,TenantUserProfile,AgentUserProfile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username","email"]


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TenantUserProfile)
admin.site.register(AgentUserProfile)
