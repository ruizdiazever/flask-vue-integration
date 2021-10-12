# Frontend by Vue.js with Flask Server integration
Frontend hecho con Vue.js en su version 2, este consume un servicio web que lo provee nuestro servidor Flask. Hice dos script de bash para automatizar el despliege, configuracion y lanzamiento del frontend y el servidor.

## Run project
```bash
sh build_vue.sh      # Build frontend
sh build_server.sh   # Make virtual enviroment, make config server and run
```

## Frontend: important files
```bash
frontend/src/components/Home.vue  # Main template
frontend/src/router/index.js      # Routes
frontend/config/index.js          # Line 51, path of dist when run build
```
