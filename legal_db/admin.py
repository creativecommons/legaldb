from django.contrib import admin

from .models import Case, FAQ, Link, Scholarship


admin.site.register(Case)
admin.site.register(FAQ)
admin.site.register(Link)
admin.site.register(Scholarship)
