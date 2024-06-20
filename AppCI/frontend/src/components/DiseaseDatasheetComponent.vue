<script setup lang="ts">
import infoIcon from '@/assets/icons/infoIcon.vue';
import fileIcon from '@/assets/icons/fileIcon.vue';
import okIcon from '@/assets/icons/okIcon.vue';
import noIcon from '@/assets/icons/noIcon.vue';
import xMarkIcon from '@/assets/icons/xMarkIcon.vue';
import warningIcon from '@/assets/icons/warningIcon.vue';
import bugIcon from '@/assets/icons/bugIcon.vue';
import squaresIcon from '@/assets/icons/squaresIcon.vue';

import type { DiseaseDetail } from '@/types/DiseaseDetail';

defineProps<{
  diseaseSheet: DiseaseDetail | null
}>();

</script>

<template>
  <div
    v-if="diseaseSheet"
    class="disease-datasheet-wrapper"
  >
    <div class="disease-title-wrapper">
      <div class="disease-type-icon-wrapper">
        <bug-icon class="size-6 text-pink-400" />
        {{ diseaseSheet.type }}
      </div>
      <h1 class="disease-title">
        {{ diseaseSheet ? diseaseSheet.name : "No se seleccionó" }}
      </h1>
      <div v-if="diseaseSheet.info?.length != 0">
        <div
          v-for="(item, key) in diseaseSheet.info"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <info-icon class="size-11 text-orange-400" />
        </div>
      </div>

      <div v-if="diseaseSheet.warnings?.length">
        <warning-icon
          class="size-8 text-red-500 blink"
          onclick="warning_modal.showModal()"
        />
        <dialog
          id="warning_modal"
          class="modal"
        >
          <div class="modal-box">
            <p
              v-for="(warning, key) in diseaseSheet.warnings"
              :key="key"
              class="py-4"
            >
              {{ warning.label }}
            </p>
          </div>
          <form
            method="dialog"
            class="modal-backdrop"
          >
            <button>close</button>
          </form>
        </dialog>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Precauciones
      </div>

      <div class="disease-datasheet-icons-wrapper">
        <div v-if="diseaseSheet.cautions?.precautions">
          <div
            v-for="(item, key) in diseaseSheet.cautions.precautions"
            :key="key"
            class="tooltip"
            :data-tip="`${item.label}`"
          >
            <squares-icon
              :id="`id`"
              class="size-14"
            />
          </div>
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <div
          v-for="(item, key) in diseaseSheet.cautions.info"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <info-icon class="size-11 text-orange-400" />
        </div>
        <div v-if="diseaseSheet.cautions?.files.length">
          <div
            v-for="(item, key) in diseaseSheet.cautions.files"
            :key="key"
            class="tooltip"
            :data-tip="`${item}`"
          >
            <div class="disease-datasheet-files-icon-wrapper">
              <file-icon
                :id="`caution-file-${key}`"
                class="size-10 text-blue-400"
              />
              <label
                :for="`caution-file-${key}`"
                class="font-thin"
              >PDF</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Modo de limpieza
      </div>

      <div class="disease-datasheet-icons-wrapper">
        <div v-if="diseaseSheet.cleaning?.cleaning_type">
          <div
            v-for="(item, key) in diseaseSheet.cleaning.cleaning_type"
            :key="key"
            class="tooltip"
            :data-tip="`${item.label}`"
          >
            <squares-icon
              :id="`id-${key}`"
              class="size-14"
            />
          </div>
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <div v-if="diseaseSheet.cleaning?.info.length">
          <div
            v-for="(item, key) in diseaseSheet.cleaning.info"
            :key="key"
            class="tooltip"
            :data-tip="`${item}`"
          >
            <info-icon class="size-11 text-orange-400" />
          </div>
        </div>
        <div v-if="diseaseSheet.cleaning?.files.length">
          <div
            v-for="(item, key) in diseaseSheet.cleaning.files"
            :key="key"
            class="tooltip"
            :data-tip="`${item}`"
          >
            <div class="disease-datasheet-files-icon-wrapper">
              <file-icon
                :id="`cleaning-file-${key}`"
                class="size-10 text-blue-400"
              />
              <label
                :for="`cleaning-file-${key}`"
                class="font-thin"
              >PDF</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Tiempo de aislamiento
      </div>

      <div class="disease-datasheet-isolation-time-wrapper">
        <div
          v-if="diseaseSheet.isolation?.isolationTime"
          class="badge badge-primary badge-outline"
        >
          {{ diseaseSheet.isolation.isolationTime }}
        </div>
        <div
          v-if="diseaseSheet.isolation?.isolationPeriod"
          class="badge badge-primary"
        >
          {{ diseaseSheet.isolation.isolationPeriod }}
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <div v-if="diseaseSheet.isolation?.info.length">
          <div
            v-for="(item, key) in diseaseSheet.isolation.info"
            :key="key"
            class="tooltip"
            :data-tip="`${item}`"
          >
            <info-icon class="size-11 text-orange-400" />
          </div>
        </div>
        <div v-if="diseaseSheet.isolation?.files.length">
          <div
            v-for="(item, key) in diseaseSheet.isolation.files"
            :key="key"
            class="tooltip"
            :data-tip="`${item}`"
          >
            <div class="disease-datasheet-files-icon-wrapper">
              <file-icon
                :id="`isolation-file-${key}`"
                class="size-10 text-blue-400"
              />
              <label
                :for="`isolation-file-${key}`"
                class="font-thin"
              >PDF</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Declaración
      </div>

      <div class="disease-datasheet-boolean-wrapper">
        <div
          v-if="diseaseSheet.mandatoryNotification?.notify"
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="mandatory-notification-ok-icon">SI</label>
          <ok-icon
            id="mandatory-notification-ok-icon"
            class="size-10 text-green-500"
          />
        </div>
        <div
          v-else-if="diseaseSheet.mandatoryNotification?.notify === false"
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="mandatory-notification-ok-icon">NO</label>
          <no-icon
            id="mandatory-notification-ok-icon"
            class="size-10 text-red-500"
          />
        </div>
        <div
          v-else
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="mandatory-notification-no-icon">NO HAY DATOS</label>
          <x-mark-icon
            id="mandatory-notification-null-icon"
            class="size-10 text-slate-400"
          />
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <div
          v-for="(item, key) in diseaseSheet.mandatoryNotification?.info"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <info-icon class="size-11 text-orange-400" />
        </div>
        <div
          v-for="(item, key) in diseaseSheet.mandatoryNotification?.files"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <div class="disease-datasheet-files-icon-wrapper">
            <file-icon
              :id="`mandatoryNotification-file-${key}`"
              class="size-10 text-blue-400"
            />
            <label
              :for="`mandatoryNotification-file-${key}`"
              class="font-thin"
            >PDF</label>
          </div>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Comparte habitación
      </div>

      <div class="disease-datasheet-boolean-wrapper">
        <div
          v-if="diseaseSheet.roomSharing?.shareable === true"
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="sharing-ok-icon">SI</label>
          <ok-icon
            id="sharing-ok-icon"
            class="size-10 text-green-500"
          />
        </div>
        <div
          v-else-if="diseaseSheet.roomSharing?.shareable === false"
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="sharing-no-icon">NO</label>
          <no-icon
            id="sharing-no-icon"
            class="size-10 text-red-600"
          />
        </div>
        <div
          v-else
          class="disease-datasheet-boolean-icon-wrapper"
        >
          <label for="sharing-null-icon">NO HAY DATOS</label>
          <x-mark-icon
            id="sharing-null-icon"
            class="size-10 text-slate-400"
          />
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <div
          v-for="(item, key) in diseaseSheet.roomSharing?.info"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <info-icon class="size-11 text-orange-400" />
        </div>
        <div
          v-for="(item, key) in diseaseSheet.roomSharing?.files"
          :key="key"
          class="tooltip"
          :data-tip="`${item}`"
        >
          <div class="disease-datasheet-files-icon-wrapper">
            <file-icon
              :id="`roomSharing-file-${key}`"
              class="size-10 text-blue-400"
            />
            <label
              :for="`roomSharing-file-${key}`"
              class="font-thin"
            >PDF</label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style></style>
