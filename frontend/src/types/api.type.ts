export interface ApiError {
  message: string
  code: number
}

export interface PaginationMeta {
  current: number
  totalPages: number
  totalItems: number
}

export interface ApiServiceConfig {
  baseURL: string
  timeout?: number
  publicEndpoints?: string[]
}
