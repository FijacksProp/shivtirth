from django.contrib import admin
from .models import *
from django.db import models
# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

class EnquireAdmin(admin.ModelAdmin):
    list_display = ['pack', 'date_created']
    readonly_fields = ('date_created',)

class MyPackage(admin.ModelAdmin):
    list_display = ['name', 'date_created']

class MyGallery(admin.ModelAdmin):
    list_display = ['img_name', 'date_created']

# class MyComment(admin.ModelAdmin):
#     list_display = ['name', 'date_created']

# Register your models here.

admin.site.register(Post, MyAdmin)
admin.site.register(Special_Packages, MyAdmin)
admin.site.register(Comment)
admin.site.register(Packages, MyPackage)
admin.site.register(Contact)
admin.site.register(Enquire, EnquireAdmin)
admin.site.register(Gallery, MyGallery)
