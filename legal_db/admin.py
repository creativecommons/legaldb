from django.contrib import admin
from .models import Case, FAQ, Link, Scholarship


admin.site.register(Case)
admin.site.register(Link)
admin.site.register(Scholarship)


class FAQAdmin(admin.ModelAdmin):
    fields = ("question", "answer", "notes")
    list_display = ("question", "order", "updated_at")


admin.site.register(FAQ, FAQAdmin)
