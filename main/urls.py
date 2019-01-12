from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('message_board.urls')),
    path('users/', include('django.contrib.auth.urls')),
    
]
