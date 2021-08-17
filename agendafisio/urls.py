from django.contrib import admin
from django.urls import path
from django.urls.conf import include


from agendafisio.core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('agendafisio.core.urls')),
    path('', home, name='home'),
]
