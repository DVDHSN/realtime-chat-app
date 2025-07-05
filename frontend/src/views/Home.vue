<template>
  <div class="home">
    <div class="hero-section">
      <h1>Welcome to Realtime Chat</h1>
      <p class="subtitle">Connect with others in real-time using WebSockets, Django Channels, and RabbitMQ</p>
      
      <div class="features">
        <div class="feature">
          <div class="feature-icon">💬</div>
          <h3>Real-time Messaging</h3>
          <p>Instant message delivery with WebSocket connections</p>
        </div>
        <div class="feature">
          <div class="feature-icon">🔔</div>
          <h3>Smart Notifications</h3>
          <p>Get notified about new messages and events</p>
        </div>
        <div class="feature">
          <div class="feature-icon">👥</div>
          <h3>Multiple Rooms</h3>
          <p>Join different chat rooms and conversations</p>
        </div>
      </div>

      <div class="cta-buttons">
        <router-link to="/chat" class="btn btn-primary" v-if="userStore.isAuthenticated">
          Start Chatting
        </router-link>
        <router-link to="/login" class="btn btn-secondary" v-else>
          Get Started
        </router-link>
      </div>
    </div>

    <div class="tech-stack">
      <h2>Built with Modern Technologies</h2>
      <div class="tech-grid">
        <div class="tech-item">
          <h4>Frontend</h4>
          <ul>
            <li>Vue.js 3 with Composition API</li>
            <li>Pinia for state management</li>
            <li>Vue Router for navigation</li>
            <li>Vite for fast development</li>
          </ul>
        </div>
        <div class="tech-item">
          <h4>Backend</h4>
          <ul>
            <li>Django 4.2 with REST Framework</li>
            <li>Django Channels for WebSockets</li>
            <li>django-notifs for notifications</li>
            <li>uWSGI for production serving</li>
          </ul>
        </div>
        <div class="tech-item">
          <h4>Infrastructure</h4>
          <ul>
            <li>RabbitMQ as message broker</li>
            <li>WebSocket connections</li>
            <li>Real-time communication</li>
            <li>Scalable architecture</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from '../stores/user'

export default {
  name: 'Home',
  setup() {
    const userStore = useUserStore()
    
    return {
      userStore
    }
  }
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.hero-section {
  text-align: center;
  margin-bottom: 4rem;
}

.hero-section h1 {
  font-size: 3rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  font-weight: 700;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.feature {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.feature:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
}

.feature p {
  color: #7f8c8d;
  line-height: 1.6;
}

.cta-buttons {
  margin-top: 2rem;
}

.btn {
  display: inline-block;
  padding: 1rem 2rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  margin: 0 0.5rem;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.btn-secondary {
  background: #ecf0f1;
  color: #2c3e50;
}

.btn-secondary:hover {
  background: #bdc3c7;
  transform: translateY(-2px);
}

.tech-stack {
  margin-top: 4rem;
}

.tech-stack h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
  font-size: 2rem;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.tech-item {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.tech-item h4 {
  color: #2c3e50;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  border-bottom: 2px solid #667eea;
  padding-bottom: 0.5rem;
}

.tech-item ul {
  list-style: none;
  padding: 0;
}

.tech-item li {
  padding: 0.5rem 0;
  color: #7f8c8d;
  border-bottom: 1px solid #ecf0f1;
}

.tech-item li:last-child {
  border-bottom: none;
}

@media (max-width: 768px) {
  .hero-section h1 {
    font-size: 2rem;
  }
  
  .features {
    grid-template-columns: 1fr;
  }
  
  .tech-grid {
    grid-template-columns: 1fr;
  }
}
</style> 