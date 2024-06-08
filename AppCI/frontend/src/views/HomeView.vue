<script setup lang="ts">

// services
import { arrayOfSheets } from '../services/diseaseDatasheetService';

// types
import type DiseaseDatasheet from '../types/DiseaseDatasheet';

// components
import DiseaseDatasheetComponent from '../components/DiseaseDatasheetComponent.vue';
import DiseaseSearchInput from '../components/DiseaseSearchInput.vue';

import { ref, onMounted, watchEffect } from 'vue';

import { getDiseasesListAPI, getDetailedDiseaseAPI } from '../apiConnections/diseases.js';

const diseaseSelectedObject = ref<DiseaseDatasheet | null>(null);
const diseaseSelected = ref<string | null>(null);
const diseaseList = ref<any[]>([]);

watchEffect(async () => {
  diseaseSelectedObject.value = arrayOfSheets.find((disease) => disease.name === diseaseSelected.value) || null;
});

const getDiseaseList = async (): Promise<any[]> => {
  const response = await getDiseasesListAPI();
  return response
}

onMounted(async () => {
  diseaseList.value = await getDiseaseList();
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
