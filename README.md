# 🚀 Realtime Chat Application

A modern real-time chat application built with Django, Vue.js, and WebSockets.

## 🎯 Features

- **Real-time Messaging** - Instant message delivery with WebSockets
- **User Authentication** - Secure login and registration
- **Chat Rooms** - Create and join different chat rooms
- **Modern UI** - Beautiful, responsive design with Vue.js
- **Notifications** - Real-time notifications for new messages
- **Cross-platform** - Works on desktop and mobile

## 🛠️ Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Django Channels** - WebSocket support
- **Django REST Framework** - API endpoints
- **PostgreSQL** - Database (Railway)
- **RabbitMQ** - Message broker for WebSockets

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Pinia** - State management
- **Vue Router** - Client-side routing
- **Axios** - HTTP client
- **Vite** - Build tool

### Deployment
- **Railway** - Backend hosting with PostgreSQL
- **Vercel** - Frontend hosting with global CDN

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/DVDHSN/realtime-chat-app.git
cd realtime-chat-app
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. **Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

4. **Access the application**
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## 🌐 Deployment

### Railway + Vercel Deployment

This app is configured for deployment on:
- **Backend**: Railway (Django + PostgreSQL)
- **Frontend**: Vercel (Vue.js + Vite)

#### Backend Deployment (Railway)
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Deploy from GitHub repo: `DVDHSN/realtime-chat-app`
4. Add PostgreSQL database
5. Set environment variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   RAILWAY_ENVIRONMENT=True
   ```

#### Frontend Deployment (Vercel)
1. Go to [vercel.com](https://vercel.com)
2. Import GitHub repository
3. Configure:
   - Framework: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

#### Update URLs
After deployment, update these files with your Railway URL:
- `frontend/src/stores/chat.js`
- `frontend/src/stores/user.js`
- `frontend/vercel.json`

## 📁 Project Structure

```
realtime-chat-app/
├── backend/                 # Django backend
│   ├── chat/               # Django app
│   │   ├── models.py       # Database models
│   │   ├── views.py        # API views
│   │   ├── consumers.py    # WebSocket consumers
│   │   └── serializers.py  # API serializers
│   ├── chat_backend/       # Django project
│   │   ├── settings.py     # Django settings
│   │   ├── urls.py         # URL configuration
│   │   └── asgi.py         # ASGI configuration
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile         # Container configuration
│   └── railway.json       # Railway deployment config
├── frontend/              # Vue.js frontend
│   ├── src/
│   │   ├── components/    # Vue components
│   │   ├── stores/        # Pinia stores
│   │   ├── views/         # Page components
│   │   └── router/        # Vue Router config
│   ├── package.json       # Node.js dependencies
│   └── vercel.json        # Vercel deployment config
└── README.md
```

## 🔧 Configuration

### Environment Variables

#### Backend (Railway)
```bash
SECRET_KEY=your-secret-key
DEBUG=False
RAILWAY_ENVIRONMENT=True
DATABASE_URL=postgresql://...
```

#### Frontend (Vercel)
```bash
VITE_API_URL=https://your-railway-app.railway.app
VITE_WS_URL=wss://your-railway-app.railway.app
```

## 🎨 Features

### Real-time Messaging
- WebSocket connections for instant message delivery
- Message persistence in PostgreSQL
- User typing indicators
- Message timestamps

### User Management
- User registration and authentication
- User profiles with avatars
- Online/offline status
- Session management

### Chat Rooms
- Create and join chat rooms
- Room descriptions and metadata
- Message history per room
- Room-specific WebSocket channels

### Modern UI/UX
- Responsive design for all devices
- Dark/light theme support
- Smooth animations and transitions
- Intuitive navigation

## 🔒 Security

- **HTTPS** - All communications encrypted
- **CORS** - Properly configured for production
- **Authentication** - Secure session management
- **Input Validation** - Server-side validation
- **SQL Injection Protection** - Django ORM

## 📊 Performance

- **Global CDN** - Vercel's edge network
- **Database Indexing** - Optimized queries
- **Caching** - Redis for session storage
- **Auto-scaling** - Railway handles traffic spikes

## 🛠️ Development

### Backend Development
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Development
```bash
cd frontend
npm run dev
npm run build
npm run preview
```

### Testing
```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm run test
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login
- `POST /api/users/logout/` - User logout
- `GET /api/users/me/` - Get current user

### Chat Endpoints
- `GET /api/chatrooms/` - List all rooms
- `POST /api/chatrooms/` - Create new room
- `GET /api/chatrooms/{id}/messages/` - Get room messages
- `POST /api/messages/` - Send message

### WebSocket
- `ws://your-domain/ws/chat/{room_id}/` - Chat room WebSocket

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Django Channels for WebSocket support
- Vue.js team for the amazing framework
- Railway for excellent hosting
- Vercel for frontend deployment

---

🎉 **Ready to chat?** Deploy this app and start messaging in real-time! 