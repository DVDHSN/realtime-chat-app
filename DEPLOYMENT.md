# 🚀 Deployment Guide - Free Platforms

## **Option 1: Render (Recommended - Easiest)**

### Setup:
1. Go to [render.com](https://render.com) and sign up
2. Connect your GitHub repo
3. Create a new **Web Service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd backend && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT`
   - **Environment Variables**:
     - `SECRET_KEY`: (auto-generated)
     - `DEBUG`: `false`
     - `ALLOWED_HOSTS`: `your-app-name.onrender.com`

4. Create a **PostgreSQL Database**:
   - Add the `DATABASE_URL` environment variable to your web service

### Pros:
- ✅ Free tier: 750 hours/month
- ✅ PostgreSQL included
- ✅ Easy deployment
- ✅ Automatic HTTPS

---

## **Option 2: Fly.io (Best Performance)**

### Setup:
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. Deploy: `fly launch`
4. Add PostgreSQL: `fly postgres create`

### Pros:
- ✅ Free tier: 3 VMs, always-on
- ✅ Global deployment
- ✅ Better performance

---

## **Option 3: Railway Split Deployment**

### Backend (Railway):
1. Deploy backend to Railway
2. Use Railway's free PostgreSQL
3. Set environment variables

### Frontend (Vercel):
1. Deploy frontend to Vercel (free)
2. Update API URLs to point to Railway backend

---

## **Option 4: Heroku (Alternative)**

### Setup:
1. Install Heroku CLI
2. Create app: `heroku create your-app-name`
3. Add PostgreSQL: `heroku addons:create heroku-postgresql:mini`
4. Deploy: `git push heroku main`

### Pros:
- ✅ Free tier available (with limitations)
- ✅ Easy deployment
- ✅ Good documentation

---

## **Quick Deploy Commands**

### For Render:
```bash
# Push to GitHub first
git add .
git commit -m "Ready for deployment"
git push origin main

# Then deploy via Render dashboard
```

### For Fly.io:
```bash
fly launch
fly postgres create
fly deploy
```

---

## **Environment Variables Needed**

```bash
SECRET_KEY=your-secret-key
DEBUG=false
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://...
RABBITMQ_URL=amqp://guest:guest@localhost:5672/
```

---

## **Which Platform Should You Choose?**

- **Beginner**: Render (easiest setup)
- **Performance**: Fly.io (always-on, faster)
- **Split deployment**: Railway + Vercel
- **Traditional**: Heroku

**Recommendation**: Start with **Render** - it's the easiest and most reliable for your chat app! 