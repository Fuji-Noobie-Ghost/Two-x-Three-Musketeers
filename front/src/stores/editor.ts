import { defineStore } from 'pinia'
import { Editor } from '@tiptap/vue-3'
import { ref } from 'vue'

import { ListItem } from '@tiptap/extension-list'
import { Color, TextStyle } from '@tiptap/extension-text-style'
import StarterKit from '@tiptap/starter-kit'
import TextAlign from '@tiptap/extension-text-align'

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
      ],
      content: `
        <h2>
          Hi there,
        </h2>
        <p style="text-align: center">
          Ce texte est centré.
        </p>
        <p>
          this is a <em>basic</em> example of <strong>Tiptap</strong>. Sure, there are all kind of basic text styles you'd probably expect from a text editor. But wait until you see the lists:
        </p>
        <ul>
          <li>
            That's a bullet list with one …
          </li>
          <li>
            … or two list items.
          </li>
        </ul>
        <p style="text-align: right">
          Ce texte est aligné à droite.
        </p>
        <p>
          Isn't that great? And all of that is editable. But wait, there's more. Let's try a code block:
        </p>
        <pre><code class="language-css">body {
  display: none;
}</code></pre>
        <p>
          I know, I know, this is impressive. It’s only the tip of the iceberg though. Give it a try and click a little bit around. Don’t forget to check the other examples too.
        </p>
      `,
    })
  }

  function destroyEditor() {
    editor.value?.destroy()
    editor.value = null
  }

  return { editor, initializeEditor, destroyEditor }
})