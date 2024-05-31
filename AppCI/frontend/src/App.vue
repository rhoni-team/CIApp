<script setup>
import 'vite/modulepreload-polyfill';
import BottomNav from './components/BottomNav.vue';
import SidebarMenu from './components/SidebarMenu.vue';
import TopNav from './components/TopNav.vue';
</script>

<template>
  <div class="drawer">
    <input
      id="my-drawer"
      type="checkbox"
      class="drawer-toggle"
    >
    <div class="drawer-content">
      <!-- Page content here -->
      <nav id="top-navbar">
        <top-nav />
      </nav>
      <main>
        <div class="vueapp">
          <RouterView />
        </div>
      </main>
      <nav id="bottom-navbar">
        <bottom-nav />
      </nav>
    </div>
    <div class="drawer-side">
      <sidebar-menu />
    </div>
  </div>
</template>

<style scoped></style>
