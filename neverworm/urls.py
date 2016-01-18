"""neverworm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from orders.views import wishlist_detail, place_wish, Dashboard
from users.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^wishlist/(?P<pk>[0-9]+)/$', wishlist_detail, name='wishlist_detail'),
    url(r'^wishlist/(?P<pk>[0-9]+)/place_wish/$', place_wish, name='place_wish'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
