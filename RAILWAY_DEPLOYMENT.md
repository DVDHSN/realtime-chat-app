# 🚀 Railway + Vercel Deployment Guide

This guide will help you deploy your real-time chat app with:
- **Backend**: Railway (Django + WebSockets)
- **Frontend**: Vercel (Vue.js)
- **Database**: Railway PostgreSQL

## 🎯 Why Railway?

### ✅ Advantages
- **WebSocket Support** - Perfect for real-time chat
- **PostgreSQL Database** - Included in deployment
- **Easy Deployment** - Git-based, automatic
- **Good Free Tier** - $5 credit monthly
- **No Sleep** - Always running
- **Global CDN** - Fast worldwide

### 📊 Comparison

| Platform | WebSockets | Database | Free Tier | Sleep |
|----------|------------|----------|-----------|-------|
| **Railway** | ✅ | ✅ PostgreSQL | $5/month | ❌ |
| **Render** | ✅ | ✅ PostgreSQL | 750h/month | ✅ |
| **Fly.io** | ✅ | ✅ PostgreSQL | 3GB bandwidth | ❌ |
| **Heroku** | ✅ | ✅ PostgreSQL | ❌ | ❌ |

## Step 1: Deploy Backend to Railway

### 1.1 Sign Up for Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Create a new project

### 1.2 Connect Your Repository
1. Click "Deploy from GitHub repo"
2. Select your repository: `DVDHSN/realtime-chat-app`
3. Railway will detect the `railway.json` configuration

### 1.3 Configure Environment Variables
Add these environment variables in Railway dashboard:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
RAILWAY_ENVIRONMENT=True
```

### 1.4 Add PostgreSQL Database
1. In Railway dashboard, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically connect it to your app

### 1.5 Deploy
Railway will automatically:
- Build your Docker image
- Run migrations
- Start your Django app
- Provide a URL like: `https://your-app-name.railway.app`

## Step 2: Update Frontend URLs

### 2.1 Update Chat Store
```javascript
// frontend/src/stores/chat.js
const API_BASE_URL = 'https://your-app-name.railway.app'
const WS_BASE_URL = 'wss://your-app-name.railway.app'
```

### 2.2 Update User Store
```javascript
// frontend/src/stores/user.js
const API_BASE_URL = 'https://your-app-name.railway.app'
```

### 2.3 Update Vercel Configuration
```json
// frontend/vercel.json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://your-app-name.railway.app/api/$1"
    },
    {
      "source": "/ws/(.*)",
      "destination": "wss://your-app-name.railway.app/ws/$1"
    }
  ]
}
```

## Step 3: Deploy Frontend to Vercel

### 3.1 Connect to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Configure:
   - **Framework**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### 3.2 Environment Variables
Add in Vercel dashboard:
```
VITE_API_URL=https://your-app-name.railway.app
VITE_WS_URL=wss://your-app-name.railway.app
```

## Step 4: Test Your Deployment

### 4.1 Backend Health Check
Visit: `https://your-app-name.railway.app/health/`

### 4.2 Frontend Test
Visit your Vercel URL and test:
- ✅ User registration/login
- ✅ Room creation
- ✅ Real-time messaging
- ✅ WebSocket connections

## Railway Dashboard Features

### 📊 Monitoring
- **Logs**: Real-time application logs
- **Metrics**: CPU, memory, network usage
- **Deployments**: Automatic from Git pushes

### 🔧 Management
- **Environment Variables**: Easy to manage
- **Database**: PostgreSQL with pgAdmin
- **Domains**: Custom domain support

## Cost Breakdown

### Railway Free Tier
- **$5 credit/month**
- **PostgreSQL**: ~$2-3/month
- **App hosting**: ~$2-3/month
- **Total**: ~$5/month

### Vercel Free Tier
- **Projects**: Unlimited
- **Bandwidth**: 100GB/month
- **Builds**: 100 builds/month
- **Total**: Free

## Troubleshooting

### Common Issues

#### 1. Database Connection
```bash
# Check Railway logs
railway logs

# Verify DATABASE_URL is set
railway variables
```

#### 2. WebSocket Issues
- Ensure Railway app supports WebSockets
- Check CORS settings
- Verify WebSocket URL in frontend

#### 3. Build Errors
```bash
# Check build logs
railway logs

# Rebuild locally
railway up
```

### Useful Commands

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# View logs
railway logs

# Open dashboard
railway open

# Deploy
railway up
```

## Performance Tips

1. **Database Indexing**: Add indexes to frequently queried fields
2. **Caching**: Implement Redis for better performance
3. **CDN**: Railway provides global CDN
4. **Monitoring**: Use Railway's built-in monitoring
5. **Scaling**: Railway auto-scales based on traffic

## Security Best Practices

1. **Environment Variables**: Never commit secrets
2. **HTTPS**: Railway provides automatic HTTPS
3. **CORS**: Configure properly for your domain
4. **Database**: Use strong passwords
5. **Logs**: Monitor for security issues

## Backup Strategy

### Database Backup
- Railway provides automatic PostgreSQL backups
- Manual backups available in dashboard
- Point-in-time recovery available

### Code Backup
- Use Git for version control
- Railway auto-deploys from Git
- Consider GitHub Actions for CI/CD

## Support Resources

- **Railway Docs**: [railway.app/docs](https://railway.app/docs)
- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **Django Docs**: [djangoproject.com](https://djangoproject.com)
- **Vue.js Docs**: [vuejs.org](https://vuejs.org)

---

🎉 **Congratulations!** Your real-time chat app is now deployed on Railway + Vercel!

## Quick Start Checklist

- [ ] Sign up for Railway
- [ ] Connect GitHub repository
- [ ] Add PostgreSQL database
- [ ] Set environment variables
- [ ] Deploy backend
- [ ] Update frontend URLs
- [ ] Deploy frontend to Vercel
- [ ] Test real-time functionality
- [ ] Monitor performance 