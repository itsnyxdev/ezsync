import { definePreset } from '@primevue/themes'
import Aura from '@primevue/themes/aura'

export const EzSync = definePreset(Aura, {
  semantic: {
    primary: {
      50: '#ecfdf5',
      100: '#d1fae5',
      200: '#a7f3d0',
      300: '#6ee7b7',
      400: '#34d399',
      500: '#10b981',
      600: '#059669',
      700: '#047857',
      800: '#065f46',
      900: '#064e3b',
      950: '#022c22',
    },
    colorScheme: {
      dark: {
        primary: {
          color: '{emerald.500}',
          inverseColor: '{zinc.950}',
          hoverColor: '{emerald.300}',
          activeColor: '{emerald.200}',
        },
        highlight: {
          background: 'rgba(16, 185, 129, .16)',
          focusBackground: 'rgba(16, 185, 129, .24)',
          color: 'rgba(255,255,255,.87)',
          focusColor: 'rgba(255,255,255,.87)',
        },
        surface: {
          0: '#ffffff',
          50: '{zinc.50}',
          100: '{zinc.100}',
          200: '{zinc.200}',
          300: '{zinc.300}',
          400: '{zinc.400}',
          500: '{zinc.500}',
          600: '{zinc.600}',
          700: '{zinc.700}',
          800: '{zinc.800}',
          900: '{zinc.900}',
          950: '{zinc.950}',
        },
      },
    },
  },
})
