<script setup lang="ts">
import { useRouter } from 'vue-router';
import logo from '../assets/IA-MA.jpg'
const router = useRouter();

const goToEditor = () => {
  router.push('/editor');
};
</script>

<template>

  <v-container class="fill-height d-flex flex-column justify-center align-center text-center">
    <v-img
      :src="logo"
      max-width="100%"
      width="300"
      contain
    ></v-img>

    <!--<h1 class="text-h2 font-weight-bold mb-4 text-primary">
      IA-Malagasy
    </h1>-->
    <p class="text-h5 text-grey-darken-1 mb-8" style="max-width: 600px;">
      Fitaovana hanoratana amin'ny teny Malagasy.
    </p>
    
    <div class="mt-12 d-flex gap-4">
      <v-sheet class="pa-4 ma-2" rounded elevation="2">
        <v-icon icon="mdi-tournament" size="large" color="secondary" class="mb-2"></v-icon>
        <div class="text-subtitle-1 font-weight-bold">Manome fototeny</div>
      </v-sheet>
      <v-sheet class="pa-4 ma-2" rounded elevation="2">
        <v-icon icon="mdi-translate" size="large" color="secondary" class="mb-2"></v-icon>
        <div class="text-subtitle-1 font-weight-bold">Mandika teny</div>
      </v-sheet>
      <v-sheet class="pa-4 ma-2" rounded elevation="2">
        <v-icon icon="mdi-check" size="large" color="secondary" class="mb-2"></v-icon>
        <v-icon icon="mdi-close" size="large" color="secondary" class="mb-2"></v-icon>

        <div class="text-subtitle-1 font-weight-bold">Manitsy teny</div>
      </v-sheet>
      <v-sheet class="pa-4 ma-2" rounded elevation="2">
        <v-icon icon="mdi-text-search" size="large" color="secondary" class="mb-2"></v-icon>
        <div class="text-subtitle-1 font-weight-bold">Maminavina teny</div>
      </v-sheet>
    </div>
    <v-spacer></v-spacer>
    <v-btn 
      color="primary" 
      size="x-large" 
      rounded="" 
      elevation="10"
      prepend-icon="mdi-pencil"
      @click="goToEditor"
    >
      Hanoratra
    </v-btn>

    
  </v-container>
</template>