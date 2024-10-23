from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    # redirecting requests to the main and users app
    path('', include("main.urls")),
    path('users/', include('users.urls')),
]
