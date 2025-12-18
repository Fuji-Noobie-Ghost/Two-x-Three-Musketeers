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
          placeholder: 'Commencer à écrire ici…',
        }),
      ],
      content: ``,
    })
  }

  function destroyEditor() {
    editor.value?.destroy()
    editor.value = null
  }

  return { editor, initializeEditor, destroyEditor }
})