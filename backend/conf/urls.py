"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from common.views import SidebarView

# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("common.urls")),
    path("api/v1/onboarding/", include("onboarding.urls")),
    path("api/v1/deals/", include("deals.urls")),
    path("api/v1/prospects/", include("prospect.urls")),
    path("api/v1/email-template/",include("email_template.urls")),
    path("api/v1/api-auth/", include("rest_framework.urls")),
    path('sidebar', SidebarView.as_view(), name='sidebar'),
    path("api/v1/scraping/", include("social_media_scraping.urls")),
    # DOCUMENTATION
    # path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/v1/swagger-docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/docs/', TemplateView.as_view(template_name='swagger.html', extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
]

# urlpatterns += static("zuri-root-config.js", document_root="react-spa/dist/zuri-root-config.js")
# urlpatterns += static("/static/zuri-zuri-plugin-company-sales-prospects.js", document_root="react-spa/epictetus/dist/zuri-zuri-plugin-company-sales-prospects.js")
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
