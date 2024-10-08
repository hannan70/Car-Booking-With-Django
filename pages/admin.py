from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = "Photo"

    list_display = ('full_name', 'last_name', 'designation', 'thumbnail')
    list_display_links = ("full_name", )
    search_fields = ('first_name', 'last_name', 'designation',)
    list_filter = ("designation",)


admin.site.register(Team, TeamAdmin)
