# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import Blueprint
import json
from evergreen_analitica import ingestedFiles
from bson import json_util, ObjectId

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
    file_id = request.json.get('FileId')
    nuevo_nombre = request.json.get('nuevo_nombre')

    archivo = ingestedFiles.find_one({'_id': ObjectId(file_id)})
    if not archivo:
        return jsonify({'error': 'No se encontró el archivo con ese ID'})

    ingestedFiles.update_one({'_id': ObjectId(file_id)}, {'$set': {'nombre': nuevo_nombre}})

    archivo_actualizado = ingestedFiles.find_one({'_id': ObjectId(file_id)})
    archivo_enviar = json.loads(json_util.dumps(archivo_actualizado))
    return jsonify({'archivo': archivo_enviar})


