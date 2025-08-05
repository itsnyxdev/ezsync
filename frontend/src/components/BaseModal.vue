<template>
  <Dialog
    v-model:visible="isVisible"
    :header="title"
    :modal="true"
    :draggable="false"
    :closable="true"
    @hide="closeModal"
    pt:mask:class="backdrop-blur-sm"
    maximizable
    :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
    :style="{ width: '50rem' }"
  >
    <div class="mb-6">
      <slot />
    </div>

    <template v-if="$slots.footer" #footer>
      <div class="flex justify-end gap-3">
        <slot name="footer" />
      </div>
    </template>
  </Dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import Dialog from 'primevue/dialog'

interface Props {
  modelValue: boolean
  title?: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
  'update:modelValue': [value: boolean]
}>()

const isVisible = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const closeModal = () => {
  emit('update:modelValue', false)
}
</script>
