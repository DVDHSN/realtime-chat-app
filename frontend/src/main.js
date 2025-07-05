import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// Configure axios base URL for production
if (import.meta.env.PROD) {
  axios.defaults.baseURL = 'https://realtime-chat-app-to8j.onrender.com'
} else {
  axios.defaults.baseURL = 'http://localhost:8000'
}

import './style.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app') 