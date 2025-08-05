import { useToast as usePrimeToast } from 'primevue/usetoast'

export const useToast = () => {
  const toast = usePrimeToast()

  const success = (message: string, summary: string = 'Success') => {
    toast.add({
      severity: 'success',
      summary,
      detail: message,
      life: 5000,
    })
  }

  const error = (message: string, summary: string = 'Error') => {
    toast.add({
      severity: 'error',
      summary,
      detail: message,
      life: 5000,
    })
  }

  const warning = (message: string, summary: string = 'Warning') => {
    toast.add({
      severity: 'warn',
      summary,
      detail: message,
      life: 5000,
    })
  }

  const info = (message: string, summary: string = 'Info') => {
    toast.add({
      severity: 'info',
      summary,
      detail: message,
      life: 5000,
    })
  }

  return {
    success,
    error,
    warning,
    info,
  }
}
