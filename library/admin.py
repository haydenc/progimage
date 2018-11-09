from django.contrib import admin

# Register your models here.
from library.models import StoredImage


admin.site.register(StoredImage)