import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import legacy from '@vitejs/plugin-legacy'
import { VitePWA } from 'vite-plugin-pwa'
import tailwindcss from '@tailwindcss/vite'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  build: {
    minify: true,
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    }
  },
  plugins: [
    vue(),
    vueDevTools(),
    VitePWA({
      registerType: 'autoUpdate',
      injectRegister: 'auto',
      manifest: {
        name: 'EZ Sync',
        short_name: 'EZSYNC',
        theme_color: '#1a1a1a',
        background_color: '#42b883',
        display: 'minimal-ui',
        icons: [
          {
            src: 'icons/appicon-16x16.png',
            sizes: '16x16',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-32x32.png',
            sizes: '32x32',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-48x48.png',
            sizes: '48x48',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-64x64.png',
            sizes: '64x64',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-128x128.png',
            sizes: '128x128',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-256x256.png',
            sizes: '256x256',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
          {
            src: 'icons/appicon-1024x1024.png',
            sizes: '1024x1024',
            type: 'image/png',
          },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        runtimeCaching: [
          {
            urlPattern: ({ url }) => url.pathname.startsWith('/api'),
            handler: 'NetworkFirst',
            options: {
              cacheName: 'api-cache',
              expiration: {
                maxEntries: 10,
                maxAgeSeconds: 60 * 60 * 24,
              },
              cacheableResponse: {
                statuses: [0, 200],
              },
            },
          },
          {
            urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'google-fonts-cache',
              expiration: {
                maxEntries: 10,
                maxAgeSeconds: 60 * 60 * 24 * 365,
              },
              cacheableResponse: {
                statuses: [0, 200],
              },
            },
          },
        ],
      },
    }),
    tailwindcss(),
    legacy({
      targets: [
        'defaults', 'not IE 11'
      ],
      modernPolyfills: true,
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
