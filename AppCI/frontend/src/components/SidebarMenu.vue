<script setup lang="ts">
import DarkLightButton from '@/components/DarkLightButton.vue';
</script>

<template>
  <label
    for="my-drawer"
    aria-label="close sidebar"
    class="drawer-overlay"
  />
  <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
    <!-- Sidebar content here -->
    <li><a>Sidebar Item 1</a></li>
    <li><a>Sidebar Item 2</a></li>
    <dark-light-button />
  </ul>
</template>
