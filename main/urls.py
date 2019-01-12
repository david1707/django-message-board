from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    
    path('admin/', admin.site.urls),
    path('board/', include('message_board.urls')),
    path('users/', include('django.contrib.auth.urls')),
    
]
