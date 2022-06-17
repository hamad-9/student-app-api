"""
Django admin customization.
"""
from django.contrib import admin
from core import models

admin.site.register(models.Student)
