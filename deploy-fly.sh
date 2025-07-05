#!/bin/bash

# Fly.io Deployment Script for Realtime Chat App
echo "🚀 Deploying to Fly.io..."

# Check if flyctl is installed
if ! command -v flyctl &> /dev/null; then
    echo "❌ flyctl not found. Please install it first:"
    echo "winget install flyctl"
    exit 1
fi

# Login to Fly.io
echo "🔐 Logging into Fly.io..."
flyctl auth login

# Create PostgreSQL database
echo "🗄️ Creating PostgreSQL database..."
flyctl postgres create --name chat-db --region iad

# Get database connection details
echo "📊 Getting database connection details..."
DB_URL=$(flyctl postgres attach --app chat-db)

# Create the app
echo "📱 Creating Fly.io app..."
cd backend
flyctl apps create realtime-chat-backend --org personal

# Set environment variables
echo "🔧 Setting environment variables..."
flyctl secrets set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
flyctl secrets set DEBUG="False"
flyctl secrets set FLY_APP_NAME="realtime-chat-backend"

# Deploy the app
echo "🚀 Deploying the app..."
flyctl deploy

# Run migrations
echo "🔄 Running database migrations..."
flyctl ssh console -C "python manage.py migrate"

# Create superuser (optional)
echo "👤 Creating superuser..."
flyctl ssh console -C "python manage.py createsuperuser --noinput --username admin --email admin@example.com" || true

echo "✅ Deployment complete!"
echo "🌐 Your app is available at: https://realtime-chat-backend.fly.dev"
echo "📊 Database: chat-db"
echo ""
echo "🔗 Next steps:"
echo "1. Update your frontend to use the new backend URL"
echo "2. Test the WebSocket connection"
echo "3. Configure your domain (optional)" 