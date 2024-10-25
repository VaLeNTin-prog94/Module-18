"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tempfile import template

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from task2.views import class_templates
#from task3.views import games_templates,carts_templates,platforms_templates
from task4.views import games_templates,carts_templates,platforms_templates
from task5.views import sign_up_by_django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes', class_templates),
    path('func/', TemplateView.as_view(template_name='second_task/func_template.html')),
    path('platform/', platforms_templates),
    path('platform/games/', games_templates),
    path('platform/cart/', carts_templates),
    path('register/', sign_up_by_django ),

]
