from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", content_type="text/plain")

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🚀 Realtime Chat App</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                overflow-x: hidden;
            }

            .container {
                text-align: center;
                max-width: 800px;
                padding: 2rem;
                animation: fadeInUp 1s ease-out;
            }

            .hero {
                margin-bottom: 3rem;
            }

            .title {
                font-size: 3.5rem;
                font-weight: 700;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #fff, #f0f0f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: glow 2s ease-in-out infinite alternate;
            }

            .subtitle {
                font-size: 1.3rem;
                opacity: 0.9;
                margin-bottom: 2rem;
                animation: fadeIn 1.5s ease-out 0.5s both;
            }

            .status {
                display: inline-block;
                background: rgba(76, 175, 80, 0.2);
                border: 2px solid #4CAF50;
                border-radius: 50px;
                padding: 0.5rem 1.5rem;
                margin-bottom: 2rem;
                animation: pulse 2s infinite;
            }

            .links {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin: 2rem 0;
            }

            .link-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 1.5rem;
                text-decoration: none;
                color: white;
                transition: all 0.3s ease;
                animation: slideInUp 0.8s ease-out both;
            }

            .link-card:nth-child(1) { animation-delay: 0.2s; }
            .link-card:nth-child(2) { animation-delay: 0.4s; }
            .link-card:nth-child(3) { animation-delay: 0.6s; }
            .link-card:nth-child(4) { animation-delay: 0.8s; }

            .link-card:hover {
                transform: translateY(-5px);
                background: rgba(255, 255, 255, 0.2);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }

            .link-icon {
                font-size: 2rem;
                margin-bottom: 0.5rem;
                display: block;
            }

            .link-title {
                font-size: 1.2rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }

            .link-desc {
                font-size: 0.9rem;
                opacity: 0.8;
            }

            .tech-stack {
                margin-top: 3rem;
                padding: 2rem;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                animation: fadeIn 2s ease-out 1s both;
            }

            .tech-title {
                font-size: 1.5rem;
                margin-bottom: 1rem;
                color: #fff;
            }

            .tech-icons {
                display: flex;
                justify-content: center;
                gap: 2rem;
                flex-wrap: wrap;
            }

            .tech-icon {
                font-size: 2.5rem;
                opacity: 0.8;
                transition: all 0.3s ease;
            }

            .tech-icon:hover {
                opacity: 1;
                transform: scale(1.2);
            }

            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            @keyframes slideInUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes glow {
                from { text-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
                to { text-shadow: 0 0 30px rgba(255, 255, 255, 0.8); }
            }

            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }

            .floating {
                animation: floating 3s ease-in-out infinite;
            }

            @keyframes floating {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }

            @media (max-width: 768px) {
                .title { font-size: 2.5rem; }
                .links { grid-template-columns: 1fr; }
                .container { padding: 1rem; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="hero">
                <h1 class="title floating">🚀 Realtime Chat App</h1>
                <p class="subtitle">Your Django backend is running successfully!</p>
                <div class="status">✅ Backend Online</div>
            </div>

            <div class="links">
                <a href="/health/" class="link-card">
                    <span class="link-icon">💚</span>
                    <div class="link-title">Health Check</div>
                    <div class="link-desc">Monitor backend status</div>
                </a>
                
                <a href="/api/" class="link-card">
                    <span class="link-icon">🔌</span>
                    <div class="link-title">API Endpoints</div>
                    <div class="link-desc">REST API documentation</div>
                </a>
                
                <a href="/admin/" class="link-card">
                    <span class="link-icon">⚙️</span>
                    <div class="link-title">Admin Panel</div>
                    <div class="link-desc">Django administration</div>
                </a>
                
                <a href="https://vercel.com" class="link-card" target="_blank">
                    <span class="link-icon">🎨</span>
                    <div class="link-title">Deploy Frontend</div>
                    <div class="link-desc">Deploy Vue.js to Vercel</div>
                </a>
            </div>

            <div class="tech-stack">
                <h3 class="tech-title">Built with Modern Tech Stack</h3>
                <div class="tech-icons">
                    <span class="tech-icon">🐍</span>
                    <span class="tech-icon">⚡</span>
                    <span class="tech-icon">🔌</span>
                    <span class="tech-icon">🐰</span>
                    <span class="tech-icon">🎨</span>
                    <span class="tech-icon">🚀</span>
                </div>
                <p style="margin-top: 1rem; opacity: 0.8;">
                    Django • Channels • WebSockets • RabbitMQ • Vue.js • Real-time
                </p>
            </div>
        </div>
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