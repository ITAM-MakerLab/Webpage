from . import models
from django.contrib import admin

admin.site.register(models.BlogEntry)
admin.site.register(models.FeaturedBlogEntry)