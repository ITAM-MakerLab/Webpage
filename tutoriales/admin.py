from django.contrib import admin
from .models import Tutorial, FeaturedTutorial

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(FeaturedTutorial)
