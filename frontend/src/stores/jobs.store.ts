import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import type { Category, Job, JobFilters } from '@/types/jobs.type.ts'
import { jobsService } from '@/services/jobs.service.ts'

export const useJobsStore = defineStore('jobs', () => {
  const jobs = ref<Job[]>([])
  const categories = ref<Category[]>([])

  const loading = ref(false)
  const error = ref<string | null>(null)
  const currentPage = ref(1)
  const totalPages = ref(0)
  const totalItems = ref(0)
  const filters = ref<JobFilters>({})

  const filteredJobs = computed(() => jobs.value)
  const hasMore = computed(() => currentPage.value < totalPages.value)

  const fetchCategories = async () => {
    try {
      categories.value = await jobsService.getCategories()
    } catch (err: any) {
      error.value = err.message
    }
  }

  const fetchJobs = async (page: number = 1, newFilters: JobFilters = {}) => {
    try {
      error.value = null
      loading.value = true

      const response = await jobsService.getJobs(page, { ...filters.value, ...newFilters })

      if (page === 1) {
        jobs.value = response.data
      } else {
        jobs.value.push(...response.data)
      }

      currentPage.value = response.meta.currentPage
      totalPages.value = response.meta.totalPages
      totalItems.value = response.meta.totalItems

      return response
    } catch (err: any) {
      error.value = err.response?.data?.message || 'Failed to fetch jobs'
      throw err
    } finally {
      loading.value = false
    }
  }

  const loadMore = async () => {
    if (hasMore.value && !loading.value) {
      await fetchJobs(currentPage.value + 1)
    }
  }

  const applyFilters = async (newFilters: JobFilters) => {
    filters.value = { ...newFilters }
    currentPage.value = 1
    await fetchJobs(1, newFilters)
  }

  const resetFilters = async () => {
    filters.value = {}
    currentPage.value = 1
    await fetchJobs(1)
  }

  return {
    jobs,
    categories,
    loading,
    error,
    currentPage,
    totalPages,
    totalItems,
    filters,
    hasMore,
    filteredJobs,
    fetchJobs,
    loadMore,
    applyFilters,
    resetFilters,
    fetchCategories,
  }
})
