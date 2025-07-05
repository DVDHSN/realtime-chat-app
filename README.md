# Realtime Chat Application

A modern, real-time chat application built with **Vue.js**, **Django**, **Django Channels**, **RabbitMQ**, and **uWSGI**. Features WebSocket-based real-time messaging, user authentication, room management, and notifications.

## 🚀 Features

- **Real-time Messaging**: Instant message delivery using WebSockets
- **User Authentication**: Secure login/register system
- **Room Management**: Create and join different chat rooms
- **Notifications**: Real-time notifications using django-notifs
- **Modern UI**: Beautiful, responsive design with Vue.js 3
- **WebSocket Support**: Full WebSocket integration for real-time communication
- **Message Broker**: RabbitMQ for reliable message handling
- **Production Ready**: Docker and uWSGI configuration included

## 🛠️ Tech Stack

### Frontend
- **Vue.js 3** with Composition API
- **Pinia** for state management
- **Vue Router** for navigation
- **Vite** for fast development
- **Axios** for HTTP requests

### Backend
- **Django 4.2** with REST Framework
- **Django Channels** for WebSocket support
- **django-notifs** for notification system
- **channels-rabbitmq** for message broker
- **uWSGI** for production serving

### Infrastructure
- **RabbitMQ** as message broker
- **Redis** for caching and sessions
- **Nginx** as reverse proxy
- **Docker** for containerization

## 📋 Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chat-application
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - RabbitMQ Management: http://localhost:15672 (guest/guest)
   - Nginx: http://localhost:80

### Local Development

1. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Start RabbitMQ**
   ```bash
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```

## 📁 Project Structure

```
chat-application/
├── backend/                 # Django backend
│   ├── chat_backend/       # Django project settings
│   ├── chat/              # Chat app
│   │   ├── models.py      # Database models
│   │   ├── views.py       # API views
│   │   ├── consumers.py   # WebSocket consumers
│   │   ├── serializers.py # DRF serializers
│   │   └── routing.py     # WebSocket routing
│   └── requirements.txt   # Python dependencies
├── frontend/              # Vue.js frontend
│   ├── src/
│   │   ├── views/        # Vue components
│   │   ├── stores/       # Pinia stores
│   │   ├── router/       # Vue Router
│   │   └── App.vue       # Main app component
│   └── package.json      # Node dependencies
├── nginx/                # Nginx configuration
├── docker-compose.yml    # Docker services
└── README.md
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
REDIS_URL=redis://localhost:6379/0
```

### Django Settings

Key settings in `backend/chat_backend/settings.py`:

- **Channels Configuration**: RabbitMQ as channel layer
- **CORS Settings**: Configured for frontend communication
- **REST Framework**: Session authentication
- **Database**: SQLite for development (change for production)

## 🎯 API Endpoints

### Authentication
- `POST /api/users/login/` - User login
- `POST /api/users/register/` - User registration
- `POST /api/users/logout/` - User logout
- `GET /api/users/me/` - Get current user

### Chat Rooms
- `GET /api/rooms/` - List all rooms
- `POST /api/rooms/` - Create new room
- `GET /api/rooms/{id}/messages/` - Get room messages

### Messages
- `GET /api/messages/` - List messages
- `POST /api/messages/` - Send message

### WebSocket Endpoints
- `ws://localhost:8000/ws/chat/{room_name}/` - Chat WebSocket
- `ws://localhost:8000/ws/notifications/` - Notifications WebSocket

## 🔌 WebSocket Events

### Chat Events
```javascript
// Send message
{
  "message": "Hello, world!"
}

// Receive message
{
  "message": "Hello, world!",
  "username": "john_doe",
  "user_id": 1
}
```

### Notification Events
```javascript
// Receive notification
{
  "type": "notification",
  "message": "New message in General",
  "notification_type": "info"
}
```

## 🎨 Frontend Features

### Components
- **Home**: Landing page with feature overview
- **Login/Register**: Authentication forms
- **Chat**: Main chat interface with rooms and messaging
- **Notifications**: Real-time notification system

### State Management
- **User Store**: Authentication and user data
- **Chat Store**: Messages, rooms, and WebSocket connection
- **Notification Store**: Notification management

## 🐳 Docker Deployment

### Production Build
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Start production services
docker-compose -f docker-compose.prod.yml up -d
```

### Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit environment variables
nano .env
```

## 🔒 Security Considerations

- **HTTPS**: Configure SSL certificates for production
- **Secret Key**: Change Django secret key in production
- **Database**: Use PostgreSQL for production
- **Rate Limiting**: Configured in Nginx
- **CORS**: Properly configured for your domain

## 📊 Monitoring

### Health Checks
- Application: `GET /health`
- RabbitMQ: `http://localhost:15672`
- Redis: `redis-cli ping`

### Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure production database (PostgreSQL)
- [ ] Set secure `SECRET_KEY`
- [ ] Configure HTTPS with SSL certificates
- [ ] Set up proper CORS settings
- [ ] Configure static file serving
- [ ] Set up monitoring and logging
- [ ] Configure backup strategy

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-secure-secret-key
DATABASE_URL=postgresql://user:pass@host:port/db
RABBITMQ_URL=amqp://user:pass@host:port/
REDIS_URL=redis://host:port/0
ALLOWED_HOSTS=your-domain.com
CORS_ALLOWED_ORIGINS=https://your-domain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **WebSocket Connection Failed**
   - Check if RabbitMQ is running
   - Verify WebSocket URL in frontend
   - Check CORS settings

2. **Messages Not Sending**
   - Verify user authentication
   - Check room permissions
   - Review WebSocket consumer logs

3. **Docker Issues**
   - Ensure Docker and Docker Compose are installed
   - Check if ports are available
   - Review container logs

### Getting Help

- Check the logs: `docker-compose logs`
- Review the configuration files
- Ensure all services are running
- Verify network connectivity between containers

## 📚 Additional Resources

- [Django Channels Documentation](https://channels.readthedocs.io/)
- [Vue.js 3 Documentation](https://vuejs.org/)
- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Docker Documentation](https://docs.docker.com/)

---

**Happy Chatting! 💬** 