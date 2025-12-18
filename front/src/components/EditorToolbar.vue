<script setup lang="ts">
import { useEditorStore } from '../stores/editor';
import { storeToRefs } from 'pinia';

const editorStore = useEditorStore();
const { editor } = storeToRefs(editorStore);
</script>

<template>
  <template v-if="editor">
    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" :variant="editor.isActive('bold') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBold().run()" :disabled="!editor.can().chain().focus().toggleBold().run()">
      <v-icon>mdi-format-bold</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive('italic') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleItalic().run()" :disabled="!editor.can().chain().focus().toggleItalic().run()">
      <v-icon>mdi-format-italic</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive('strike') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleStrike().run()" :disabled="!editor.can().chain().focus().toggleStrike().run()">
      <v-icon>mdi-format-strikethrough</v-icon>
    </v-btn>

    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" :variant="editor.isActive('heading', { level: 1 }) ? 'tonal' : 'text'" @click="editor.chain().focus().toggleHeading({ level: 1 }).run()">
      <v-icon>mdi-format-header-1</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive('heading', { level: 2 }) ? 'tonal' : 'text'" @click="editor.chain().focus().toggleHeading({ level: 2 }).run()">
      <v-icon>mdi-format-header-2</v-icon>
    </v-btn>

    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" :variant="editor.isActive({ textAlign: 'left' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('left').run()">
      <v-icon>mdi-format-align-left</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive({ textAlign: 'center' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('center').run()">
      <v-icon>mdi-format-align-center</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive({ textAlign: 'right' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('right').run()">
      <v-icon>mdi-format-align-right</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive({ textAlign: 'justify' }) ? 'tonal' : 'text'" @click="editor.chain().focus().setTextAlign('justify').run()">
      <v-icon>mdi-format-align-justify</v-icon>
    </v-btn>

    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" :variant="editor.isActive('bulletList') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBulletList().run()">
      <v-icon>mdi-format-list-bulleted</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive('orderedList') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleOrderedList().run()">
      <v-icon>mdi-format-list-numbered</v-icon>
    </v-btn>

    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" :variant="editor.isActive('codeBlock') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleCodeBlock().run()">
      <v-icon>mdi-code-braces-box</v-icon>
    </v-btn>
    <v-btn icon size="small" :variant="editor.isActive('blockquote') ? 'tonal' : 'text'" @click="editor.chain().focus().toggleBlockquote().run()">
      <v-icon>mdi-format-quote-close</v-icon>
    </v-btn>
    <v-btn icon size="small" variant="text" @click="editor.chain().focus().setHorizontalRule().run()">
      <v-icon>mdi-minus</v-icon>
    </v-btn>

    <v-divider vertical inset class="mx-2"></v-divider>

    <v-btn icon size="small" variant="text" @click="editor.chain().focus().undo().run()" :disabled="!editor.can().chain().focus().undo().run()">
      <v-icon>mdi-undo</v-icon>
    </v-btn>
    <v-btn icon size="small" variant="text" @click="editor.chain().focus().redo().run()" :disabled="!editor.can().chain().focus().redo().run()">
      <v-icon>mdi-redo</v-icon>
    </v-btn>
  </template>
</template>