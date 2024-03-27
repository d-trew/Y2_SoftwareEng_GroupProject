from django.contrib import admin
from django.urls import path, include

from account.views import activateemail


urlpatterns = [
    path('api/', include('account.urls')),
        path('activateemail/', activateemail, name='activateemail'),
    path('admin/', admin.site.urls),
]