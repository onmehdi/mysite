"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from website.views import pagetest,json_test
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('urladdress','view','name')
    # path('website/',include('website.urls'))
    path('',include('website.urls')),
    # چنانچه یک مسیر زمان تایپ آدرس درون آن اسمی از blog آوردیم منظور مسیر فیزیکی برو توی app blog و پوشه url 
    # برعکس آن روی منوها کار میکند زمانی میزنیم blog: 
    path('blog/',include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
