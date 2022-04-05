from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin

from enterprise_catalog.apps.curation import models


class EnterpriseCurationAdmin(SimpleHistoryAdmin):
    """ Admin configuration for the EnterpriseCuration model. """
    list_display = (
        'uuid',
        'enterprise_uuid',
        'title',
    )
    search_fields = (
        'uuid',
        'enterprise_uuid',
    )


class CatalogHighlightSetAdmin(SimpleHistoryAdmin):
    """ Admin config for CatalogHighlightSet model. """
    list_display = (
        'uuid',
        'title',
        'enterprise_uuid',
        'enterprise_curation',
        'enterprise_catalog',
        'title',
    )
    search_fields = (
        'uuid',
        'enterprise_uuid',
        'enterprise_catalog',
        'enterprise_curation',
    )


class HighlightedContentAdmin(SimpleHistoryAdmin):
    """ Admin config for HighlightedContent model. """
    list_display = (
        'uuid',
        'catalog_highlight_set',
        'content_metadata',
    )
    search_fields = (
        'uuid',
        'catalog_highlight_set',
        'content_metadata',
    )


admin.site.register(models.EnterpriseCuration, EnterpriseCurationAdmin)
admin.site.register(models.CatalogHighlightSet, CatalogHighlightSetAdmin)
admin.site.register(models.HighlightedContent, HighlightedContentAdmin)
