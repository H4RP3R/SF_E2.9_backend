from django.contrib import admin
from app.models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):

    ordering = ['-created']
