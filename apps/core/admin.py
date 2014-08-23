__author__ = 'ben'
from .models import HTMLSlug

from django.contrib import admin

class HTMLSlugAdmin(admin.ModelAdmin):
    pass

admin.site.register(HTMLSlug, HTMLSlugAdmin)