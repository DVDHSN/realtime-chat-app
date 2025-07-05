import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

export const useChatStore = defineStore('chat', () => {
  const rooms = ref([])
  const currentRoom = ref(null)
  const messages = ref([])
  const onlineUsers = ref([])
  const websocket = ref(null)
  const isConnected = ref(false)

  const currentRoomName = computed(() => currentRoom.value?.name || 'general')

  const fetchRooms = async () => {
    try {
      const response = await axios.get('/api/rooms/', {
        withCredentials: true
      })
      rooms.value = response.data
      return { success: true }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Failed to fetch rooms' 
      }
    }
  }

  const createRoom = async (roomData) => {
    try {
      const response = await axios.post('/api/rooms/', roomData, {
        withCredentials: true
      })
      rooms.value.push(response.data)
      return { success: true, room: response.data }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Failed to create room' 
      }
    }
  }

  const fetchMessages = async (roomName) => {
    try {
      const response = await axios.get(`/api/rooms/${roomName}/messages/`, {
        withCredentials: true
      })
      messages.value = response.data
      return { success: true }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Failed to fetch messages' 
      }
    }
  }

  const sendMessage = async (content) => {
    if (!currentRoom.value) return { success: false, error: 'No room selected' }
    
    try {
      const response = await axios.post('/api/messages/', {
        room: currentRoom.value.id,
        content
      }, {
        withCredentials: true
      })
      messages.value.push(response.data)
      return { success: true }
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Failed to send message' 
      }
    }
  }

  const connectWebSocket = (roomName) => {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
    const wsUrl = `${protocol}//${window.location.host}/ws/chat/${roomName}/`
    
    websocket.value = new WebSocket(wsUrl)
    
    websocket.value.onopen = () => {
      isConnected.value = true
      console.log('WebSocket connected')
    }
    
    websocket.value.onmessage = (event) => {
      const data = JSON.parse(event.data)
      if (data.message) {
        messages.value.push({
          id: Date.now(),
          content: data.message,
          user: { username: data.username, id: data.user_id },
          timestamp: new Date().toISOString()
        })
      }
    }
    
    websocket.value.onclose = () => {
      isConnected.value = false
      console.log('WebSocket disconnected')
    }
    
    websocket.value.onerror = (error) => {
      console.error('WebSocket error:', error)
      isConnected.value = false
    }
  }

  const disconnectWebSocket = () => {
    if (websocket.value) {
      websocket.value.close()
      websocket.value = null
    }
    isConnected.value = false
  }

  const setCurrentRoom = (room) => {
    disconnectWebSocket()
    currentRoom.value = room
    if (room) {
      connectWebSocket(room.name)
      fetchMessages(room.name)
    }
  }

  return {
    rooms,
    currentRoom,
    messages,
    onlineUsers,
    isConnected,
    currentRoomName,
    fetchRooms,
    createRoom,
    fetchMessages,
    sendMessage,
    connectWebSocket,
    disconnectWebSocket,
    setCurrentRoom
  }
}) 