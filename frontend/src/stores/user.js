import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const user = ref(null)
  const isAuthenticated = computed(() => !!user.value)

  const login = async (credentials) => {
    try {
      const response = await axios.post('/api/users/login/', credentials, {
        withCredentials: true
      })
      user.value = response.data
      return { success: true }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.error || 'Login failed' 
      }
    }
  }

  const register = async (userData) => {
    try {
      const response = await axios.post('/api/users/register/', userData, {
        withCredentials: true
      })
      user.value = response.data
      return { success: true }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Registration failed' 
      }
    }
  }

  const logout = async () => {
    try {
      await axios.post('/api/users/logout/', {}, {
        withCredentials: true
      })
    } catch (error) {
      console.error('Logout error:', error)
    } finally {
      user.value = null
    }
  }

  const checkAuth = async () => {
    try {
      const response = await axios.get('/api/users/me/', {
        withCredentials: true
      })
      user.value = response.data
      return true
    } catch (error) {
      user.value = null
      return false
    }
  }

  return {
    user,
    isAuthenticated,
    login,
    register,
    logout,
    checkAuth
  }
}) 