from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menue/', include('menue.urls')),
    path('main/', include('main.urls')),
    path('orders/', include('orders.urls')),
]

urlpatterns += staticfiles_urlpatterns()