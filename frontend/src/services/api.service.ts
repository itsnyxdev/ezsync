import { useAuthStore } from '@/stores/auth.store.ts'
import type { ApiServiceConfig } from '@/types/api.type.ts'

import axios, {
  type AxiosInstance,
  type AxiosResponse,
  type InternalAxiosRequestConfig,
} from 'axios'

class ApiService {
  private readonly api: AxiosInstance
  private isRefreshing = false
  private publicEndpoints: string[]
  private failedQueue: Array<{
    resolve: (value?: any) => void
    reject: (error?: any) => void
  }> = []

  constructor(config: ApiServiceConfig) {
    this.publicEndpoints = config.publicEndpoints || [
      '/auth/login',
      '/auth/register',
      '/auth/refresh',
    ]

    this.api = axios.create({
      baseURL: config.baseURL,
      timeout: config.timeout || 10000,
    })

    this.setupInterceptors()
  }

  private isPublicEndpoint(url: string): boolean {
    return this.publicEndpoints.some((endpoint) => url.includes(endpoint))
  }

  private processQueue(error: any, token: string | null = null) {
    this.failedQueue.forEach(({ resolve, reject }) => {
      if (error) {
        reject(error)
      } else {
        resolve(token)
      }
    })

    this.failedQueue = []
  }

  private setupInterceptors() {
    this.api.interceptors.request.use(
      (config: InternalAxiosRequestConfig) => {
        if (config.url && !this.isPublicEndpoint(config.url)) {
          const token = localStorage.getItem('accessToken')
          if (token) {
            config.headers.Authorization = `Bearer ${token}`
          }
        }

        return config
      },
      (error) => Promise.reject(error),
    )

    this.api.interceptors.response.use(
      (response: AxiosResponse) => response,
      async (error) => {
        const originalRequest = error.config
        const isPublic = originalRequest.url && this.isPublicEndpoint(originalRequest.url)

        if (error.response?.status === 401 && !originalRequest._retry && !isPublic) {
          if (this.isRefreshing) {
            return new Promise((resolve, reject) => {
              this.failedQueue.push({ resolve, reject })
            })
              .then((token) => {
                originalRequest.headers.Authorization = `Bearer ${token}`
                return this.api(originalRequest)
              })
              .catch((err) => {
                return Promise.reject(err)
              })
          }

          originalRequest._retry = true
          this.isRefreshing = true

          try {
            const refreshToken = localStorage.getItem('refreshToken')
            if (!refreshToken) {
              throw new Error('No refresh token available')
            }

            const refreshResponse = await axios.post(
              `${this.api.defaults.baseURL}/auth/refresh`,
              { refresh_token: refreshToken },
              {
                headers: {
                  'Content-Type': 'application/json',
                },
              },
            )

            const { access_token, refresh_token: newRefreshToken } = refreshResponse.data

            localStorage.setItem('accessToken', access_token)
            if (newRefreshToken) {
              localStorage.setItem('refreshToken', newRefreshToken)
            }

            originalRequest.headers.Authorization = `Bearer ${access_token}`

            this.processQueue(null, access_token)
            return this.api(originalRequest)
          } catch (refreshError) {
            this.processQueue(refreshError, null)

            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')

            try {
              const authStore = useAuthStore()
              await authStore.logout()
            } catch {
              if (typeof window !== 'undefined' && window.location.pathname !== '/login') {
                window.location.href = '/login'
              }
            }

            return Promise.reject(refreshError)
          } finally {
            this.isRefreshing = false
          }
        }

        if (error.response?.status === 401 && isPublic) {
          return Promise.reject(error)
        }

        return Promise.reject(error)
      },
    )
  }

  addPublicEndpoints(endpoints: string[]) {
    this.publicEndpoints.push(...endpoints)
  }

  removePublicEndpoints(endpoints: string[]) {
    this.publicEndpoints = this.publicEndpoints.filter((endpoint) => !endpoints.includes(endpoint))
  }

  getPublicEndpoints(): string[] {
    return [...this.publicEndpoints]
  }

  getInstance(): AxiosInstance {
    return this.api
  }
}

export const apiService = new ApiService({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 10000,
  publicEndpoints: ['/auth/login', '/auth/register', '/auth/refresh'],
})

export const api = apiService.getInstance()
export { apiService as apiServiceInstance }
