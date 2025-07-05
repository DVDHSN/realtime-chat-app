<template>
  <div class="chat-container">
    <div class="chat-sidebar">
      <div class="sidebar-header">
        <h3>Chat Rooms</h3>
        <button @click="showCreateRoom = true" class="btn-create-room">
          <span>+</span>
        </button>
      </div>
      
      <div class="rooms-list">
        <div
          v-for="room in chatStore.rooms"
          :key="room.id"
          @click="selectRoom(room)"
          :class="['room-item', { active: currentRoom?.id === room.id }]"
        >
          <div class="room-info">
            <h4>{{ room.name }}</h4>
            <p>{{ room.description || 'No description' }}</p>
          </div>
        </div>
      </div>
      
      <div class="user-info">
        <div class="user-avatar">
          {{ userStore.user?.username?.charAt(0).toUpperCase() }}
        </div>
        <div class="user-details">
          <h4>{{ userStore.user?.username }}</h4>
          <p>{{ userStore.user?.email }}</p>
        </div>
      </div>
    </div>
    
    <div class="chat-main">
      <div v-if="!currentRoom" class="no-room-selected">
        <div class="no-room-content">
          <h2>Welcome to Chat!</h2>
          <p>Select a room from the sidebar to start chatting</p>
          <div class="connection-status">
            <span :class="['status-dot', { connected: chatStore.isConnected }]"></span>
            {{ chatStore.isConnected ? 'Connected' : 'Disconnected' }}
          </div>
        </div>
      </div>
      
      <div v-else class="chat-room">
        <div class="room-header">
          <h2>{{ currentRoom.name }}</h2>
          <div class="room-status">
            <span :class="['status-dot', { connected: chatStore.isConnected }]"></span>
            {{ chatStore.isConnected ? 'Connected' : 'Disconnected' }}
          </div>
        </div>
        
        <div class="messages-container" ref="messagesContainer">
          <div
            v-for="message in chatStore.messages"
            :key="message.id"
            :class="['message', { 'own-message': message.user?.id === userStore.user?.id }]"
          >
            <div class="message-header">
              <span class="username">{{ message.user?.username }}</span>
              <span class="timestamp">{{ formatTime(message.timestamp) }}</span>
            </div>
            <div class="message-content">
              {{ message.content }}
            </div>
          </div>
        </div>
        
        <div class="message-input">
          <form @submit.prevent="sendMessage">
            <div class="input-group">
              <input
                v-model="newMessage"
                type="text"
                placeholder="Type your message..."
                :disabled="!chatStore.isConnected"
                class="message-input-field"
              />
              <button type="submit" :disabled="!newMessage.trim() || !chatStore.isConnected" class="send-btn">
                <span>Send</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    
    <!-- Create Room Modal -->
    <div v-if="showCreateRoom" class="modal-overlay" @click="showCreateRoom = false">
      <div class="modal" @click.stop>
        <h3>Create New Room</h3>
        <form @submit.prevent="createRoom">
          <div class="form-group">
            <label for="room-name">Room Name</label>
            <input
              id="room-name"
              v-model="newRoom.name"
              type="text"
              required
              placeholder="Enter room name"
            />
          </div>
          <div class="form-group">
            <label for="room-description">Description</label>
            <textarea
              id="room-description"
              v-model="newRoom.description"
              placeholder="Enter room description"
              rows="3"
            ></textarea>
          </div>
          <div class="modal-actions">
            <button type="button" @click="showCreateRoom = false" class="btn-cancel">
              Cancel
            </button>
            <button type="submit" class="btn-create">
              Create Room
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, nextTick, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import { useChatStore } from '../stores/chat'
import { useNotificationStore } from '../stores/notification'

