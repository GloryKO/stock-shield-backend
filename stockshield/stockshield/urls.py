"""stockshield URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
#from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Inventory API'
API_DESCRIPTION = 'An Inventory API for stockshield.'
schema_view = get_schema_view(title=API_TITLE)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Inventory API",
        default_version='v1',
       
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'), 
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('stockshield-auth/',include('rest_framework.urls')),
    path('stockshield/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('stockshield/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view)

]
