#!/bin/bash

echo "🚀 Deploying to Render..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if remote is set
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No remote repository found. Please add your GitHub repo:"
    echo "   git remote add origin https://github.com/yourusername/your-repo.git"
    exit 1
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git add .
git commit -m "Deploy to Render - $(date)"
git push origin main

echo "✅ Code pushed to GitHub!"
echo ""
echo "🎯 Next steps:"
echo "1. Go to https://render.com"
echo "2. Sign up/Login with GitHub"
echo "3. Click 'New Web Service'"
echo "4. Connect your GitHub repository"
echo "5. Configure:"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: cd backend && python manage.py migrate && python manage.py runserver 0.0.0.0:\$PORT"
echo "6. Add environment variables:"
echo "   - SECRET_KEY: (auto-generate)"
echo "   - DEBUG: false"
echo "   - ALLOWED_HOSTS: your-app-name.onrender.com"
echo "7. Create PostgreSQL database and add DATABASE_URL"
echo ""
echo "🌐 Your app will be available at: https://your-app-name.onrender.com" 