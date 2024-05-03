import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'url'

// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      // This is a workaround for the following error:
      // "Uncaught TypeError: Cannot read properties of undefined (reading 'install')"
      "@": fileURLToPath(new URL('./src', import.meta.url)),
    },
  }, 
  plugins: [vue()],
})
