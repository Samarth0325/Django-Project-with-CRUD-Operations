from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)     #we call the model data in admin page to store it to database.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')