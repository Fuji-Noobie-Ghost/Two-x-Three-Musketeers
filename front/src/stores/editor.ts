import { defineStore } from 'pinia'
import { Editor } from '@tiptap/vue-3'
import { ref } from 'vue'

import { ListItem } from '@tiptap/extension-list'
import { Color, TextStyle } from '@tiptap/extension-text-style'
import StarterKit from '@tiptap/starter-kit'
import TextAlign from '@tiptap/extension-text-align'
import Placeholder from '@tiptap/extension-placeholder'

export const useEditorStore = defineStore('editor', () => {
  const editor = ref<Editor | null>(null)
  const fullText = ref('')
  const selectedText = ref('')
  let selectionTimeout: number | undefined;

  function initializeEditor() {
    editor.value = new Editor({
      extensions: [
        Color.configure({ types: [TextStyle.name, ListItem.name] }),
        TextStyle.configure({ types: [ListItem.name] }),
        StarterKit,
        TextAlign.configure({
          types: ['heading', 'paragraph', 'listItem'],
          alignments: ['left', 'center', 'right', 'justify'],
          defaultAlignment: 'left',
        }),
        Placeholder.configure({
          placeholder: 'Manomboka manoratra eto …',
        }),
      ],
      content: ``,
      onUpdate: ({ editor }) => {
        const currentText = editor.getText()
        fullText.value = currentText
        // Récupère le contenu de l'éditeur et l'affiche dans la console
        console.log("Texte complet (depuis le store):", currentText);
      },
       onSelectionUpdate: ({ editor }) => {
        // On efface le précédent timeout pour ne pas déclencher de multiples mises à jour
        if (selectionTimeout) {
          clearTimeout(selectionTimeout);
        }

        // On attend 200ms d'inactivité avant de considérer la sélection comme "terminée"
        selectionTimeout = window.setTimeout(() => {
          const { from, to } = editor.state.selection;
          const finalSelectedText = editor.state.doc.textBetween(from, to, ' ');
          selectedText.value = finalSelectedText;

          if (finalSelectedText) {
            console.log('Sélection terminée (depuis le store):', finalSelectedText);
          }
        }, 500); // Délai de 200ms
      },
    })
  }

  function destroyEditor() {
    editor.value?.destroy();
    if (selectionTimeout) {
      clearTimeout(selectionTimeout);
    }
    editor.value = null;
    fullText.value = '';
    selectedText.value = '';
  }

  return { editor, initializeEditor, destroyEditor, fullText, selectedText }
})