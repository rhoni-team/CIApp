<script setup lang="ts">

// services
import { arrayOfSheets } from '../services/diseaseDatasheetService';

// types
import type DiseaseDatasheet from '../types/DiseaseDatasheet';

// components
import DiseaseDatasheetComponent from '../components/DiseaseDatasheetComponent.vue';
import DiseaseSearchInput from '../components/DiseaseSearchInput.vue';

import { ref, watchEffect } from 'vue';

const diseaseSelectedObject = ref<DiseaseDatasheet | null>(null);
const diseaseSelected = ref<string | null>(null);
const diseaseList = arrayOfSheets.map((disease) => disease.name);

watchEffect(async () => {
  diseaseSelectedObject.value = arrayOfSheets.find((disease) => disease.name === diseaseSelected.value) || null;
});

</script>

<template>
  <div>
    <disease-search-input
      :disease-list="diseaseList"
      @@disease-selected="diseaseSelected = $event"
    />
    <disease-datasheet-component :disease-sheet="diseaseSelectedObject" />
  </div>
</template>

<style scoped></style>