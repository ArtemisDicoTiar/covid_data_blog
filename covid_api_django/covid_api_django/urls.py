"""covid_api_django URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter

from Apps.CSSE import views as CSSE_views
from Apps.UK import views as UK_views
from Apps.Google import views as GoogleMobility_views
from Apps.OWID import views as OWID_views
from Apps.Helper import views as Helper_views

API_TITLE = 'COVID-19 Data API'
API_DESCRIPTION = 'This API provides COVID-19 related data.'

# Create a router and register our viewsets with it.
router = DefaultRouter()

ptrns = CSSE_views.route.patterns \
        + UK_views.route.patterns \
        + GoogleMobility_views.route.patterns \
        + OWID_views.route.patterns \
        + Helper_views.route.patterns

for ptrn in ptrns:
    router.register(prefix=ptrn.pattern.regex.pattern[1:-1], viewset=ptrn.callback, basename=ptrn.name)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/admin/', admin.site.urls),

    path('api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
