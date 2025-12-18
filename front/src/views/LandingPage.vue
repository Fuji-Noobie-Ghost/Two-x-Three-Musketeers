<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const goToEditor = () => {
  router.push('/editor');
};
</script>

<template>
  <v-container class="fill-height d-flex flex-column justify-center align-center text-center">
    <h1 class="text-h2 font-weight-bold mb-4 text-primary">
      IA-Malagasy
    </h1>
    <p class="text-h5 text-grey-darken-1 mb-8" style="max-width: 600px;">
      L'outil intelligent pour l'édition et l'analyse de textes en Malgache.
    </p>
    
    <v-btn 
      color="primary" 
      size="x-large" 
      rounded="pill" 
      elevation="4"
      prepend-icon="mdi-pencil"
      @click="goToEditor"
    >
      Commencer à écrire
    </v-btn>

    <div class="mt-12 d-flex gap-4">
      <v-sheet class="pa-4 ma-2" rounded elevation="1">
        <v-icon icon="mdi-translate" size="large" color="secondary" class="mb-2"></v-icon>
        <div class="text-subtitle-1 font-weight-bold">Traduction</div>
      </v-sheet>
      <v-sheet class="pa-4 ma-2" rounded elevation="1">
        <v-icon icon="mdi-text-search" size="large" color="secondary" class="mb-2"></v-icon>
        <div class="text-subtitle-1 font-weight-bold">Analyse</div>
      </v-sheet>
    </div>
  </v-container>
</template>