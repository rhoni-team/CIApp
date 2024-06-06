<script setup>
import calculatorIcon from '@/assets/icons/calculatorIcon.vue'
import homeIcon from '@/assets/icons/homeIcon.vue'
import goBackIcon from '@/assets/icons/goBackIcon.vue'
</script>

<template>
  <div class="btm-nav">
    <button class="text-accent focus:active">
      <goBackIcon /> 
    </button>
    <button class="text-accent focus:active">
      <homeIcon />
    </button>
    <button class="text-accent focus:active">
      <calculatorIcon />
    </button>
  </div>
</template>

