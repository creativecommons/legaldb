from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import Case, FAQ, Link, Scholarship


class CaseAdmin(admin.ModelAdmin):
    # Customize order of fields in edit form
    fields = (
        "name",
        "related_cases",
        "country",
        "courts",
        "decision_year",
        "is_pending",
        "license",
        "tags",
        "background",
        "summary",
        "links",
        "status",
        "contributor_name",
        "contributor_email",
        "notes",
    )
    # Customize the list
    list_display = ("name", "license", "status", "updated_at")
    list_filter = ["status", "license"]
    search_fields = ("name", "courts", "related_cases", "background", "summary")


class LinkAdmin(admin.ModelAdmin):
    # Customize the list
    list_display = ("url", "title")


class ScholarshipAdmin(admin.ModelAdmin):
    # Customize order of fields in edit form
    fields = (
        "title",
        "authors",
        "publication_name",
        "publication_year",
        "license",
        "tags",
        "summary",
        "link",
        "status",
        "contributor_name",
        "contributor_email",
        "notes",
    )
    # Customize the list
    list_display = ("title", "license", "status", "updated_at")
    list_filter = ["status", "license"]
    search_fields = ("title", "authors", "summary")


class FAQAdmin(OrderedModelAdmin):
    fields = ("question", "answer", "notes")
    list_display = ("question", "order", "move_up_down_links", "updated_at")


admin.site.register(Case, CaseAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Scholarship, ScholarshipAdmin)
