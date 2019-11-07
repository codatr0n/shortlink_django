from django.contrib import admin
from .models import Link, Tag

# Configure Models for Admin here
class LinkAdmin(admin.ModelAdmin):
    pass

# Register your models here
admin.site.register(Link, LinkAdmin)
admin.site.register(Tag)

