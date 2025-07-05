import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

// API base URL - will use Render backend
const API_BASE_URL = 'https://realtime-chat-app-to8j.onrender.com'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const isAuthenticated = ref(false)
  const isLoading = ref(false)

  // Computed properties
  const username = computed(() => user.value?.username || '')
  const userId = computed(() => user.value?.id || null)

  // API instance
  const api = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true
  })

  // Login function
  const login = async (credentials) => {
    isLoading.value = true
    try {
      const response = await api.post('/api/users/login/', credentials)
      if (response.data) {
        user.value = response.data
        isAuthenticated.value = true
        return { success: true }
      } else {
        return { success: false, error: 'Login failed' }
      }
    } catch (error) {
      console.error('Login error:', error)
      return { 
        success: false, 
        error: error.response?.data?.error || 'Login failed' 
      }
    } finally {
      isLoading.value = false
    }
  }

  // Register function
  const register = async (userData) => {
    isLoading.value = true
    try {
      const response = await api.post('/api/users/register/', userData)
      if (response.data) {
        user.value = response.data
        isAuthenticated.value = true
        return { success: true }
      } else {
        return { success: false, error: 'Registration failed' }
      }
    } catch (error) {
      console.error('Registration error:', error)
      return { 
        success: false, 
        error: error.response?.data?.error || 'Registration failed' 
      }
    } finally {
      isLoading.value = false
    }
  }

  // Logout function
  const logout = async () => {
    try {
      await api.post('/api/users/logout/')
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      user.value = null
      isAuthenticated.value = false
    }
  }

  // Check authentication status
  const checkAuth = async () => {
    try {
      const response = await api.get('/api/users/me/')
      user.value = response.data
      isAuthenticated.value = true
      return true
    } catch (error) {
      user.value = null
      isAuthenticated.value = false
      return false
    }
  }

  // Get current user
  const getCurrentUser = async () => {
    try {
      const response = await api.get('/api/users/me/')
      user.value = response.data
      isAuthenticated.value = true
      return response.data
    } catch (error) {
      console.error('Error fetching current user:', error)
      throw error
    }
  }

  return {
    user,
    isAuthenticated,
    isLoading,
    username,
    userId,
    login,
    register,
    logout,
    checkAuth,
    getCurrentUser
  }
}) 