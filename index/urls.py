"""index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from index.schema import schema
from rest_framework_jwt.views import ObtainJSONWebToken #obtain_jwt_token

from core.api.serializers import CustomJWTSerializer

# Don't change anything unless you know what you're doing or have read the documentation and it says so

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('token-auth/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('api/', include('core.api.urls'))
]
