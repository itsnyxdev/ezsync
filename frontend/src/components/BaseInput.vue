<template>
  <div class="mb-4">
    <label v-if="label" :for="id" class="block text-sm font-medium text-zinc-200 mb-2">
      {{ label }}
      <span v-if="required" class="text-red-400">*</span>
    </label>
    <InputText
      :id="id"
      :type="type"
      :modelValue="modelValue"
      :placeholder="placeholder"
      :required="required"
      :disabled="disabled"
      :invalid="!!error"
      class="w-full"
      @input="handleInput"
      @blur="handleBlur"
    />
    <small v-if="error" class="text-red-400">{{ error }}</small>
  </div>
</template>

<script setup lang="ts">
import InputText from 'primevue/inputtext'

interface Props {
  id?: string
  type?: string
  label?: string
  placeholder?: string
  modelValue?: string
  required?: boolean
  disabled?: boolean
  error?: string
}

withDefaults(defineProps<Props>(), {
  type: 'text',
  required: false,
  disabled: false,
})

const emit = defineEmits<{
  'update:modelValue': [value: string]
  blur: [event: FocusEvent]
}>()

const handleInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  emit('update:modelValue', target.value)
}

const handleBlur = (event: FocusEvent) => {
  emit('blur', event)
}
</script>
