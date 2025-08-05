import { ref, onMounted, onUnmounted } from 'vue'

export const useInfiniteScroll = (callback: () => void, threshold: number = 100) => {
  const target = ref<HTMLElement | null>(null)
  const observer = ref<IntersectionObserver | null>(null)

  const createObserver = () => {
    observer.value = new IntersectionObserver(
      (entries) => {
        const entry = entries[0]
        if (entry.isIntersecting) {
          callback()
        }
      },
      {
        rootMargin: `${threshold}px`,
      },
    )
  }

  const observe = (element: HTMLElement) => {
    if (observer.value && element) {
      observer.value.observe(element)
    }
  }

  const unobserve = (element: HTMLElement) => {
    if (observer.value && element) {
      observer.value.unobserve(element)
    }
  }

  onMounted(() => {
    createObserver()
  })

  onUnmounted(() => {
    if (observer.value) {
      observer.value.disconnect()
    }
  })

  return {
    target,
    observe,
    unobserve,
  }
}
