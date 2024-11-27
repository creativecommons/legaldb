"""caselaw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Third-party
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import set_language

if settings.DEBUG:
    # Third-party
    import debug_toolbar

# Non-translated URLs (admin and markdownx)
urlpatterns = [
    re_path(r"^markdownx/", include("markdownx.urls")),
    path("admin/", admin.site.urls),
    path("set_language/", set_language, name="set_language"),
]

# URLs with language code prefixes
urlpatterns += i18n_patterns(
    path("", include("legal_db.urls")),
)
if settings.DEBUG:
    urlpatterns += i18n_patterns(
        path("__debug__/", include(debug_toolbar.urls)),
    )
