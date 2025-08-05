<template>
  <div class="min-h-screen flex items-center justify-center bg-zinc-900 py-12 px-4 sm:px-6 lg:px-8">
    <Card class="max-w-md w-full">
      <template #content>
        <div class="text-center mb-8">
          <h2 class="text-3xl font-extrabold text-zinc-100">Create your account</h2>
          <p class="mt-2 text-sm text-zinc-400">
            Or
            <router-link
              to="/auth/login"
              class="font-medium text-emerald-400 hover:text-emerald-300"
            >
              sign in to your existing account
            </router-link>
          </p>
        </div>

        <form class="space-y-6" @submit.prevent="handleSubmit">
          <BaseInput
            id="name"
            v-model="form.name"
            type="text"
            label="Full Name"
            placeholder="Enter your full name"
            :error="errors.name"
            @blur="validateName"
          />

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
            id="email"
            v-model="form.email"
            type="email"
            label="Email address"
            placeholder="Enter your email"
            required
            :error="errors.email"
            @blur="validateEmail"
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

          <BaseButton type="submit" :loading="authStore.loading" full-width>
            Create Account
          </BaseButton>
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
  name: '',
  email: '',
  username: '',
  password: '',
})

const errors = reactive({
  name: '',
  email: '',
  username: '',
  password: '',
})

const validateName = () => {
  if (form.name.trim().length < 2) {
    errors.name = 'Name must be at least 2 characters'
  } else {
    errors.name = ''
  }
}

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

const validateEmail = () => {
  if (!form.email) {
    errors.email = 'Email is required'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
    errors.email = 'Please enter a valid email address'
  } else {
    errors.email = ''
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
  validateName()
  validateEmail()
  validateUsername()
  validatePassword()
  return !errors.name && !errors.email && !errors.username && !errors.password
}

const handleSubmit = async () => {
  if (!validateForm()) return

  try {
    await authStore.register({
      email: form.email,
      username: form.username,
      password: form.password,
    })

    success('Account created successfully!')
    await router.push('/auth/login')
  } catch (error) {
    console.error('Registration failed:', error)
  }
}
</script>
