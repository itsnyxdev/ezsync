import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from '@/App.vue'
import router from '@/router'
import PrimeVue from 'primevue/config'
import { ToastService } from 'primevue'
import { EzSync } from '@/theme.ts'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

app.use(PrimeVue, {
  theme: {
    preset: EzSync,
    options: {
      cssLayer: false,
      darkModeSelector: '.dark',
    },
  },
})

app.use(ToastService)
app.mount('#app')
