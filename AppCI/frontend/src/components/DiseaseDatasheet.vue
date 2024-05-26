<script lang="ts" setup>
import infoIcon from '@/assets/icons/infoIcon.vue';
import fileIcon from '@/assets/icons/fileIcon.vue';
import okIcon from '@/assets/icons/okIcon.vue';
import noIcon from '@/assets/icons/noIcon.vue';
import warningIcon from '@/assets/icons/warningIcon.vue';
import bugIcon from '@/assets/icons/bugIcon.vue';
import squaresIcon from '@/assets/icons/squaresIcon.vue';
</script>

<template>
  <div class="disease-datasheet-wrapper">
    <div class="disease-title-wrapper">
      <bug-icon class="size-8 text-pink-400" />
      <h1 class="disease-title">
        Dengue
      </h1>
      <info-icon class="size-8 text-orange-400" />
      <warning-icon class="size-8 text-red-500 blink" />
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Precauciones
      </div>

      <div class="disease-datasheet-icons-wrapper">
        <squares-icon class="size-14" />
        <squares-icon class="size-14" />
      </div>

      <div class="disease-datasheet-files-wrapper">
        <info-icon class="size-11 text-orange-400" />
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="cleaning-file"
            class="size-10 text-blue-400"
          />
          <label
            for="cleaning-file"
            class="font-thin"
          >PDF</label>
        </div>
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="cleaning-image"
            class="size-10 text-blue-400"
          />
          <label
            for="cleaning-image"
            class="font-thin"
          >PNG</label>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Modo de limpieza
      </div>

      <div class="disease-datasheet-icons-wrapper">
        <squares-icon class="size-14" />
        <squares-icon class="size-14" />
      </div>

      <div class="disease-datasheet-files-wrapper">
        <info-icon class="size-11 text-orange-400" />
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="cleaning-file"
            class="size-10 text-blue-400"
          />
          <label
            for="cleaning-file"
            class="font-thin"
          >PDF</label>
        </div>
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="cleaning-image"
            class="size-10 text-blue-400"
          />
          <label
            for="cleaning-image"
            class="font-thin"
          >PNG</label>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Tiempo de aislamiento
      </div>

      <div class="disease-datasheet-isolation-time-wrapper">
        <div class="badge badge-primary badge-outline">
          1
        </div>
        <div class="badge badge-primary">
          Mes
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <info-icon class="size-11 text-orange-400" />
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="isolation-time-file"
            class="size-10 text-blue-400"
          />
          <label
            for="isolation-time-file"
            class="font-thin"
          >PDF</label>
        </div>
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="isolation-time-image"
            class="size-10 text-blue-400"
          />
          <label
            for="isolation-time-image"
            class="font-thin"
          >PNG</label>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Declaración
      </div>

      <div class="disease-datasheet-boolean-wrapper">
        <div class="disease-datasheet-boolean-icon-wrapper">
          <label for="mandatory-notification-ok-icon">SI</label>
          <ok-icon
            id="mandatory-notification-ok-icon"
            class="size-10 text-green-500"
          />
        </div>
        <div class="disease-datasheet-boolean-icon-wrapper">
          <label for="mandatory-notification-no-icon">NO</label>
          <no-icon
            id="mandatory-notification-no-icon"
            class="size-10 text-red-600"
          />
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <info-icon class="size-11 text-orange-400" />
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="mandatory-notification-file"
            class="size-10 text-blue-400"
          />
          <label
            for="mandatory-notification-file"
            class="font-thin"
          >PDF</label>
        </div>
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="mandatory-notification-image"
            class="size-10 text-blue-400"
          />
          <label
            for="mandatory-notification-image"
            class="font-thin"
          >PNG</label>
        </div>
      </div>
    </div>
    <div class="disease-datasheet-item-wrapper">
      <div class="disease-datasheet-item-title">
        Comparte habitación
      </div>

      <div class="disease-datasheet-boolean-wrapper">
        <div class="disease-datasheet-boolean-icon-wrapper">
          <label for="sharing-ok-icon">SI</label>
          <ok-icon
            id="sharing-ok-icon"
            class="size-10 text-green-500"
          />
        </div>
        <div class="disease-datasheet-boolean-icon-wrapper">
          <label for="sharing-no-icon">NO</label>
          <no-icon
            id="sharing-no-icon"
            class="size-10 text-red-600"
          />
        </div>
      </div>

      <div class="disease-datasheet-files-wrapper">
        <info-icon class="size-11 text-orange-400" />
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="room-sharing-file"
            class="size-10 text-blue-400"
          />
          <label
            for="room-sharing-file"
            class="font-thin"
          >PDF</label>
        </div>
        <div class="disease-datasheet-files-icon-wrapper">
          <file-icon
            id="room-sharing-image"
            class="size-10 text-blue-400"
          />
          <label
            for="room-sharing-image"
            class="font-thin"
          >PNG</label>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
</style>
