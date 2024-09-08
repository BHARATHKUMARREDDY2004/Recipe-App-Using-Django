"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import *
from receipe.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('recipes/', receipes, name= 'recipes'),
    path('delete_recipe/<id>', delete_recipe, name= 'delete_recipe'),
    path('update_recipe/<id>', update_recipe, name= 'update_recipe'),
    path('register/', register_page, name='register_page'),


    path('success-page/', success_page, name= 'success_page'),
    path('scores/', scores_page, name= 'scores_page'),
    path('skills/', skills_page, name= 'skills_page'),
    path('projects/', projects_page, name= 'projects_page'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()