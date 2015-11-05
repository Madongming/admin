"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'visualization.views.index', name='index'),
    url(r'^base_monitor$', 'visualization.views.base_monitor', name='base_monitor'),
    url(r'^conf_dashboard$', 'customization.views.conf_dashboard', name='conf_dashboard'),
    url(r'^manage_pic$', 'customization.views.manage_pic', name='manage_pic'),
    url(r'^database_monitor$', 'visualization.views.database_monitor', name='database_monitor'),
    url(r'^money_of_all$', 'visualization.views.money_of_all', name='money_of_all'),
    url(r'^money_of_province$', 'visualization.views.money_of_province', name='money_of_province'),
    url(r'^order_count$', 'visualization.views.order_count', name='order_count'),
    url(r'^product_count$', 'visualization.views.product_count', name='product_count'),
    url(r'^site_data$', 'visualization.views.site_data', name='site_data'),
    url(r'^dashboard1$', 'visualization.views.dashboard1', name='dashboard1'),
    url(r'^dashboard2$', 'visualization.views.dashboard2', name='dashboard2'),
    url(r'^api/post_profile_data$', 'visualization.views.api_post_profile_data', name='api_post_profile_data'),
    url(r'^api/post_get_profile_data$', 'customization.views.post_get_profile_data', name='post_get_profile_data'),
    url(r'^api/post_update_pic_profile$', 'customization.views.post_update_pic_profile', name='post_update_pic_profile'),
]
