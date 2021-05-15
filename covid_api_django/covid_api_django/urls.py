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

from Apps.CSSE import views as CSSE_views
from covid_global import views as covid_global_views
from covid_info import views as covid_info_views

API_TITLE = 'COVID-19 Data API'
API_DESCRIPTION = 'This API provides COVID-19 related data.'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'covid_global', covid_global_views.COVIDGlobalMetaView)

router.register(r'covid/cases/global', covid_info_views.COVID_CasesView)
router.register(r'covid/cases/uk', covid_info_views.UK_CasesView)
router.register(r'covid/prediction/global', covid_info_views.COVID_Cases_predictionView)
router.register(r'covid/prediction/uk', covid_info_views.UK_Cases_predictionView)
router.register(r'covid/pred_accuracy/global', covid_info_views.COVID_Cases_prediction_accuracyView)
router.register(r'covid/pred_accuracy/uk', covid_info_views.UK_Cases_prediction_accuracyView)

router.register(r'google_mobility', covid_info_views.Google_MobilityView)

router.register(r'owid/health', covid_info_views.OWID_healthView)
router.register(r'owid/mortality', covid_info_views.OWID_mortalityView)
router.register(r'owid/testing', covid_info_views.Google_MobilityView)
router.register(r'owid/vaccination', covid_info_views.Google_MobilityView)

for ptrn in CSSE_views.route.patterns:
    router.register(prefix=ptrn.pattern.regex.pattern[1:-1], viewset=ptrn.callback, basename=ptrn.name)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
