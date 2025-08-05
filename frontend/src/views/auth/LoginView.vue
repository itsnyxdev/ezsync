<template>
  <div class="min-h-screen flex items-center justify-center bg-zinc-900 py-12 px-4 sm:px-6 lg:px-8">
    <Card class="max-w-md w-full">
      <template #content>
        <div class="text-center mb-8">
          <h2 class="text-3xl font-extrabold text-zinc-100">Sign in to your account</h2>
          <p class="mt-2 text-sm text-zinc-400">
            Or
            <router-link
              to="/auth/register"
              class="font-medium text-emerald-400 hover:text-emerald-300"
            >
              Register
            </router-link>
          </p>
        </div>

        <form class="space-y-6" @submit.prevent="handleSubmit">
          <BaseInput
            id="username"
            v-model="form.username"
            type="text"
            label="Username"
            placeholder="Enter your username"
            required
            :error="errors.username"
            @blur="validateUsername"
          />

          <BaseInput
            id="password"
            v-model="form.password"
            type="password"
            label="Password"
            placeholder="Enter your password"
            required
            :error="errors.password"
            @blur="validatePassword"
          />

          <BaseButton type="submit" :loading="authStore.loading" full-width> Sign in </BaseButton>
        </form>

        <Message v-if="authStore.error" severity="error" class="mt-4">
          {{ authStore.error }}
        </Message>
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from '@/composables/useToast'
import { useAuthStore } from '@/stores/auth.store.ts'

import Card from 'primevue/card'
import Message from 'primevue/message'
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'

const router = useRouter()
const authStore = useAuthStore()
const { success } = useToast()

const form = reactive({
  username: '',
  password: '',
})

const errors = reactive({
  username: '',
  password: '',
})

const validateUsername = () => {
  if (!form.username.trim()) {
    errors.username = 'Username is required'
  } else if (form.username.trim().length < 4) {
    errors.username = 'Username must be at least 4 characters'
  } else if (form.username.trim().length > 10) {
    errors.username = 'Username must be at maximum of 10 characters'
  } else {
    errors.username = ''
  }
}

const validatePassword = () => {
  if (!form.password) {
    errors.password = 'Password is required'
  } else if (form.password.length < 8) {
    errors.password = 'Password must be at least 8 characters'
  } else {
    errors.password = ''
  }
}

const validateForm = () => {
  validatePassword()
  validatePassword()
  return !errors.username && !errors.password
}

const handleSubmit = async () => {
  if (!validateForm()) return

  try {
    await authStore.login(form)
    success('Welcome back!')
    await router.push('/')
  } catch (error) {
    console.error('Login failed:', error)
  }
}
</script>
