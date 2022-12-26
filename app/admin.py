from django.contrib import admin

# Register your models here.
from app.models import *

class webpagecustomview(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['name']
    list_display_links=['url']
    list_per_page=2
    search_fields=['name','url']
    list_filter=['url','topic_name','name']





admin.site.register(Topic)

admin.site.register(Webpage,webpagecustomview)

admin.site.register(AccessRecords)