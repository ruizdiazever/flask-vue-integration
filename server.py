from flask import Flask, jsonify
from flask.templating import render_template

""" En produccion no es necesario trabajar con CORS, debido a que unicamente
estaremos ejecutando todo sobre una unica instancia. """
from flask_cors import CORS


app = Flask(__name__,
            static_folder='./static',
            template_folder='./templates')

# Habilitamos a flask para que solamente resuelva las peticiones de /api/*
# Sobre otras rutas no
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1.0/mensaje')
def message():
    return jsonify('Nuevo mensaje desde un servido Flask')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')            # Esto nos permitira trabajar con las diferentes rutas creadas en Vue
def render_vue(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)