from django.contrib import admin
from sunny_poster.models import Section

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)