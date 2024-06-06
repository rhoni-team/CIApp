<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import VueTailwinDatePicker from 'vue-tailwind-datepicker';
import dayjs from 'dayjs';
import 'dayjs/locale/es';
import LocalizedFormat from 'dayjs/plugin/localizedFormat';
import customParseFormat from 'dayjs/plugin/customParseFormat'
  
dayjs.extend(customParseFormat)
dayjs.extend(LocalizedFormat)
dayjs.locale('es');

const startSymptomsDate = ref("");
const isolationTime = ref(0);
const isolationTimeUnit = ref<dayjs.ManipulateType | undefined>();
const isolationEndDate = ref();
const formatter = ref({
  date: 'DD MMMM YYYY',
  month: 'MMMM',
})

watchEffect(async () => {
  isolationEndDate.value = dayjs(startSymptomsDate.value, 'DD MMMM YYYY', 'es').add(isolationTime.value, isolationTimeUnit.value).format('dddd DD MMMM YYYY');
});

</script>

<template>
  <div class="isolation-calculator-wrapper">
    <label for="startSymptomsDate">Inicio de síntoma</label>
    <Vue-tailwin-datePicker
      id="startSymptomsDate"
      v-model="startSymptomsDate"
      placeholder="Seleccione una fecha"
      :formatter="formatter"
      class="input-bordered input-info w-full max-w-xs"
      as-single
      overlay
      i18n="es"
    />
    <label for="isolationTime">Tiempo de aislamiento</label>
    <input
      id="isolationTime"
      v-model="isolationTime"
      type="number"
      class="input input-bordered input-info w-full max-w-xs text-info"
    >
    <label for="isolationPeriod">Periodo de aislamiento</label>
    <select
      id="isolationPeriod"
      v-model="isolationTimeUnit"
      class="input input-bordered input-info w-full max-w-xs text-info"
    >
      <option value="day">
        Días
      </option>
      <option value="week">
        Semanas
      </option>
      <option value="month">
        Meses
      </option>
    </select>
    <br>
    <label for="isolation-end-date">Fin del aislamiento</label>
    <p
      v-if="isolationEndDate !== 'Invalid Date' && isolationTimeUnit !== undefined && isolationTime !== 0"  
      id="isolation-end-date" 
      class="text-secondary font-bold text-3xl"
    >
      {{ isolationEndDate }}
    </p>
  </div>
</template>
