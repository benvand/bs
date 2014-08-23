__author__ = 'ben'

from django.db import models
from django.contrib.sites.models import Site

class HTMLSlug(models.Model):
    site = models.OneToOneField(Site)
    favicon = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    path_to_favicon = models.CharField(max_length=255, blank=True, null=True)
    home_url_name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return '%s html slugs' % self.site.name

    def __str__(self):
        return str(self.__unicode__())