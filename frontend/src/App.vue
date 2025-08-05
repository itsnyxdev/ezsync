<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { RouterView } from 'vue-router'
import SplashScreen from './components/SplashScreen.vue'
import ToastContainer from '@/components/ToastContainer.vue'

const showSplash = ref(true)

onMounted(() => {
  const splashShown = sessionStorage.getItem('splashShown')

  if (splashShown) {
    showSplash.value = false
  } else {
    setTimeout(() => {
      showSplash.value = false
      sessionStorage.setItem('splashShown', 'true')
    }, 2000)
  }
})
</script>

<template>
  <ToastContainer />
  <SplashScreen v-if="showSplash" />
  <RouterView v-else />
</template>

<style scoped></style>
