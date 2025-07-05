<template>
  <div class="register-container">
    <div class="register-card">
      <h2>Create Account</h2>
      <p class="subtitle">Join our community and start chatting with others</p>
      
      <form @submit.prevent="handleRegister" class="register-form">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="form.username"
            type="text"
            required
            placeholder="Choose a username"
            :class="{ 'error': errors.username }"
          />
          <span class="error-message" v-if="errors.username">{{ errors.username }}</span>
        </div>
        
        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            required
            placeholder="Enter your email"
            :class="{ 'error': errors.email }"
          />
          <span class="error-message" v-if="errors.email">{{ errors.email }}</span>
        </div>
        
        <div class="form-group">
          <label for="first_name">First Name</label>
          <input
            id="first_name"
            v-model="form.first_name"
            type="text"
            required
            placeholder="Enter your first name"
            :class="{ 'error': errors.first_name }"
          />
          <span class="error-message" v-if="errors.first_name">{{ errors.first_name }}</span>
        </div>
        
        <div class="form-group">
          <label for="last_name">Last Name</label>
          <input
            id="last_name"
            v-model="form.last_name"
            type="text"
            required
            placeholder="Enter your last name"
            :class="{ 'error': errors.last_name }"
          />
          <span class="error-message" v-if="errors.last_name">{{ errors.last_name }}</span>
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            required
            placeholder="Create a password"
            :class="{ 'error': errors.password }"
          />
          <span class="error-message" v-if="errors.password">{{ errors.password }}</span>
        </div>
        
        <div class="form-group">
          <label for="confirm_password">Confirm Password</label>
          <input
            id="confirm_password"
            v-model="form.confirm_password"
            type="password"
            required
            placeholder="Confirm your password"
            :class="{ 'error': errors.confirm_password }"
          />
          <span class="error-message" v-if="errors.confirm_password">{{ errors.confirm_password }}</span>
        </div>
        
        <button type="submit" class="btn-register" :disabled="loading">
          <span v-if="loading">Creating account...</span>
          <span v-else>Create Account</span>
        </button>
      </form>
      
      <div class="divider">
        <span>or</span>
      </div>
      
      <router-link to="/login" class="btn-login">
        Already have an account? Sign in
      </router-link>
    </div>
  </div>
</template>

<script>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import { useNotificationStore } from '../stores/notification'

export default {
  name: 'Register',
  setup() {
    const router = useRouter()
    const userStore = useUserStore()
    const notificationStore = useNotificationStore()
    
    const form = reactive({
      username: '',
      email: '',
      first_name: '',
      last_name: '',
      password: '',
      confirm_password: ''
    })
    
    const errors = reactive({})
    const loading = ref(false)
    
    const validateForm = () => {
      errors.username = ''
      errors.email = ''
      errors.first_name = ''
      errors.last_name = ''
      errors.password = ''
      errors.confirm_password = ''
      
      if (!form.username.trim()) {
        errors.username = 'Username is required'
      } else if (form.username.length < 3) {
        errors.username = 'Username must be at least 3 characters'
      }
      
      if (!form.email) {
        errors.email = 'Email is required'
      } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
        errors.email = 'Please enter a valid email'
      }
      
      if (!form.first_name.trim()) {
        errors.first_name = 'First name is required'
      }
      
      if (!form.last_name.trim()) {
        errors.last_name = 'Last name is required'
      }
      
      if (!form.password) {
        errors.password = 'Password is required'
      } else if (form.password.length < 6) {
        errors.password = 'Password must be at least 6 characters'
      }
      
      if (!form.confirm_password) {
        errors.confirm_password = 'Please confirm your password'
      } else if (form.password !== form.confirm_password) {
        errors.confirm_password = 'Passwords do not match'
      }
      
      return !Object.values(errors).some(error => error)
    }
    
    const handleRegister = async () => {
      if (!validateForm()) return
      
      loading.value = true
      
      try {
        const result = await userStore.register({
          username: form.username,
          email: form.email,
          first_name: form.first_name,
          last_name: form.last_name,
          password: form.password
        })
        
        if (result.success) {
          notificationStore.addNotification('Account created successfully!', 'success')
          router.push('/chat')
        } else {
          notificationStore.addNotification(result.error, 'error')
        }
      } catch (error) {
        notificationStore.addNotification('Registration failed. Please try again.', 'error')
      } finally {
        loading.value = false
      }
    }
    
    return {
      form,
      errors,
      loading,
      handleRegister
    }
  }
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.register-card {
  background: white;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
}

.register-card h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 2rem;
  font-weight: 700;
}

.subtitle {
  text-align: center;
  color: #7f8c8d;
  margin-bottom: 2rem;
  font-size: 1rem;
}

.register-form {
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 600;
  font-size: 0.9rem;
}

.form-group input {
  width: 100%;
  padding: 1rem;
  border: 2px solid #ecf0f1;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
}

.form-group input.error {
  border-color: #e74c3c;
}

.error-message {
  color: #e74c3c;
  font-size: 0.8rem;
  margin-top: 0.25rem;
  display: block;
}

.btn-register {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-register:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.btn-register:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.divider {
  text-align: center;
  margin: 2rem 0;
  position: relative;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: #ecf0f1;
}

.divider span {
  background: white;
  padding: 0 1rem;
  color: #7f8c8d;
  font-size: 0.9rem;
}

.btn-login {
  display: block;
  text-align: center;
  padding: 1rem;
  background: #ecf0f1;
  color: #2c3e50;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-login:hover {
  background: #bdc3c7;
  transform: translateY(-2px);
}

@media (max-width: 480px) {
  .register-card {
    padding: 2rem;
  }
  
  .register-card h2 {
    font-size: 1.5rem;
  }
}
</style> 