<template>
  <Transition name="splash" appear>
    <div v-if="showSplash" class="splash-screen">
      <div class="content">
        <h1 class="title">EZ Sync</h1>
        <a
          href="https://github.com/itsnyxdev"
          target="_blank"
          rel="noopener noreferrer"
          class="github-link"
          @click="trackGitHubClick"
        >
          <div class="github">
            <i class="logo">
              <svg
                width="11"
                height="22"
                viewBox="0 0 11 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M10.2997 11.641C10.2508 11.5739 10.2043 11.5047 10.1612 11.4336C10.1012 11.3345 9.56031 10.5346 8.52594 9.7805C6.96417 8.64176 5.43832 8.45373 3.30921 6.92866C2.89957 6.63522 2.62306 6.4036 2.35278 6.12877C2.02565 5.79591 1.21054 4.94671 0.805202 3.55514C0.805202 3.55514 0.330114 1.96813 0.857383 0.529457C0.882497 0.460881 0.952895 0.268815 1.04867 0.268555C1.08536 0.268555 1.11555 0.296532 1.13559 0.320735C1.2138 0.41885 1.33312 0.565242 1.48342 0.738049C2.04582 1.38464 3.04479 2.40119 5.41334 3.83335C6.89716 4.73044 7.74232 4.78692 9.39544 5.88531C9.73545 6.11121 10.1677 6.41583 10.5084 6.9634C11.0428 7.82249 11.0055 8.889 10.9953 9.43267C10.9935 9.53104 10.986 9.64061 10.986 9.64061C10.9709 9.92116 10.95 10.1269 10.9431 10.1978C10.9431 10.1978 10.8266 11.3937 10.6822 11.815C10.6681 11.8564 10.6357 11.9463 10.5779 11.9541C10.5457 11.9584 10.5154 11.9373 10.2997 11.6412V11.641Z"
                  fill="url(#paint0_linear_1_9)"
                  fill-opacity="0.8"
                />
                <path
                  d="M10.3866 14.5798C10.3847 14.6782 10.3773 14.7878 10.3773 14.7878C10.3773 14.8566 10.3463 15.2075 10.3344 15.345C10.3019 15.7214 10.2465 16.364 10.0215 16.9622C10.0045 17.0073 9.99157 17.0387 9.97647 17.0681C9.97608 17.069 9.97556 17.0696 9.9753 17.0705C9.9701 17.0808 9.9645 17.0911 9.95838 17.1015C9.95513 17.1072 9.95162 17.1128 9.94811 17.1184C9.63541 16.6419 9.20769 16.0927 8.63032 15.5538C7.78906 14.7685 6.92594 14.2818 6.24603 13.9801C6.24551 13.9781 6.24499 13.9764 6.24447 13.9747C6.20817 13.9607 6.17212 13.9466 6.13634 13.9323C6.03029 13.8869 5.92905 13.8463 5.83393 13.8097C4.40085 13.2127 3.37468 12.5632 2.7005 12.0761C2.20277 11.7163 1.94148 11.4768 1.74408 11.2762C1.41695 10.9433 0.60197 10.0942 0.196499 8.70254C0.196499 8.70254 -0.278589 7.11566 0.248679 5.67686C0.273924 5.60815 0.344191 5.41621 0.439963 5.41595C0.476659 5.41595 0.506979 5.44393 0.526888 5.46814C0.605093 5.56625 0.724418 5.71264 0.874713 5.88545C1.43712 6.53204 2.43609 7.54859 4.80463 8.98075C6.28846 9.87784 7.13362 9.93445 8.78674 11.0327C9.12688 11.2586 9.55903 11.5632 9.8997 12.1108C10.4341 12.9699 10.3969 14.0363 10.3866 14.5801V14.5798Z"
                  fill="url(#paint1_linear_1_9)"
                  fill-opacity="0.8"
                />
                <path
                  d="M9.94809 17.1183C9.74341 17.4472 9.32219 17.5369 9.15199 17.5707C8.41105 17.718 7.23446 17.5119 6.75221 17.4491C5.96469 17.3461 4.32017 17.1342 3.60474 17.9882C3.19276 18.4802 3.20005 19.2098 3.32653 19.6576C3.55464 20.4658 4.41854 21.2344 5.01334 21.5182C5.07333 21.5469 5.214 21.6104 5.20463 21.6573C5.1829 21.7665 4.35673 21.7552 3.81346 21.6226C2.74135 21.3608 1.42435 20.3346 1.27458 18.8229C1.15473 17.6126 1.84622 16.7306 1.96151 16.5884C2.46913 15.9613 3.11676 15.6977 3.72653 15.4494C5.04236 14.9137 6.0468 15.0101 6.24798 14.4235C6.30588 14.2546 6.27777 14.0905 6.24602 13.98C6.92593 14.2818 7.78892 14.7685 8.63031 15.5538C9.20768 16.0926 9.6354 16.642 9.94809 17.1184V17.1183Z"
                  fill="url(#paint2_linear_1_9)"
                  fill-opacity="0.8"
                />
                <defs>
                  <linearGradient
                    id="paint0_linear_1_9"
                    x1="-15.6467"
                    y1="-18.2531"
                    x2="13.951"
                    y2="11.6491"
                    gradientUnits="userSpaceOnUse"
                  >
                    <stop offset="0.5" stop-color="white" stop-opacity="0.15" />
                    <stop offset="0.75" stop-color="white" stop-opacity="0.975" />
                    <stop offset="1" stop-color="white" />
                  </linearGradient>
                  <linearGradient
                    id="paint1_linear_1_9"
                    x1="-16.2554"
                    y1="-13.1318"
                    x2="13.3843"
                    y2="16.771"
                    gradientUnits="userSpaceOnUse"
                  >
                    <stop offset="0.5" stop-color="white" stop-opacity="0.15" />
                    <stop offset="0.75" stop-color="white" stop-opacity="0.975" />
                    <stop offset="1" stop-color="white" />
                  </linearGradient>
                  <linearGradient
                    id="paint2_linear_1_9"
                    x1="8.38637"
                    y1="13.9677"
                    x2="2.79541"
                    y2="23.9705"
                    gradientUnits="userSpaceOnUse"
                  >
                    <stop stop-color="#999999" />
                    <stop offset="0.659849" stop-color="white" />
                  </linearGradient>
                </defs>
              </svg>
            </i>
            <span class="username">@itsnyxdev</span>
          </div>
        </a>
      </div>
    </div>
  </Transition>
  <Teleport to="body">
    <ProgressBar
      v-if="showSplash"
      mode="indeterminate"
      style="height: 2px; width: 100%; background: var(--p-primary-400)"
    />
  </Teleport>
