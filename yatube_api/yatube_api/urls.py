from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.urls import api_urls_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls_list)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
