# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import Blueprint
import json
from evergreen_analitica import ingestedFiles
from bson import json_util

tratamiento_archivos_micro_service = Blueprint("tratamiento_archivos_micro_service", __name__)

"""
    'OriginalFile',
    'FileName',
    'FileExt',
    'FileSize',
    'Url',
    'Status'
"""

@tratamiento_archivos_micro_service.route('/api/listar_archivos', methods=['GET'])
def listar_archivos():
    print("Listando los archivos")
    archivos = list(ingestedFiles.find({}))
    archivos_enviar = json.loads(json_util.dumps(archivos))
    return jsonify({'archivos': archivos_enviar})


@tratamiento_archivos_micro_service.route('/api/cambiar_nombre_archivo', methods=['POST'])
def cambiar_nombre_archivo():
    nombre_archivo = request.json.get('nombre_archivo')
    nuevo_nombre_archivo = request.json.get('nuevo_nombre_archivo')

    archivo = ingestedFiles.find_one({'FileName': nombre_archivo})
    if not archivo:
        return jsonify({'error': 'No se encontró el archivo'})

    ingestedFiles.update_one({'FileName': nombre_archivo}, {'$set': {'FileName': nuevo_nombre_archivo}})

    archivo_actualizado = ingestedFiles.find_one({'FileName': nuevo_nombre_archivo})
    return jsonify({'archivo': archivo_actualizado})

