<script setup lang="ts">

// services
import { arrayOfSheets } from '../services/diseaseDatasheetService';

// types
import type DiseaseDatasheet from '../types/DiseaseDatasheet';

// components
import DiseaseDatasheetComponent from '../components/DiseaseDatasheetComponent.vue';
import DiseaseSearchInput from '../components/DiseaseSearchInput.vue';

import { ref } from 'vue';

const diseaseSelectedObject = ref<DiseaseDatasheet | null>(null);

</script>

<template>
  <div>
    <disease-search-input
      :array-of-sheets="arrayOfSheets"
      @@disease-selected="diseaseSelectedObject = $event"
    />
    <disease-datasheet-component :disease-sheet="diseaseSelectedObject" />
  </div>
</template>

<style scoped></style>