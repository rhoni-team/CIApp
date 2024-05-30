<script setup>
import 'vite/modulepreload-polyfill';
import BottomNav from './components/BottomNav.vue';
</script>

<template>
  <main>
    <div class="vueapp">
      <RouterView />
    </div>
  </main>
  <nav>
    <bottom-nav />
  </nav>
</template>

<style scoped></style>
