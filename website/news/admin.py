from django.contrib import admin
from django.forms import DateInput
from .models import Post, FeedBack, Documents, Activities, Anti_corrupsion, Plans, Examinations
from django.db import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

@admin.register(FeedBack)
class PostFeedBack(admin.ModelAdmin):
    list_display = ('subject', 'email', 'content', 'created_at', 'ip_address')
    readonly_fields = ('subject', 'email', 'content', 'created_at', 'ip_address')
    search_fields = ['subject', 'content']

@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput},
    }
    list_display = ('title', 'created_at', 'status')

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput},
    }
    list_display = ('title', 'created_at', 'status')

@admin.register(Anti_corrupsion)
class Anti_corrupsionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput},
    }
    list_display = ('title', 'created_at')

@admin.register(Plans)
class Plans_Admin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput},
    }
    list_display = ('title', 'created_at')

@admin.register(Examinations)
class Examinations_Admin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': DateInput},
    }
    list_display = ('title', 'created_at')
