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
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework.routers import DefaultRouter

from covid_global import views as covid_global_views

API_TITLE = 'COVID-19 Data API'
API_DESCRIPTION = 'This API provides COVID-19 related data.'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'covid_global', covid_global_views.COVIDGlobalMetaView)
router.register(r'covid_global/active', covid_global_views.COVIDGlobal_ActiveContinentView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
