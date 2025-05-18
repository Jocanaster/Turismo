from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from core import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
