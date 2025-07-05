# 🚀 Fly.io + Vercel Deployment Guide

This guide will help you deploy your real-time chat app with:
- **Backend**: Fly.io (Django + WebSockets)
- **Frontend**: Vercel (Vue.js)
- **Database**: Fly.io PostgreSQL

## Prerequisites

1. **Fly.io Account**: Sign up at [fly.io](https://fly.io)
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **GitHub Repository**: Your code should be on GitHub

## Step 1: Deploy Backend to Fly.io

### 1.1 Install Fly CLI
```bash
# Windows
winget install flyctl

# macOS
brew install flyctl

# Linux
curl -L https://fly.io/install.sh | sh
```

### 1.2 Login to Fly.io
```bash
flyctl auth login
```

### 1.3 Create PostgreSQL Database
```bash
# Create a PostgreSQL database
flyctl postgres create --name chat-db --region iad

# Attach it to your app
flyctl postgres attach --app chat-db
```

### 1.4 Deploy the Backend
```bash
# Navigate to backend directory
cd backend

# Create the app
flyctl apps create realtime-chat-backend --org personal

# Set environment variables
flyctl secrets set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
flyctl secrets set DEBUG="False"
flyctl secrets set FLY_APP_NAME="realtime-chat-backend"

# Deploy
flyctl deploy
```

### 1.5 Run Database Migrations
```bash
# Run migrations
flyctl ssh console -C "python manage.py migrate"

# Create superuser (optional)
flyctl ssh console -C "python manage.py createsuperuser --noinput --username admin --email admin@example.com"
```

## Step 2: Deploy Frontend to Vercel

### 2.1 Connect GitHub to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### 2.2 Environment Variables
Add these environment variables in Vercel:
```
VITE_API_URL=https://realtime-chat-backend.fly.dev
VITE_WS_URL=wss://realtime-chat-backend.fly.dev
```

## Step 3: Test Your Deployment

### 3.1 Backend Health Check
Visit: `https://realtime-chat-backend.fly.dev/health/`

### 3.2 Frontend Test
Visit your Vercel URL and test:
- User registration/login
- Room creation
- Real-time messaging

## Step 4: Custom Domain (Optional)

### 4.1 Backend Domain
```bash
# Add custom domain to Fly.io app
flyctl certs add your-domain.com
```

### 4.2 Frontend Domain
1. Go to Vercel dashboard
2. Select your project
3. Go to "Settings" → "Domains"
4. Add your custom domain

## Troubleshooting

### Common Issues

#### 1. Database Connection Error
```bash
# Check database status
flyctl postgres status --app chat-db

# View logs
flyctl logs
```

#### 2. WebSocket Connection Issues
- Ensure your frontend is using `wss://` (secure WebSocket)
- Check CORS settings in Django
- Verify the WebSocket URL in your frontend code

#### 3. Build Errors
```bash
# Check build logs
flyctl logs

# Rebuild locally
flyctl deploy --local-only
```

### Useful Commands

```bash
# View app status
flyctl status

# View logs
flyctl logs

# SSH into the app
flyctl ssh console

# Scale the app
flyctl scale count 1

# View database
flyctl postgres connect --app chat-db
```

## Cost Optimization

### Fly.io Free Tier
- **Apps**: 3 apps
- **PostgreSQL**: 1 database (256MB)
- **Bandwidth**: 3GB/month
- **Compute**: 3 shared-cpu-1x 256mb VMs

### Vercel Free Tier
- **Projects**: Unlimited
- **Bandwidth**: 100GB/month
- **Builds**: 100 builds/month

## Monitoring

### Fly.io Monitoring
```bash
# View metrics
flyctl dashboard

# Monitor logs
flyctl logs --follow
```

### Vercel Analytics
- Built-in analytics in Vercel dashboard
- Performance monitoring
- Error tracking

## Security Best Practices

1. **Environment Variables**: Never commit secrets to Git
2. **HTTPS**: Always use HTTPS in production
3. **CORS**: Configure CORS properly
4. **Database**: Use strong passwords for database
5. **Logs**: Monitor logs for security issues

## Backup Strategy

### Database Backup
```bash
# Create backup
flyctl postgres backup create --app chat-db

# List backups
flyctl postgres backup list --app chat-db
```

### Code Backup
- Use Git for version control
- Regular commits and pushes
- Consider using GitHub Actions for CI/CD

## Performance Tips

1. **Database Indexing**: Add indexes to frequently queried fields
2. **Caching**: Implement Redis caching for better performance
3. **CDN**: Use Vercel's global CDN
4. **Compression**: Enable gzip compression
5. **Monitoring**: Set up alerts for performance issues

## Support

- **Fly.io Docs**: [fly.io/docs](https://fly.io/docs)
- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **Django Docs**: [djangoproject.com](https://djangoproject.com)
- **Vue.js Docs**: [vuejs.org](https://vuejs.org)

---

🎉 **Congratulations!** Your real-time chat app is now deployed on Fly.io + Vercel! 