<template lang="html">
  <div class="">
    <p> {{ mensaje }} </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      mensaje: 'Nuevo mensaje desde Vue.js'
    }
  },
  methods: {
    getMensaje () {
      const path = 'http://localhost:5000/api/v1.0/mensaje' /* Ruta donde realizamos la peticion */
      axios.get(path).then((respuesta) => { /* Usamos axios para la peticion, usamos then (una promesa) */
        this.mensaje = respuesta.data
      })
        .catch((error) => { /* Si no puede realizar la peticion, lo siguiente.. */
          console.error(error)
        })
    }
  },
  created () {
    this.getMensaje() /* Cuando el componente se cree, vamos a ejecutar este mensaje  */
  }
}
</script>

<style lang="css" scoped>
</style>
