from django.contrib import admin
from .models import Case, FAQ, Link, Scholarship


admin.site.register(Link)
admin.site.register(Scholarship)


class CaseAdmin(admin.ModelAdmin):
    # Customize the order of fields in form
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
    # Customize the listing
    list_display = ("name", "license", "status", "updated_at")
    list_filter = ["status"]


class FAQAdmin(admin.ModelAdmin):
    fields = ("question", "answer", "notes")
    list_display = ("question", "order", "updated_at")


admin.site.register(Case, CaseAdmin)
admin.site.register(FAQ, FAQAdmin)
