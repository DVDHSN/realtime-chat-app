import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

// API base URL - will use Render backend
const API_BASE_URL = 'https://realtime-chat-app-to8j.onrender.com'
const WS_BASE_URL = 'wss://realtime-chat-app-to8j.onrender.com'

export const useChatStore = defineStore('chat', () => {
  const messages = ref([])
  const rooms = ref([])
  const currentRoom = ref(null)
  const ws = ref(null)
  const isConnected = ref(false)

  // Computed properties
  const currentMessages = computed(() => {
    if (!currentRoom.value) return []
    return messages.value.filter(msg => msg.room === currentRoom.value.id)
  })

  // API functions
  const api = axios.create({
    baseURL: API_BASE_URL,
    withCredentials: true
  })

  // WebSocket connection
  const connectWebSocket = (roomId) => {
    if (ws.value) {
      ws.value.close()
    }

    const wsUrl = `${WS_BASE_URL}/ws/chat/${roomId}/`
    ws.value = new WebSocket(wsUrl)

    ws.value.onopen = () => {
      console.log('WebSocket connected')
      isConnected.value = true
    }

    ws.value.onmessage = (event) => {
      const data = JSON.parse(event.data)
      if (data.type === 'chat_message') {
        messages.value.push(data.message)
      }
    }

    ws.value.onclose = () => {
      console.log('WebSocket disconnected')
      isConnected.value = false
    }

    ws.value.onerror = (error) => {
      console.error('WebSocket error:', error)
      isConnected.value = false
    }
  }

  // Send message
  const sendMessage = async (content, roomId) => {
    try {
      const response = await api.post('/api/messages/', {
        content,
        room: roomId
      })
      
      if (ws.value && ws.value.readyState === WebSocket.OPEN) {
        ws.value.send(JSON.stringify({
          type: 'chat_message',
          message: response.data
        }))
      }
      
      return response.data
    } catch (error) {
      console.error('Error sending message:', error)
      throw error
    }
  }

  // Get messages for a room
  const getMessages = async (roomId) => {
    try {
      const response = await api.get(`/api/chatrooms/${roomId}/messages/`)
      messages.value = response.data
      return response.data
    } catch (error) {
      console.error('Error fetching messages:', error)
      throw error
    }
  }

  // Get all rooms
  const getRooms = async () => {
    try {
      const response = await api.get('/api/chatrooms/')
      rooms.value = response.data
      return response.data
    } catch (error) {
      console.error('Error fetching rooms:', error)
      throw error
    }
  }

  // Create a new room
  const createRoom = async (name, description = '') => {
    try {
      const response = await api.post('/api/chatrooms/', {
        name,
        description
      })
      rooms.value.push(response.data)
      return response.data
    } catch (error) {
      console.error('Error creating room:', error)
      throw error
    }
  }

  // Join a room
  const joinRoom = (room) => {
    currentRoom.value = room
    connectWebSocket(room.id)
    getMessages(room.id)
  }

  // Disconnect WebSocket
  const disconnect = () => {
    if (ws.value) {
      ws.value.close()
      ws.value = null
    }
    isConnected.value = false
  }

  return {
    messages,
    rooms,
    currentRoom,
    isConnected,
    currentMessages,
    sendMessage,
    getMessages,
    getRooms,
    createRoom,
    joinRoom,
    connectWebSocket,
    disconnect
  }
}) 