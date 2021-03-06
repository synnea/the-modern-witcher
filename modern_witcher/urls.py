"""modern_witcher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from .views import home_view
from accounts import urls as accounts_urls
from shop import urls as shop_urls
from cart import urls as cart_urls
from items import urls as item_urls
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home_view"),
    path('cart/', include(cart_urls)),
    path('user/', include(accounts_urls)),
    path('shop/', include(shop_urls)),
    path('items/', include(item_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