</template>

<script setup lang="ts">
import { ProgressBar } from 'primevue'
import { ref, onMounted, onUnmounted, readonly } from 'vue'

interface Props {
  duration?: number
}

interface Emits {
  (e: 'hidden'): void
  (e: 'github-click'): void
}

const props = withDefaults(defineProps<Props>(), {
  duration: 2000,
})

const emit = defineEmits<Emits>()

const showSplash = ref(true)
let timeoutId: number | null = null

const trackGitHubClick = (): void => {
  emit('github-click')
}

onMounted(() => {
  timeoutId = window.setTimeout(() => {
    showSplash.value = false
    emit('hidden')
  }, props.duration)
})

onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId)
  }
})

defineExpose({
  showSplash: readonly(showSplash),
})
</script>

<style scoped>
.splash-enter-active {
  transition: opacity 0.3s ease-in;
}

.splash-leave-active {
  transition: opacity 0.5s ease-out;
}

.splash-enter-from,
.splash-leave-to {
  opacity: 0;
}

.github-link {
  text-decoration: none;
  outline-offset: 4px;
}

.github-link:focus-visible {
  outline: 2px solid var(--p-primary-500);
  border-radius: 100px;
}

.splash-screen {
  position: fixed;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  text-align: center;
}

.title {
  color: var(--p-primary-500);
  font-size: clamp(2rem, 5vw, 6rem);
  font-weight: 700;
  margin: 0;
  line-height: 1;
  letter-spacing: -0.02em;
}

.github {
  position: fixed;
  bottom: 68px;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  gap: clamp(8px, 1vw, 12px);
  padding: 10px clamp(24px, 3vw, 28px);
  border-radius: 100px;
  transition: all 0.2s linear;
  cursor: pointer;
}

.github:hover {
  padding: 10px clamp(25px, 3.5vw, 40px);
}

.logo {
  display: flex;
  align-items: center;
  opacity: 0.9;
  transition: opacity 0.2s ease;
}

.username {
  color: rgba(255, 255, 255, 0.7);
  font-size: clamp(0.8rem, 1.5vw, 1.2rem);
  font-weight: 500;
  line-height: 1;
  transition: color 0.2s ease;
}

.github:hover .logo {
  opacity: 1;
}

.github:hover .username {
  color: rgba(255, 255, 255, 0.9);
}

@media (max-width: 768px) {
  .title {
    font-size: clamp(1.5rem, 8vw, 3rem);
  }

  .github {
    padding: 10px clamp(24px, 4vw, 32px);
    margin-top: clamp(15px, 4vh, 30px);
  }

  .github .username {
    font-size: clamp(0.6rem, 2vw, 1rem);
  }

  .github:hover {
    padding: 10px clamp(32px, 5vw, 40px);
  }
}

@media (max-width: 480px) {
  .content {
    padding: 0 1rem;
  }

  .github {
    bottom: clamp(32px, 5vh, 56px);
    position: fixed;
  }
}

@media (min-width: 1440px) {
  .github {
    padding: 10px clamp(20px, 3vw, 26px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .splash-enter-active,
  .splash-leave-active,
  .github,
  .logo,
  .username {
    transition: none;
  }
}
</style>
