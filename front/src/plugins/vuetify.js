// front/src/plugins/vuetify.ts
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css' 

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
  },
  // Ajoutez cette section :
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#4CAF4F',    // Le vert de votre image
          secondary: '#4D4D4D',  // Le gris foncé du texte
          info: '#2196F3',
          success: '#4CAF50',
          warning: '#FB8C00',
          error: '#FF5252',
          background: '#F5F7FA', // Le gris très clair du fond
        },
      },
    },
  },
})

export default vuetify
