export interface User {
  id: string
  name: string
  email: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface RegisterCredentials {
  email: string
  username: string
  password: string
}

export interface AuthResponse {
  user: User
  access_token: string
  refresh_token: string
}

export interface RegisterAuthResponse {
  email: string
  username: string
  full_name: string
}

export interface LoginAuthResponse {
  access_token: string
  refresh_token: string
}
