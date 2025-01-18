from django.contrib import admin
from django.urls import path, include  # importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Redirigimos la URL principal a pages.urls
]
