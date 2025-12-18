<script setup lang="ts">
import { onMounted, onUnmounted, defineOptions, watch } from 'vue';
import EditorView from './components/EditorView.vue';
import EditorToolbar from './components/EditorToolbar.vue';
import { useEditorStore } from './stores/editor';

const editorStore = useEditorStore();

// Définit le nom du composant pour le débogage (Vue DevTools)
defineOptions({ name: 'App' });

// Observer les changements du texte sélectionné depuis le store
watch(() => editorStore.selectedText, (newSelectedText) => {
  if (newSelectedText) {
    console.log(`%cTexte sélectionné (vu depuis App.vue): ${newSelectedText}`, 'color: blue; font-weight: bold;');
  }
});

// Observer les changements du texte complet
watch(() => editorStore.fullText, (newFullText) => {
  console.log(`%cTexte complet: ${newFullText}`, 'color: green; font-weight: bold;');
});
</script>

<template>
  <v-app>
    <v-app-bar app color="white" elevation="2" density="compact">
      <v-toolbar-title class="text-h6 font-weight-bold text-grey-darken-2 mx-2">IA-Malagasy</v-toolbar-title>
      
      <EditorToolbar />
      
      <v-spacer></v-spacer>

      <!-- <v-btn prepend-icon="mdi-content-save" variant="text">
        Sauvegarder
      </v-btn>

      <v-btn prepend-icon="mdi-printer" variant="text">
        Imprimer
      </v-btn> -->
    </v-app-bar>
    <v-main style="background-color: #fafafa;">
      <v-container fluid>
        <v-row justify="center">
          <v-col cols="8"  class="transition-all duration-300">
            <EditorView/>
          </v-col>
          <v-col 
            v-if="editorStore.selectedText" 
            cols="12" 
            md="4"
            class="animate-col"
          >            
            <v-card class="right-panel" :class="{ 'card-enter-active': editorStore.selectedText }">
              <!-- Section texte sélectionné -->
              <div class="selected-section">
                <div class="section-header">
                  <v-icon color="primary" class="mr-2">mdi-cursor-text</v-icon>
                  <v-card-title class="text-h6 font-weight-bold pa-0">Teny voafantina</v-card-title>
                </div>
                <v-card-text class="selected-text-content">
                  <div class="text-quote">{{ editorStore.selectedText }}</div>
                  <div class="text-meta">
                    <v-chip size="x-small" variant="outlined" color="primary">
                      {{ editorStore.selectedText.length }} caractères
                    </v-chip>
                    <v-chip size="x-small" variant="outlined" color="primary">
                      {{ editorStore.selectedText.split(' ').length }} mots
                    </v-chip>
                  </div>
                </v-card-text>
              </div>

              <v-divider class="my-4"></v-divider>

              <!-- Section traduction -->
              

              <v-divider class="my-4"></v-divider>

              <!-- Section mots apparentés -->
              
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.right-panel {
  padding: 1rem;
  height: 100%;
  background-color: white;
  border-radius: 4px;
  opacity: 0;
  transform: translateX(20px);
  transition: opacity 0.3s ease, transform 0.4s ease;
}

.right-panel.card-enter-active {
  opacity: 1;
  transform: translateX(0);
}

/* Animation pour la colonne */
.animate-col {
  animation: slideIn 0.4s ease-out forwards;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Animation pour la transition de la largeur des colonnes */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Animation subtile pour le contenu */
.selected-section {
  animation: fadeInUp 0.5s ease-out 0.2s both;
}

.text-quote {
  animation: fadeIn 0.6s ease-out 0.3s both;
}

.text-meta {
  animation: fadeIn 0.6s ease-out 0.4s both;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Styles existants */
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