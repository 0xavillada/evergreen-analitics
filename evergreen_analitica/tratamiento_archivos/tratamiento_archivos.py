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
    archivos = list(ingestedFiles.find({}))
    archivos_enviar = json.loads(json_util.dumps(archivos))
    return jsonify({'archivos': archivos_enviar}), 200


@tratamiento_archivos_micro_service.route('/api/actualizar_archivo/<string:file_id>', methods=['PUT'])
def actualizar_archivo(file_id):
    # Obtener el nuevo nombre de archivo del cuerpo de la solicitud
    nuevo_nombre = request.json['nuevo_nombre']

    # Buscar el archivo por ID y verificar si se encontró o no
    archivo_db = ingestedFiles.find_one({'_id': ObjectId(file_id)})
    if not archivo_db:
        return jsonify({'error': 'No se encontró el archivo con ese ID'}), 404

    # Actualizar el campo de nombre de archivo en la base de datos
    ingestedFiles.update_one({'_id': ObjectId(file_id)}, {'$set': {'FileName': nuevo_nombre}})

    # Devolver el archivo actualizado
    archivo_actualizado = ingestedFiles.find_one({'_id': ObjectId(file_id)})
    archivo_enviar = json.loads(json_util.dumps(archivo_actualizado))
    return jsonify({'archivo': archivo_enviar}), 200

