from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", content_type="text/plain")

def home(request):
    return HttpResponse("""
    <html>
    <head><title>Realtime Chat App</title></head>
    <body>
        <h1>🚀 Realtime Chat App</h1>
        <p>Your Django backend is running successfully!</p>
        <ul>
            <li><a href="/health/">Health Check</a></li>
            <li><a href="/api/">API Endpoints</a></li>
            <li><a href="/admin/">Admin Panel</a></li>
        </ul>
        <p>Deploy your Vue frontend to Vercel to complete the full-stack app!</p>
    </body>
    </html>
    """, content_type="text/html")

urlpatterns = [
    path('', home, name='home'),
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