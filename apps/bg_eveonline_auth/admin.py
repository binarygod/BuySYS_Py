from django.contrib import admin
from .models import EveUser

# Register your models here.
@admin.register(EveUser)
class EveUserAdmin(admin.ModelAdmin):
    pass