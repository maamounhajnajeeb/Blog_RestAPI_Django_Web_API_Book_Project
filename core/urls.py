"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from drf_spectacular.views import (
    SpectacularAPIView,  SpectacularRedocView, SpectacularSwaggerSplitView,
    )

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # machine documenting (dynamic approach) (downloadable url)
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema_api"),
    
    # human friendly documenting (swagger approach) 
    path("api/v1/schema/swagger/", SpectacularSwaggerSplitView.as_view(url_name="swagger_api", ), name="swagger_api", ),
    
    # human friendly documenting (redoc approach) 
    path("api/v1/schema/redoc/", SpectacularRedocView.as_view(url_name="redoc_api", ), name="redoc_api", ),
    
    # view api by hand
    path('api/v1/', include("posts.urls", namespace="posts_api")),
    
    # auth api by rest framework
    path("api-auth/", include("rest_framework.urls", namespace="auth_api")),
    
    # django rest auth 3rd party package
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    
    # django_rest_auth and allauth 3rd party pacakges combination
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    
]
