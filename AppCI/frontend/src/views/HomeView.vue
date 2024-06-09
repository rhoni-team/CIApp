<script setup lang="ts">

// services
// import { arrayOfSheets } from '../services/diseaseDatasheetService';

// API
import { getDiseasesListAPI, getDetailedDiseaseAPI } from '../apiConnections/diseasesAPI.js';

// types
import type DiseaseDatasheet from '../types/DiseaseDatasheet';

// components
import DiseaseDatasheetComponent from '../components/DiseaseDatasheetComponent.vue';
import DiseaseSearchInput from '../components/DiseaseSearchInput.vue';

import { ref, onMounted, watch } from 'vue';


const diseaseSelected = ref<string | null>(null);
const diseaseList = ref<any[]>([]);
const detailedDisease = ref<{ [key: string]: DiseaseDetail }>({});


watch(diseaseSelected, async (newValue) => {
  if (newValue) {
    detailedDisease.value = await getDetailedDiseaseAPI(newValue);
    console.log("detailedDisease.value", detailedDisease.value);
  } else {
    detailedDisease.value = null;
  }
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
    <disease-datasheet-component :disease-sheet="detailedDisease" />
  </div>
</template>
