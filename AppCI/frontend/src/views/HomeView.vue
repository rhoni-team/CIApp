<script setup lang="ts">

// services
import { arrayOfSheets } from '../services/diseaseDatasheetService';

// types
import DiseaseDatasheet from '../types/DiseaseDatasheet';

// components
import DiseaseDatasheetComponent from '../components/DiseaseDatasheetComponent.vue';
import BottomNav from '../components/BottomNav.vue';
import DiseaseSearchInput from '../components/DiseaseSearchInput.vue';
// import DarkLightButton from '../components/DarkLightButton.vue';

import { ref } from 'vue';

const diseaseSelectedObject = ref<DiseaseDatasheet | null>(null);

</script>

<template>
  <div>
    <!-- <dark-light-button /> -->

    <disease-search-input
      :array-of-sheets="arrayOfSheets"
      @@disease-selected="diseaseSelectedObject = $event"
    />

    <DiseaseDatasheetComponent :disease-sheet="diseaseSelectedObject" />

    <!-- <bottom-nav /> -->
  </div>
</template>

<style scoped></style>