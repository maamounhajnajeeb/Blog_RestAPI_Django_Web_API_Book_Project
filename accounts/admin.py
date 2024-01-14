from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, FollowingSystem
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # adding user [adding form and adding fields]
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("name", ) }), )
    # editing user [editing form and editing fields]
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("name", ) }), )
    
    model = CustomUser
    list_display = [
        "email", "username", "name", "is_staff", 
    ]
    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FollowingSystem)