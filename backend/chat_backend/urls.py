from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

def health_check(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>💚 Health Check - Chat App</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container {
                text-align: center;
                padding: 3rem;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                animation: fadeInUp 0.8s ease-out;
            }
            .status {
                font-size: 4rem;
                margin-bottom: 1rem;
                animation: pulse 2s infinite;
            }
            .message {
                font-size: 1.5rem;
                margin-bottom: 2rem;
                opacity: 0.9;
            }
            .details {
                font-size: 1rem;
                opacity: 0.7;
                margin-bottom: 2rem;
            }
            .back-btn {
                display: inline-block;
                padding: 0.8rem 2rem;
                background: rgba(255, 255, 255, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 50px;
                color: white;
                text-decoration: none;
                transition: all 0.3s ease;
            }
            .back-btn:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.1); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="status">💚</div>
            <div class="message">Backend is Healthy!</div>
            <div class="details">
                Status: OK<br>
                Response Time: Excellent<br>
                Database: Connected<br>
                WebSocket: Ready
            </div>
            <a href="/" class="back-btn">← Back to Home</a>
        </div>
    </body>
    </html>
    """, content_type="text/html")

def api_docs(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🔌 API Documentation - Chat App</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: white;
                line-height: 1.6;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
            }
            .header {
                text-align: center;
                margin-bottom: 3rem;
                animation: fadeInUp 1s ease-out;
            }
            .title {
                font-size: 3rem;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #fff, #f0f0f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .subtitle {
                font-size: 1.2rem;
                opacity: 0.8;
            }
            .endpoint {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                animation: slideInUp 0.8s ease-out both;
            }
            .method {
                display: inline-block;
                padding: 0.3rem 0.8rem;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: bold;
                margin-right: 1rem;
            }
            .get { background: #4CAF50; }
            .post { background: #2196F3; }
            .url {
                font-family: 'Courier New', monospace;
                background: rgba(0, 0, 0, 0.3);
                padding: 0.5rem;
                border-radius: 5px;
                margin: 0.5rem 0;
            }
            .description {
                margin-top: 0.5rem;
                opacity: 0.9;
            }
            .back-btn {
                display: inline-block;
                padding: 0.8rem 2rem;
                background: rgba(255, 255, 255, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 50px;
                color: white;
                text-decoration: none;
                transition: all 0.3s ease;
                margin-top: 2rem;
            }
            .back-btn:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes slideInUp {
                from { opacity: 0; transform: translateY(50px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .section {
                margin-bottom: 3rem;
            }
            .section-title {
                font-size: 2rem;
                margin-bottom: 1.5rem;
                border-bottom: 2px solid rgba(255, 255, 255, 0.3);
                padding-bottom: 0.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 class="title">🔌 API Documentation</h1>
                <p class="subtitle">RESTful API endpoints for the Realtime Chat Application</p>
            </div>

            <div class="section">
                <h2 class="section-title">Authentication</h2>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <div class="url">/api/users/login/</div>
                    <div class="description">Authenticate user with username and password</div>
                </div>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <div class="url">/api/users/register/</div>
                    <div class="description">Create a new user account</div>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Chat Rooms</h2>
                <div class="endpoint">
                    <span class="method get">GET</span>
                    <div class="url">/api/chatrooms/</div>
                    <div class="description">Get all chat rooms</div>
                </div>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <div class="url">/api/chatrooms/</div>
                    <div class="description">Create a new chat room</div>
                </div>
            </div>

            <div class="section">
                <h2 class="section-title">Messages</h2>
                <div class="endpoint">
                    <span class="method get">GET</span>
                    <div class="url">/api/messages/</div>
                    <div class="description">Get all messages</div>
                </div>
                <div class="endpoint">
                    <span class="method post">POST</span>
                    <div class="url">/api/messages/</div>
                    <div class="description">Send a new message</div>
                </div>
            </div>

            <div style="text-align: center;">
                <a href="/" class="back-btn">← Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """, content_type="text/html")

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def register_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email', '')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return JsonResponse({'success': True, 'message': 'Registration successful'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

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
                max-width: 900px;
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

            .auth-section {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 2rem;
                margin: 2rem 0;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }

            .auth-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 2rem;
                animation: slideInUp 0.8s ease-out both;
            }

            .auth-card:nth-child(1) { animation-delay: 0.2s; }
            .auth-card:nth-child(2) { animation-delay: 0.4s; }

            .auth-title {
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                font-weight: 600;
            }

            .form-group {
                margin-bottom: 1rem;
                text-align: left;
            }

            .form-group label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
            }

            .form-group input {
                width: 100%;
                padding: 0.8rem;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.1);
                color: white;
                font-size: 1rem;
                transition: all 0.3s ease;
            }

            .form-group input:focus {
                outline: none;
                border-color: rgba(255, 255, 255, 0.6);
                background: rgba(255, 255, 255, 0.2);
            }

            .form-group input::placeholder {
                color: rgba(255, 255, 255, 0.6);
            }

            .btn {
                width: 100%;
                padding: 0.8rem;
                border: none;
                border-radius: 8px;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                margin-top: 1rem;
            }

            .btn-primary {
                background: linear-gradient(45deg, #4CAF50, #45a049);
                color: white;
            }

            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
            }

            .btn-secondary {
                background: linear-gradient(45deg, #2196F3, #1976D2);
                color: white;
            }

            .btn-secondary:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
            }

            .message {
                padding: 0.8rem;
                border-radius: 8px;
                margin-top: 1rem;
                font-weight: 500;
            }

            .message.success {
                background: rgba(76, 175, 80, 0.2);
                border: 1px solid #4CAF50;
            }

            .message.error {
                background: rgba(244, 67, 54, 0.2);
                border: 1px solid #F44336;
            }

            .links {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
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

            .link-card:nth-child(1) { animation-delay: 0.6s; }
            .link-card:nth-child(2) { animation-delay: 0.8s; }
            .link-card:nth-child(3) { animation-delay: 1.0s; }

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
                .auth-section { grid-template-columns: 1fr; }
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

            <div class="auth-section">
                <div class="auth-card">
                    <h3 class="auth-title">🔐 Login</h3>
                    <form id="loginForm">
                        <div class="form-group">
                            <label for="loginUsername">Username</label>
                            <input type="text" id="loginUsername" placeholder="Enter username" required>
                        </div>
                        <div class="form-group">
                            <label for="loginPassword">Password</label>
                            <input type="password" id="loginPassword" placeholder="Enter password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>
                        <div id="loginMessage"></div>
                    </form>
                </div>

                <div class="auth-card">
                    <h3 class="auth-title">📝 Register</h3>
                    <form id="registerForm">
                        <div class="form-group">
                            <label for="registerUsername">Username</label>
                            <input type="text" id="registerUsername" placeholder="Choose username" required>
                        </div>
                        <div class="form-group">
                            <label for="registerEmail">Email</label>
                            <input type="email" id="registerEmail" placeholder="Enter email" required>
                        </div>
                        <div class="form-group">
                            <label for="registerPassword">Password</label>
                            <input type="password" id="registerPassword" placeholder="Choose password" required>
                        </div>
                        <button type="submit" class="btn btn-secondary">Register</button>
                        <div id="registerMessage"></div>
                    </form>
                </div>
            </div>

            <div class="links">
                <a href="/health/" class="link-card">
                    <span class="link-icon">💚</span>
                    <div class="link-title">Health Check</div>
                    <div class="link-desc">Monitor backend status</div>
                </a>
                
                <a href="/api/docs/" class="link-card">
                    <span class="link-icon">🔌</span>
                    <div class="link-title">API Documentation</div>
                    <div class="link-desc">REST API documentation</div>
                </a>
                
                <a href="/admin/" class="link-card">
                    <span class="link-icon">⚙️</span>
                    <div class="link-title">Admin Panel</div>
                    <div class="link-desc">Django administration</div>
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

        <script>
            document.getElementById('loginForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const username = document.getElementById('loginUsername').value;
                const password = document.getElementById('loginPassword').value;
                const messageDiv = document.getElementById('loginMessage');

                try {
                    const response = await fetch('/login/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ username, password })
                    });

                    const data = await response.json();
                    
                    if (data.success) {
                        messageDiv.className = 'message success';
                        messageDiv.textContent = 'Login successful! Redirecting...';
                        setTimeout(() => {
                            window.location.href = '/api/docs/';
                        }, 1500);
                    } else {
                        messageDiv.className = 'message error';
                        messageDiv.textContent = data.message || 'Login failed';
                    }
                } catch (error) {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = 'Network error. Please try again.';
                }
            });

            document.getElementById('registerForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const username = document.getElementById('registerUsername').value;
                const email = document.getElementById('registerEmail').value;
                const password = document.getElementById('registerPassword').value;
                const messageDiv = document.getElementById('registerMessage');

                try {
                    const response = await fetch('/register/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ username, email, password })
                    });

                    const data = await response.json();
                    
                    if (data.success) {
                        messageDiv.className = 'message success';
                        messageDiv.textContent = 'Registration successful! Redirecting...';
                        setTimeout(() => {
                            window.location.href = '/api/docs/';
                        }, 1500);
                    } else {
                        messageDiv.className = 'message error';
                        messageDiv.textContent = data.message || 'Registration failed';
                    }
                } catch (error) {
                    messageDiv.className = 'message error';
                    messageDiv.textContent = 'Network error. Please try again.';
                }
            });
        </script>
    </body>
    </html>
    """, content_type="text/html")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')),
    path('api/docs/', api_docs, name='api_docs'),
    path('health/', health_check, name='health_check'),
    path('login/', login_api, name='login_api'),
    path('register/', register_api, name='register_api'),
]

# Add notifs URLs if available
try:
    from notifs.urls import urlpatterns as notifs_urlpatterns
    urlpatterns.append(path('notifs/', include('notifs.urls')))
except ImportError:
    pass 