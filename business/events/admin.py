from django.contrib import admin
from .models import AddUserModel

# Register your models here.
@admin.register(AddUserModel)
class AddUserModelAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'businessname', 'businessaddress', 'phone')