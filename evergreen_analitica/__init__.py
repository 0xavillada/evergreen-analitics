# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, resources = { r"/*": {"origins": "*"}})

# Definiciones de rutas Blueprints
from evergreen_analitica.entrega_reporte.entrega_reporte import entrega_reporte_micro_service
from evergreen_analitica.ingesta_archivos.ingesta_archivos import ingesta_archivos_micro_service

# Instancios de Blueprints
app.register_blueprint(entrega_reporte_micro_service)
app.register_blueprint(ingesta_archivos_micro_service)


@app.route('/api/')
def index():
    return "!OK"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')