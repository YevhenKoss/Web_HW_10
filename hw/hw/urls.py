from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_quotes.urls')),
    path('users/', include('app_users.urls')),
    path('author/', include('app_quotes.urls'))
]

