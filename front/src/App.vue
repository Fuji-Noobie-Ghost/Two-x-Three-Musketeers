<script setup lang="ts">
import EditorView from './components/EditorView.vue';
import EditorToolbar from './components/EditorToolbar.vue';
</script>

<template>
  <v-app>
    <v-app-bar app color="white" elevation="2" density="compact">
      <v-toolbar-title class="text-h6 font-weight-bold text-grey-darken-2 mx-2">IA-Malagasy</v-toolbar-title>
      
      <EditorToolbar />
      
      <v-spacer></v-spacer>

      <v-btn prepend-icon="mdi-content-save" variant="text">
        Sauvegarder
      </v-btn>

      <v-btn prepend-icon="mdi-printer" variant="text">
        Imprimer
      </v-btn>
    </v-app-bar>
    <v-main class="d-flex align-center justify-center">
      <v-container>
        <EditorView/>
      </v-container>
    </v-main>
  </v-app>
  
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
