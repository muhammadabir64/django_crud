from django.contrib import admin
from .models import User_Info

@admin.register(User_Info)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')