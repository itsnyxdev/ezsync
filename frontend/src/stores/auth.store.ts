import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type { LoginCredentials, RegisterCredentials } from '@/types/auth.type.ts'
import { authService } from '@/services/auth.service.ts'

export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref(localStorage.getItem('accessToken'))
  const loading = ref(false)
  const error = ref<string | null>(null)

  const isAuthenticated = computed(() => !!accessToken.value)

  const setTokens = (newAccessToken: string, refreshToken: string) => {
    accessToken.value = newAccessToken
    localStorage.setItem('accessToken', newAccessToken)
    localStorage.setItem('refreshToken', refreshToken)
  }

  const clearTokens = () => {
    accessToken.value = null
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
  }

  const login = async (credentials: LoginCredentials) => {
    try {
      loading.value = true
      error.value = null

      const response = await authService.login(credentials)

      setTokens(response.access_token, response.refresh_token)

      return response
    } catch (err: any) {
      error.value = err.response?.data?.message || 'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  const register = async (credentials: RegisterCredentials) => {
    try {
      loading.value = true
      error.value = null

      return await authService.register(credentials)
    } catch (err: any) {
      error.value = err.response?.data?.message || 'Registration failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  const logout = async () => {
    try {
      await authService.logout()
    } catch (err) {
      console.error('Logout error:', err)
    } finally {
      clearTokens()
    }
  }

  const initializeAuth = () => {
    const token = localStorage.getItem('accessToken')

    if (token) {
      try {
        accessToken.value = token
      } catch {
        clearTokens()
      }
    }
  }

  return {
    accessToken,
    loading,
    error,
    isAuthenticated,
    login,
    register,
    logout,
    initializeAuth,
  }
})
