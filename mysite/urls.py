"""mysite URL Configuration

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
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from blog.sitemaps import PostSitemap
from django.conf.urls import handler404,handler500

sitemaps = {
    'posts':PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/' , include('tinymce.urls')),
    path('',include('blog.urls' , namespace='blog')),
    path('sitemap.xml' , sitemap , {'sitemaps':sitemaps} , name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt' , TemplateView.as_view(template_name = 'robots.txt' , content_type = 'text/plain'))
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
