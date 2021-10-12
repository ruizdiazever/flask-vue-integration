#!/bin/bash
cd frontend
npm install
npm run build
cp dist/static/css/*.css ../static/css/
cp dist/static/js/*.js ../static/js/
cp dist/*.html ../templates/
cp -R dist/static/img ../static/img/
