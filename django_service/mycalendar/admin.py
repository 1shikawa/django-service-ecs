from django.contrib import admin
from .models import Schedule, LargeItem, MiddleItem
from django.contrib.auth.admin import UserAdmin


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('LargeItem', 'summary', 'kosu', 'date', 'totalkosu', 'register')
    list_display_links = ('LargeItem',)


class LargeItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class MiddleItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

# admin.site.register(User, UserAdmin)


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(LargeItem, LargeItemAdmin)
admin.site.register(MiddleItem, MiddleItemAdmin)
