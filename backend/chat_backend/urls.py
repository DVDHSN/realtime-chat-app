from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
    path('health/', health_check, name='health_check'),
]

# Add notifs URLs if available
try:
    from notifs.urls import urlpatterns as notifs_urlpatterns
    urlpatterns.append(path('notifs/', include('notifs.urls')))
except ImportError:
    pass 