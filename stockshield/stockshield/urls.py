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
        #description="Welcome to the world of Jaseci",
        #terms_of_service="https://www.jaseci.org",
        #contact=openapi.Contact(email="jason@jaseci.org"),
        #license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'), 
    path('admin/', admin.site.urls),
    path('mystockapi/', include('mystockapi.urls')),
    path('mystockapi-auth/',include('rest_framework.urls')),
    path('mystockapi/rest-auth/', include('rest_auth.urls')),
    path('mystockapi/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view)

]
