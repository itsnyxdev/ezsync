<template>
  <BaseModal v-model="isOpen" :title="job?.title">
    <div v-if="job" class="space-y-4">
      <div class="flex items-center space-x-2">
        <Tag
          v-for="(item, index) in job.levels"
          :key="randomKey(item, index)"
          severity="success"
          :value="item.charAt(0).toUpperCase() + item.slice(1)"
        />
        <Tag severity="contrast" :value="categoryName" />
      </div>

      <div class="pt-4">
        <div class="grid grid-cols-2 gap-4 mb-4">
          <div class="flex flex-col gap-2">
            <h4 class="text-sm font-medium">Company</h4>
            <p class="text-xs text-muted-color-emphasis">{{ job.company }}</p>
          </div>
          <div class="flex flex-col gap-2">
            <h4 class="text-sm font-medium">Location</h4>
            <p class="text-xs text-muted-color-emphasis">{{ location }}</p>
          </div>
        </div>

        <div class="mt-8 mb-4">
          <h4 class="text-sm font-medium mb-2">Job Description</h4>
          <div class="prose prose-sm max-w-none">
            <p class="text-sm text-gray-600 whitespace-pre-line">{{ job.description }}</p>
          </div>
        </div>

        <div class="text-xs">Posted {{ formatDate(job.modified_at) }}</div>
      </div>
    </div>

    <template #footer>
      <Button label="Close" severity="secondary" @click="closeModal" />
      <Button
        as="a"
        label="Open on LinkedIn"
        :href="job?.link"
        target="_blank"
        severity="primary"
        @click="closeModal"
      />
    </template>
  </BaseModal>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { Job } from '@/types/jobs.type.ts'

import { Tag, Button } from 'primevue'
import BaseModal from '@/components/BaseModal.vue'
import { useJobsStore } from '@/stores/jobs.store.ts'

interface Props {
  modelValue: boolean
  job: Job | null
}

const props = defineProps<Props>()

const emit = defineEmits<{
  'update:modelValue': [value: boolean]
}>()

const jobsStore = useJobsStore()

const isOpen = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const closeModal = () => {
  isOpen.value = false
}

const categoryName = computed(() => {
  const filtered = jobsStore.categories.filter((category) => category.id == props.job?.category_id)
  return filtered[0].name
})

const location = computed(() => {
  return props.job?.location.city
})

const randomKey = (item: string, index: number) => {
  return `${index + item}`
}

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
