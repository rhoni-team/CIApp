<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import DiseaseDatasheet from '@/types/DiseaseDatasheet';

const diseaseSelected = ref<string | null>(null);
const diseaseSelectedObject = ref<DiseaseDatasheet | null>(null);

const props = defineProps<{
  arrayOfSheets: DiseaseDatasheet[];
}>();

defineEmits<{
  '@disease-selected': [disease: DiseaseDatasheet | null]
  // (e: '@disease-selected', disease: DiseaseDatasheet | null ): void;
}>();

watchEffect(async () => {
  diseaseSelectedObject.value = props.arrayOfSheets.find((disease) => disease.name === diseaseSelected.value) || null;
});

</script>

<template>
  <div class="disease-datasheet-search-wrapper">
    <select
      v-model="diseaseSelected"
      class="select select-secondary w-full max-w-xs"
      @change="() => $emit('@disease-selected', diseaseSelectedObject)"
    >
      <option
        selected
        disabled
      >
        Selecciona una enfermedad...
      </option>
      <option
        v-for="(item, key) in arrayOfSheets"
        :key="key"
      >
        {{ item.name }}
      </option>
    </select>
  </div>
</template>
