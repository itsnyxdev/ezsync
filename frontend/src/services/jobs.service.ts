import { api } from '@/services/api.service.ts'
import type { JobsResponse, JobFilters, Category } from '@/types/jobs.type.ts'

export const jobsService = {
  async getJobs(page: number = 1, filters: JobFilters = {}): Promise<JobsResponse> {
    const params = {
      page,
      limit: 10,
      ...filters,
    }

    const response = await api.get('/jobs', { params })
    return response.data
  },

  async getCategories(): Promise<Category[]> {
    const response = await api.get('/jobs/categories')
    return response.data
  },
}
