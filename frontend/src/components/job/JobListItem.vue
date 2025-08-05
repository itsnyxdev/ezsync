<template>
  <Card
    class="rounded-lg shadow hover:shadow-md transition-shadow duration-200 p-4 cursor-pointer"
    @click="$emit('click')"
  >
    <template #content>
      <div class="flex items-start justify-between">
        <div class="flex-1">
          <div class="flex items-center space-x-2 mb-2">
            <h3 class="text-lg font-medium text-primary">{{ job.title }}</h3>
          </div>

          <div class="flex items-center space-x-4 text-sm">
            <span class="inline-flex items-center">
              <Tag
                class="font-light"
                icon="pi pi-sparkles"
                severity="secondary"
                :value="categoryName(job.category_id)"
              />
            </span>
            <span class="inline-flex items-center">
              <Tag class="font-light" icon="pi pi-gauge" severity="secondary" :value="levels" />
            </span>
          </div>
        </div>
      </div>
    </template>

    <template #footer>
      <div class="flex mt-4">
        <p class="text-sm text-muted-color-emphasis">{{ formatDate(job.modified_at) }}</p>
      </div>
    </template>
  </Card>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useJobsStore } from '@/stores/jobs.store.ts'
import type { Job } from '@/types/jobs.type.ts'

import { Card, Tag } from 'primevue'

interface Props {
  job: Job
}

const props = defineProps<Props>()

defineEmits<{
  click: []
}>()

const jobsStore = useJobsStore()

const categoryName = (categoryId: string) => {
  const filtered = jobsStore.categories.filter((category) => category.id == categoryId)
  return filtered[0].name
}

const levels = computed(() => {
  const levelsArray = props.job.levels.map((str) => str.charAt(0).toUpperCase() + str.slice(1))
  return levelsArray.join(', ')
})

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  const now = new Date()
  const diffTime = Math.abs(now.getTime() - date.getTime())
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

  if (diffDays === 1) return '1 day ago'
  if (diffDays < 7) return `${diffDays} days ago`
  if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
  return `${Math.ceil(diffDays / 30)} months ago`
}
</script>
