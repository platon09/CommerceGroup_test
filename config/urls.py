from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include('employees.urls')),
    path('api/docs/', include_docs_urls(
        title='Test API documentation'
    )),
]

admin.site.site_header = _("Test Admin")
admin.site.site_title = _("Test Admin Portal")
admin.site.index_title = _("Welcome to Test Portal")