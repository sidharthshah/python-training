from django.contrib import admin
from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_time', 'comments')
    list_filter = ('name', )

admin.site.register(LogEntry, LogEntryAdmin)
