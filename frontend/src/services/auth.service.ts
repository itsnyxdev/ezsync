import { api } from '@/services/api.service.ts'

import type {
  LoginAuthResponse,
  LoginCredentials,
  RegisterAuthResponse,
  RegisterCredentials,
} from '@/types/auth.type.ts'

export const authService = {
  async login(credentials: LoginCredentials): Promise<LoginAuthResponse> {
    try {
      const params = new URLSearchParams()
      params.append('username', credentials.username)
      params.append('password', credentials.password)

      const response = await api.post('/auth/login', params, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })

      return response.data
    } catch (error: any) {
      if (error.response?.status === 401) {
        throw new Error('Invalid username or password')
      } else if (error.response?.status === 422) {
        throw new Error('Please check your input and try again')
      } else if (error.response?.data?.detail) {
        throw new Error(error.response.data.detail)
      } else {
        throw new Error('Login failed. Please try again.')
      }
    }
  },

  async register(credentials: RegisterCredentials): Promise<RegisterAuthResponse> {
    try {
      const response = await api.post('/auth/register', credentials)

      return response.data
    } catch (error: any) {
      if (error.response?.status === 400) {
        const detail = error.response.data?.detail

        if (detail?.includes('already registered')) {
          throw new Error('Username or email already exists')
        }

        throw new Error(detail || 'Registration failed')
      } else if (error.response?.status === 422) {
        const errors = error.response.data?.detail

        if (Array.isArray(errors)) {
          const errorMessages = errors.map((err: any) => err.msg).join(', ')
          throw new Error(`Validation error: ${errorMessages}`)
        }

        throw new Error('Please check your input and try again')
      } else if (error.response?.data?.detail) {
        throw new Error(error.response.data.detail)
      } else {
        throw new Error('Registration failed. Please try again.')
      }
    }
  },

  async refreshToken(token: string): Promise<{ access_token: string; refresh_token: string }> {
    try {
      const response = await api.post('/auth/refresh', { refresh_token: token })
      return response.data
    } catch (error: any) {
      console.error('Token refresh failed:', error)
      throw new Error('Session expired. Please login again.')
    }
  },

  async logout(): Promise<void> {
    try {
      await api.post('/auth/logout')
    } catch (error) {
      console.warn('Logout request failed:', error)
    }
  },

  isLoginError(error: any): boolean {
    return (
      error.response?.status === 401 ||
      error.message?.includes('Session expired') ||
      error.message?.includes('Invalid username or password')
    )
  },
}
