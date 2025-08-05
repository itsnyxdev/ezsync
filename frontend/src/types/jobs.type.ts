export interface Job {
  link: string
  title: string
  company: string
  location: {
    city: string
    country: string
  }
  category_id: string
  levels: string[]
  description: string
  modified_at: string
  created_at: string
  job_id: string
}

export interface JobsResponse {
  data: Job[]
  meta: {
    currentPage: number
    totalPages: number
    totalItems: number
  }
}

export interface JobFilters {
  category_id?: string
  level?: string
  search?: string
}

export interface CategoriesResponse {
  id: string
  name: string
  created_at: string
}

export interface Category {
  id: string
  name: string
}

export interface CategoryOptions {
  label: string
  value: string
}
