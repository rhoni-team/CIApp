<script setup>
import sunIcon from '@/assets/icons/sunIcon.vue';
import moonIcon from '@/assets/icons/moonIcon.vue';
</script>

<template>
  <div>
    <label class="swap swap-rotate">
      <!-- this hidden checkbox controls the state -->
      <input
        type="checkbox"
        class="theme-controller"
        value="light"
      >
      <sun-icon />
      <moon-icon />
    </label>
  </div>
</template>