export default {
  name: 'Chat',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const userStore = useUserStore()
    const chatStore = useChatStore()
    const notificationStore = useNotificationStore()
    
    const messagesContainer = ref(null)
    const newMessage = ref('')
    const showCreateRoom = ref(false)
    const newRoom = ref({
      name: '',
      description: ''
    })
    
    const currentRoom = computed(() => chatStore.currentRoom)
    
    onMounted(async () => {
      // Check authentication first
      const isAuth = await userStore.checkAuth()
      if (!isAuth) {
        router.push('/login')
        return
      }
      
      await chatStore.fetchRooms()
      
      // Set initial room from route or default to first room
      if (route.params.roomName) {
        const room = chatStore.rooms.find(r => r.name === route.params.roomName)
        if (room) {
          chatStore.setCurrentRoom(room)
        }
      } else if (chatStore.rooms.length > 0) {
        chatStore.setCurrentRoom(chatStore.rooms[0])
      }
    })
    
    const selectRoom = (room) => {
      chatStore.setCurrentRoom(room)
      router.push(`/chat/${room.name}`)
    }
    
    const sendMessage = async () => {
      if (!newMessage.value.trim()) return
      
      const result = await chatStore.sendMessage(newMessage.value)
      if (result.success) {
        newMessage.value = ''
        await nextTick()
        scrollToBottom()
      } else {
        notificationStore.addNotification(result.error, 'error')
      }
    }
    
    const createRoom = async () => {
      const result = await chatStore.createRoom(newRoom.value)
      if (result.success) {
        showCreateRoom.value = false
        newRoom.value = { name: '', description: '' }
        notificationStore.addNotification('Room created successfully!', 'success')
        selectRoom(result.room)
      } else {
        notificationStore.addNotification(result.error, 'error')
      }
    }
    
    const scrollToBottom = () => {
      if (messagesContainer.value) {
        messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
      }
    }
    
    const formatTime = (timestamp) => {
      return new Date(timestamp).toLocaleTimeString([], { 
        hour: '2-digit', 
        minute: '2-digit' 
      })
    }
    
    // Auto-scroll to bottom when new messages arrive
    watch(() => chatStore.messages.length, () => {
      nextTick(() => scrollToBottom())
    })
    
    return {
      messagesContainer,
      newMessage,
      showCreateRoom,
      newRoom,
      currentRoom,
      chatStore,
      userStore,
      selectRoom,
      sendMessage,
      createRoom,
      formatTime
    }
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  height: calc(100vh - 80px);
  background: #f8f9fa;
}

.chat-sidebar {
  width: 300px;
  background: white;
  border-right: 1px solid #e9ecef;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sidebar-header h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.btn-create-room {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s ease;
}

.btn-create-room:hover {
  transform: scale(1.1);
}

.rooms-list {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.room-item {
  padding: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  margin-bottom: 0.5rem;
}

.room-item:hover {
  background: #f8f9fa;
}

.room-item.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.room-info h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1rem;
}

.room-info p {
  margin: 0;
  font-size: 0.8rem;
  opacity: 0.8;
}

.user-info {
  padding: 1rem;
  border-top: 1px solid #e9ecef;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.1rem;
}

.user-details h4 {
  margin: 0;
  font-size: 0.9rem;
  color: #2c3e50;
}

.user-details p {
  margin: 0;
  font-size: 0.8rem;
  color: #7f8c8d;
}

.chat-main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.no-room-selected {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  margin: 1rem;
  border-radius: 12px;
}

.no-room-content {
  text-align: center;
  color: #7f8c8d;
}

.no-room-content h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.connection-status {
  margin-top: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #e74c3c;
}

.status-dot.connected {
  background: #27ae60;
}

.chat-room {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: white;
  margin: 1rem;
  border-radius: 12px;
  overflow: hidden;
}

.room-header {
  padding: 1.5rem;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.room-header h2 {
  margin: 0;
  color: #2c3e50;
}

.room-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: #7f8c8d;
}

.messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message {
  max-width: 70%;
  padding: 1rem;
  border-radius: 12px;
  background: #f8f9fa;
  align-self: flex-start;
}

.message.own-message {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  align-self: flex-end;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
  font-size: 0.8rem;
}

.username {
  font-weight: 600;
}

.timestamp {
  opacity: 0.7;
}

.message-content {
  line-height: 1.4;
  word-wrap: break-word;
}

.message-input {
  padding: 1rem;
  border-top: 1px solid #e9ecef;
}

.input-group {
  display: flex;
  gap: 0.5rem;
}

.message-input-field {
  flex: 1;
  padding: 1rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.message-input-field:focus {
  outline: none;
  border-color: #667eea;
}

.message-input-field:disabled {
  background: #f8f9fa;
  cursor: not-allowed;
}

.send-btn {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.send-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
}

.modal h3 {
  margin: 0 0 1.5rem 0;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 600;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #667eea;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.btn-cancel,
.btn-create {
  flex: 1;
  padding: 0.75rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-cancel {
  background: #ecf0f1;
  color: #2c3e50;
  border: none;
}

.btn-cancel:hover {
  background: #bdc3c7;
}

.btn-create {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
}

.btn-create:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

@media (max-width: 768px) {
  .chat-container {
    flex-direction: column;
  }
  
  .chat-sidebar {
    width: 100%;
    height: 200px;
  }
  
  .chat-main {
    height: calc(100vh - 280px);
  }
}
</style> 