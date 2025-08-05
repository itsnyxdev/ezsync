<template>
  <div>
    <header class="w-full m-auto pt-6 pl-6 pr-6">
      <Toolbar
        class="fixed top-0 left-0 right-0 bg-white shadow-lg z-50 px-[100px] py-4"
        style="border-radius: 3rem"
      >
        <template #start>
          <div class="flex items-center gap-2">
            <Button label="Home" text plain />
          </div>
        </template>

        <template #end>
          <div class="flex items-center gap-2">
            <Button
              rounded
              icon="pi pi-sign-out"
              label="Logout"
              severity="primary"
              size="small"
              @click="logout"
            />
          </div>
        </template>
      </Toolbar>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
        <aside class="lg:col-span-1">
          <JobSearchFilter />
        </aside>

        <div class="lg:col-span-3">
          <JobList />
        </div>
      </div>
    </main>

    <JobDetailModal v-model="showJobModal" :job="selectedJob" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store.ts'
import { useJobsStore } from '@/stores/jobs.store.ts'
import { useToast } from '@/composables/useToast.ts'
import type { Job } from '@/types/jobs.type.ts'

import JobSearchFilter from '@/components/job/JobSearchFilter.vue'
import JobList from '@/components/job/JobList.vue'
import JobDetailModal from '@/components/job/JobDetailModal.vue'
import { Toolbar, Button } from 'primevue'

const router = useRouter()
const authStore = useAuthStore()
const jobsStore = useJobsStore()
const { success } = useToast()

const showJobModal = ref(false)
const selectedJob = ref<Job | null>(null)

const openJobModal = (job: Job) => {
  selectedJob.value = job
  showJobModal.value = true
}

provide('openJobModal', openJobModal)

const logout = async () => {
  await authStore.logout()
  success('You have been signed out')
  await router.push('/auth/login')
}

onMounted(async () => {
  await jobsStore.fetchCategories()
  await jobsStore.fetchJobs()
})
</script>
