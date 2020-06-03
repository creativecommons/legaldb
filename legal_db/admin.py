from django.contrib import admin

from .models import Case, FAQ, Scholarship

admin.site.register(Case)
admin.site.register(Scholarship)
admin.site.register(FAQ)
