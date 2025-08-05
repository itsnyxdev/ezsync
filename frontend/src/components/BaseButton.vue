<template>
  <Button
    :type="type"
    :disabled="disabled || loading"
    :severity="severity"
    :size="size"
    :loading="loading"
    :class="{ 'w-full': fullWidth }"
    @click="$emit('click', $event)"
  >
    <slot />
  </Button>
</template>

<script setup lang="ts">
import Button from 'primevue/button'

interface Props {
  severity?: 'primary' | 'secondary' | 'success' | 'info' | 'warn' | 'help' | 'danger' | 'contrast'
  size?: 'small' | 'large'
  type?: 'button' | 'submit' | 'reset'
  disabled?: boolean
  loading?: boolean
  fullWidth?: boolean
}

withDefaults(defineProps<Props>(), {
  severity: 'primary',
  type: 'button',
  disabled: false,
  loading: false,
  fullWidth: false,
})

defineEmits<{
  click: [event: MouseEvent]
}>()
</script>
