<template>
  <div class="space-y-4">
    <div class="flex items-center justify-between">
      <h2 class="text-xl font-semibold text-muted-color">
        Available Jobs
        <span v-if="jobsStore.totalItems" class="text-sm font-normal text-gray-500">
          ({{ jobsStore.totalItems }} total)
        </span>
      </h2>
    </div>

    <div v-if="jobsStore.loading && jobsStore.jobs.length === 0" class="text-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
      <p class="mt-2 text-gray-500">Loading jobs...</p>
    </div>

    <div v-else-if="jobsStore.jobs.length === 0 && !jobsStore.loading" class="text-center py-12">
      <p class="text-gray-500">No jobs found matching your criteria.</p>
    </div>

    <div v-else class="space-y-4">
      <JobListItem
        v-for="job in jobsStore.jobs"
        :key="job.job_id"
        :job="job"
        @click="openJobModal(job)"
      />

      <div ref="loadMoreTrigger" class="py-4">
        <div v-if="jobsStore.loading" class="text-center">
          <div class="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600 mx-auto"></div>
          <p class="mt-2 text-sm text-gray-500">Loading more jobs...</p>
        </div>
        <div v-else-if="!jobsStore.hasMore" class="text-center">
          <p class="text-sm text-gray-500">You've reached the end of the list</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, inject, onMounted, watch, onUnmounted } from 'vue'
import { useJobsStore } from '@/stores/jobs.store.ts'
import { useInfiniteScroll } from '@/composables/useInfiniteScroll.ts'

import JobListItem from './JobListItem.vue'
import type { Job } from '@/types/jobs.type.ts'

const jobsStore = useJobsStore()
const loadMoreTrigger = ref<HTMLElement>()

const openJobModal = inject<(job: Job) => void>('openJobModal')!

const { observe, unobserve } = useInfiniteScroll(() => {
  if (jobsStore.hasMore && !jobsStore.loading) {
    jobsStore.loadMore()
  }
})

watch(loadMoreTrigger, (newTrigger) => {
  if (newTrigger) {
    observe(newTrigger)
  } else {
    if (loadMoreTrigger.value) {
      unobserve(loadMoreTrigger.value)
    }
  }
})

onMounted(() => {
  if (loadMoreTrigger.value) {
    observe(loadMoreTrigger.value)
  }
})

onUnmounted(() => {
  if (loadMoreTrigger.value) {
    unobserve(loadMoreTrigger.value)
  }
})
</script>
