<template>
  <Card>
    <template #title>
      <div class="flex items-center gap-2">
        <i class="pi pi-filter"></i>
        Filter Jobs
      </div>
    </template>
    <template #content>
      <div class="space-y-6 pt-4">
        <div>
          <label class="block text-sm font-medium text-zinc-200 mb-2">Search</label>
          <InputText
            v-model="filters.search"
            placeholder="Job title, company..."
            class="w-full"
            @input="debouncedApplyFilters"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-zinc-200 mb-2">Category</label>
          <Select
            v-model="filters.category_id"
            :options="categoryOptions"
            option-label="label"
            option-value="value"
            placeholder="All Categories"
            class="w-full"
            @change="applyFilters"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-zinc-200 mb-2">Level</label>
          <Select
            v-model="filters.level"
            :options="levelTypes"
            option-label="label"
            option-value="value"
            placeholder="All Levels"
            class="w-full"
            @change="applyFilters"
          />
        </div>

        <BaseButton severity="secondary" size="small" full-width @click="clearFilters">
          <i class="pi pi-times mr-2"></i>
          Clear Filters
        </BaseButton>
      </div>
    </template>
  </Card>
</template>

<script setup lang="ts">
import { computed, reactive, ref } from 'vue'
import { useJobsStore } from '@/stores/jobs.store.ts'
import type { JobFilters } from '@/types/jobs.type.ts'

import Card from 'primevue/card'
import InputText from 'primevue/inputtext'
import Select from 'primevue/select'
import BaseButton from '@/components/BaseButton.vue'

const jobsStore = useJobsStore()

let debounceTimer: number | null = null
const categoryOptions = computed(() =>
  jobsStore.categories.map((category) => ({
    label: category.name,
    value: category.id,
  })),
)

const levelTypes = ref([
  { label: 'Entry', value: 'entry' },
  { label: 'Mid-Level', value: 'mid' },
  { label: 'Senior', value: 'senior' },
])

const filters = reactive<JobFilters>({
  search: '',
  level: '',
  category_id: '',
})

const applyFilters = () => {
  const filtersParams = Object.fromEntries(
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    Object.entries(filters).filter(([_, value]) => value !== ''),
  )
  jobsStore.applyFilters(filtersParams)
}

const debouncedApplyFilters = () => {
  if (debounceTimer) {
    clearTimeout(debounceTimer)
  }
  debounceTimer = setTimeout(applyFilters, 300)
}

const clearFilters = () => {
  filters.search = ''
  filters.category_id = ''
  filters.level = ''

  jobsStore.resetFilters()
}
</script>
