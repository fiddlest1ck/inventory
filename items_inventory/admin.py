from django.contrib import admin

from items_inventory.models import Record, History
# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record, RecordAdmin)

class HistoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(History, HistoryAdmin)