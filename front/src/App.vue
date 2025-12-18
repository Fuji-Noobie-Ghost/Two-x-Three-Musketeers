<script setup lang="ts">
import { onMounted, onUnmounted, defineOptions } from 'vue';
import EditorView from './components/EditorView.vue';
import EditorToolbar from './components/EditorToolbar.vue';
import { useEditorStore } from './stores/editor';

const editorStore = useEditorStore();

// Définit le nom du composant pour le débogage (Vue DevTools)
defineOptions({ name: 'App' });

// Initialiser l'éditeur quand le composant est monté
onMounted(() => editorStore.initializeEditor());

// Détruire l'éditeur pour nettoyer quand le composant est démonté
onUnmounted(() => editorStore.destroyEditor());
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
    <v-main style="background-color: #fafafa;">
      <v-container fluid>
        <v-row>
          <v-col cols="12" md="8">
            <EditorView/>
          </v-col>
          <v-col cols="12" md="4">
            <div class="right-panel">Contenu de la div de droite</div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
  
</template>

<style scoped>
.right-panel {
  border: 1px dashed #ccc;
  padding: 1rem;
  height: 100%;
  background-color: white;
  border-radius: 4px;
}
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
