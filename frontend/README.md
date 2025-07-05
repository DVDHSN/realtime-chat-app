# Chat App Frontend

Vue.js 3 + Vite frontend for the realtime chat application.

## 🚀 Quick Deploy to Vercel

### Option 1: Deploy via Vercel Dashboard

1. **Go to [vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import your repository**: `DVDHSN/realtime-chat-app`
5. **Configure settings**:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. **Click "Deploy"**

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow the prompts
```

### Option 3: Deploy via GitHub Integration

1. **Connect your GitHub repo** to Vercel
2. **Select the repository**: `DVDHSN/realtime-chat-app`
3. **Configure build settings**:
   - **Root Directory**: `frontend`
   - **Framework**: Vite
4. **Deploy automatically** on every push

## 🔧 Configuration

The frontend is configured to connect to your Render backend:

- **API URL**: `https://realtime-chat-app-to8j.onrender.com`
- **WebSocket URL**: `wss://realtime-chat-app-to8j.onrender.com`

## 📁 Project Structure

```
frontend/
├── src/
│   ├── views/          # Vue components
│   │   ├── Home.vue
│   │   ├── Login.vue
│   │   ├── Register.vue
│   │   └── Chat.vue
│   ├── stores/         # Pinia stores
│   │   ├── user.js
│   │   ├── chat.js
│   │   └── notification.js
│   ├── router/         # Vue Router
│   │   └── index.js
│   ├── App.vue         # Main app
│   └── main.js         # Entry point
├── public/             # Static assets
├── package.json        # Dependencies
├── vite.config.js      # Vite config
└── vercel.json         # Vercel config
```

## 🛠️ Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 🌐 Environment Variables

The app uses these environment variables (configured in Vercel):

- `VITE_API_URL`: Backend API URL
- `VITE_WS_URL`: WebSocket URL

## 🎨 Features

- **Modern Vue 3** with Composition API
- **Vite** for fast development and building
- **Pinia** for state management
- **Vue Router** for navigation
- **Real-time chat** with WebSockets
- **User authentication**
- **Responsive design**
- **Beautiful UI** with animations

## 🔗 Backend Integration

The frontend connects to your Django backend on Render:

- **Authentication**: Login/Register via API
- **Real-time messaging**: WebSocket connections
- **Room management**: Create and join chat rooms
- **Notifications**: Real-time notifications

## 🚀 Deployment Checklist

- [x] Repository connected to Vercel
- [x] Build settings configured (Vite)
- [x] Environment variables set
- [x] Backend URL configured
- [x] WebSocket URL configured
- [x] CORS settings updated

## 📱 Mobile Support

The app is fully responsive and works on:
- Desktop browsers
- Mobile browsers
- Tablets

## 🔒 Security

- HTTPS enabled by default on Vercel
- Secure WebSocket connections (WSS)
- CORS properly configured
- XSS protection headers

## 🎯 Next Steps

After deployment:

1. **Test the app** at your Vercel URL
2. **Create a user account** via the registration form
3. **Test real-time messaging** between users
4. **Customize the design** if needed

## 🆘 Troubleshooting

### Common Issues

1. **Build fails**: Check Node.js version (18+ required)
2. **API errors**: Verify backend URL in stores
3. **WebSocket errors**: Check WebSocket URL configuration
4. **CORS errors**: Ensure backend CORS settings
5. **Vite build issues**: Check `vite.config.js` configuration

### Getting Help

- Check Vercel deployment logs
- Review browser console for errors
- Verify backend is running on Render
- Test API endpoints directly

---

**Your full-stack chat app is now deployed!** 🎉 