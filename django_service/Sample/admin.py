from django.contrib import admin

# Register your models here.
from .models import Sample, Test

class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Sample, SampleAdmin)
admin.site.register(Test, TestAdmin)