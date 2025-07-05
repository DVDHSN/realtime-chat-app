<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-brand">
        <h1>💬 Realtime Chat</h1>
      </div>
      <div class="nav-menu">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/login" class="nav-link" v-if="!userStore.isAuthenticated">Login</router-link>
        <router-link to="/register" class="nav-link" v-if="!userStore.isAuthenticated">Register</router-link>
        <button @click="logout" class="nav-link logout-btn" v-if="userStore.isAuthenticated">Logout</button>
      </div>
    </nav>

    <main class="main-content">
      <router-view />
    </main>

    <div class="notifications" v-if="notificationStore.notifications.length">
      <div 
        v-for="notification in notificationStore.notifications" 
        :key="notification.id"
        :class="['notification', `notification-${notification.type}`]"
      >
        {{ notification.message }}
        <button @click="notificationStore.removeNotification(notification.id)" class="close-btn">×</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from './stores/user'
import { useNotificationStore } from './stores/notification'

export default {
  name: 'App',
  setup() {
    const userStore = useUserStore()
    const notificationStore = useNotificationStore()

    const logout = async () => {
      await userStore.logout()
    }

    return {
      userStore,
      notificationStore,
      logout
    }
  }
}
</script>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-brand h1 {
  color: white;
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.nav-menu {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: background-color 0.3s;
  font-weight: 500;
}

.nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.logout-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
}

.main-content {
  flex: 1;
  padding: 2rem;
  background-color: #f8f9fa;
}

.notifications {
  position: fixed;
  top: 80px;
  right: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.notification {
  padding: 1rem;
  border-radius: 8px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-width: 300px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.notification-success {
  background-color: #28a745;
}

.notification-error {
  background-color: #dc3545;
}

.notification-info {
  background-color: #17a2b8;
}

.notification-warning {
  background-color: #ffc107;
  color: #212529;
}

.close-btn {
  background: none;
  border: none;
  color: inherit;
  font-size: 1.2rem;
  cursor: pointer;
  padding: 0;
  margin-left: 0.5rem;
}

.close-btn:hover {
  opacity: 0.8;
}
</style> 