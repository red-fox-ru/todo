from django.contrib import admin
from .models import Task


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complete')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('complete',)
    list_filter = ('complete',)


admin.site.register(Task, TodoAdmin)