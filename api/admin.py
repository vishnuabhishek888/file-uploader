# In yourapp/admin.py
from django.contrib import admin
from .models import UploadedFile

admin.site.register(UploadedFile)
