<script setup>
import calculatorIcon from '@/assets/icons/calculatorIcon.vue'
import homeIcon from '@/assets/icons/homeIcon.vue'
import goBackIcon from '@/assets/icons/goBackIcon.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <div class="btm-nav">
    <button class="text-accent focus:active">
      <goBackIcon /> 
    </button>
    <button 
      class="text-accent focus:active" 
      @click="router.push({name: 'Home'})"
    >
      <homeIcon />
    </button>
    <button 
      class="text-accent focus:active" 
      @click="router.push({name: 'IsolationCalculator'})"
    >
      <calculatorIcon />
    </button>
  </div>
</template>

