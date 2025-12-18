<template>
  <div v-if="editor" class="container">
    <v-toolbar density="compact" class="mb-4">
      <!-- Boutons existants... -->
      <v-btn icon :variant="editor.isActive('bold') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBold().run()" :disabled="!editor.can().chain().focus().toggleBold().run()">
        <v-icon>mdi-format-bold</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('italic') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleItalic().run()" :disabled="!editor.can().chain().focus().toggleItalic().run()">
        <v-icon>mdi-format-italic</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('strike') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleStrike().run()" :disabled="!editor.can().chain().focus().toggleStrike().run()">
        <v-icon>mdi-format-strikethrough</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('code') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleCode().run()" :disabled="!editor.can().chain().focus().toggleCode().run()">
        <v-icon>mdi-code-tags</v-icon>
      </v-btn>

      <v-divider vertical inset class="mx-2"></v-divider>

      <v-btn icon :variant="editor.isActive('heading', { level: 1 }) ? 'tonal' : 'text'" @click="editor.chain().focus().toggleHeading({ level: 1 }).run()">
        <v-icon>mdi-format-header-1</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('heading', { level: 2 }) ? 'tonal' : 'text'" @click="editor.chain().focus().toggleHeading({ level: 2 }).run()">
        <v-icon>mdi-format-header-2</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('paragraph') ? 'tonal' : 'text'" @click="editor.chain().focus().setParagraph().run()">
        <v-icon>mdi-format-paragraph</v-icon>
      </v-btn>

      <v-divider vertical inset class="mx-2"></v-divider>

      <!-- Boutons d'alignement (AJOUT) -->
      <v-btn icon :variant="editor.isActive({ textAlign: 'left' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('left').run()">
        <v-icon>mdi-format-align-left</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive({ textAlign: 'center' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('center').run()">
        <v-icon>mdi-format-align-center</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive({ textAlign: 'right' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('right').run()">
        <v-icon>mdi-format-align-right</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive({ textAlign: 'justify' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('justify').run()">
        <v-icon>mdi-format-align-justify</v-icon>
      </v-btn>

      <v-divider vertical inset class="mx-2"></v-divider>

      <v-btn icon :variant="editor.isActive('bulletList') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBulletList().run()">
        <v-icon>mdi-format-list-bulleted</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('orderedList') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleOrderedList().run()">
        <v-icon>mdi-format-list-numbered</v-icon>
      </v-btn>

      <v-divider vertical inset class="mx-2"></v-divider>

      <v-btn icon :variant="editor.isActive('codeBlock') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleCodeBlock().run()">
        <v-icon>mdi-code-braces-box</v-icon>
      </v-btn>
      <v-btn icon :variant="editor.isActive('blockquote') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBlockquote().run()">
        <v-icon>mdi-format-quote-close</v-icon>
      </v-btn>
      <v-btn icon variant="text" @click="editor.chain().focus().setHorizontalRule().run()">
        <v-icon>mdi-minus</v-icon>
      </v-btn>

      <v-divider vertical inset class="mx-2"></v-divider>

      <v-btn icon variant="text" @click="editor.chain().focus().undo().run()" :disabled="!editor.can().chain().focus().undo().run()">
        <v-icon>mdi-undo</v-icon>
      </v-btn>
      <v-btn icon variant="text" @click="editor.chain().focus().redo().run()" :disabled="!editor.can().chain().focus().redo().run()">
        <v-icon>mdi-redo</v-icon>
      </v-btn>
    </v-toolbar>
    <editor-content :editor="editor" />
  </div>
</template>

<script>
import { ListItem } from '@tiptap/extension-list';
import { Color, TextStyle } from '@tiptap/extension-text-style';
import StarterKit from '@tiptap/starter-kit';
import TextAlign from '@tiptap/extension-text-align'; // AJOUT
import { Editor, EditorContent } from '@tiptap/vue-3';

export default {
  components: {
    EditorContent,
  },

  data() {
    return {
      editor: null,
    };
  },

  mounted() {
    this.editor = new Editor({
      extensions: [
        Color.configure({ types: [TextStyle.name, ListItem.name] }),
        TextStyle.configure({ types: [ListItem.name] }),
        StarterKit,
        // AJOUT: Extension d'alignement
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
        <p style="text-align: justify">
          I know, I know, this is impressive. It's only the tip of the iceberg though. Give it a try and click a little bit around. Don't forget to check the other examples too.
        </p>
        <blockquote>
          Wow, that's amazing. Good work, boy! 👏
          <br />
          — Mom
        </blockquote>
      `,
    });
  },

  beforeUnmount() {
    this.editor.destroy();
  },
};
</script>

<style lang="scss">
.container {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
}

/* Basic editor styles */
.tiptap {
  :first-child {
    margin-top: 0;
  }

  /* Styles d'alignement (AJOUT) */
  & > * {
    &[style*="text-align: left"] {
      text-align: left;
    }
    
    &[style*="text-align: center"] {
      text-align: center;
    }
    
    &[style*="text-align: right"] {
      text-align: right;
    }
    
    &[style*="text-align: justify"] {
      text-align: justify;
    }
  }

  /* List styles */
  ul,
  ol {
    padding: 0 1rem;
    margin: 1.25rem 1rem 1.25rem 0.4rem;

    li p {
      margin-top: 0.25em;
      margin-bottom: 0.25em;
    }
  }

  /* Heading styles */
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    line-height: 1.1;
    margin-top: 2.5rem;
    text-wrap: pretty;
  }

  h1,
  h2 {
    margin-top: 3.5rem;
    margin-bottom: 1.5rem;
  }

  h1 {
    font-size: 1.4rem;
  }

  h2 {
    font-size: 1.2rem;
  }

  h3 {
    font-size: 1.1rem;
  }

  h4,
  h5,
  h6 {
    font-size: 1rem;
  }

  /* Code and preformatted text styles */
  code {
    background-color: var(--purple-light);
    border-radius: 0.4rem;
    color: var(--black);
    font-size: 0.85rem;
    padding: 0.25em 0.3em;
  }

  pre {
    background: var(--black);
    border-radius: 0.5rem;
    color: var(--white);
    font-family: 'JetBrainsMono', monospace;
    margin: 1.5rem 0;
    padding: 0.75rem 1rem;

    code {
      background: none;
      color: inherit;
      font-size: 0.8rem;
      padding: 0;
    }
  }

  blockquote {
    border-left: 3px solid var(--gray-3);
    margin: 1.5rem 0;
    padding-left: 1rem;
  }

  hr {
    border: none;
    border-top: 1px solid var(--gray-2);
    margin: 2rem 0;
  }
}

.tiptap:focus {
  outline: none;
}
</style>