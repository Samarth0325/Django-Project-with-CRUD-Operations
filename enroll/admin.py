from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)     #we call the model data in admin page to store it to database.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')