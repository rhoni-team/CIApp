<script setup lang="ts">
import { ref } from 'vue';

const diseaseSelected = ref<string | null>(null);

defineProps<{
  diseaseList: string[];
}>();

defineEmits<{
  '@disease-selected': [string | null]
}>();
</script>

<template>
  <div class="disease-datasheet-search-wrapper">
    <select
      v-model="diseaseSelected"
      class="select select-secondary w-full max-w-xs"
      @change="() => $emit('@disease-selected', diseaseSelected)"
    >
      <option
        selected
        disabled
      >
        Selecciona una enfermedad...
      </option>
      <option
        v-for="item in diseaseList"
        :key="item.id"
        :value="item.id"
      >
        {{ item.label }}
      </option>
    </select>
  </div>
</template>
