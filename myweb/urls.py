"""myweb URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', ''),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^carts/', include('carts.urls', namespace='carts')),
    url(r'^order/', include('order.urls', namespace='order')),
    #url(r'^favicon.ico$', RedirectView.as_view(url='static/favicon.ico'))
]



#handler404 = 'my_app.views.my_custom_page_not_found_view'
#handler500 = 'my_app.views.my_custom_error_view'
#handler403 = 'my_app.views.my_custom_permission_denied_view'