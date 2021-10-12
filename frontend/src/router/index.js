import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({ /* Estas son las rutas.. Flask las gestiona con la vista 'render_vue' */
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }
  ],
  mode: 'history' /* De esta forma podemos seguir agregando nuevas rutas a nuestro proyecto */
})
