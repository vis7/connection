from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserModelForm, UserProfileModelForm

class CustomUserAdmin(UserAdmin):
    add_form = UserModelForm
    # form = UserProfileModelForm
    model = User
    # list_display = ['username', 'email']

# class WorkPlaceInline(admin.StackedInline):
#     model = WorkPlace
#     extra = 2

# class UserAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Basic',       {'fields':['username']})
#     ]
#     inlines = [WorkPlaceInline]

# Register your models here.
admin.site.register(User)

# admin.site.register(CustomUserAdmin)
