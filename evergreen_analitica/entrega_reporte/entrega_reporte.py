# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import Blueprint
import json, os, requests
from evergreen_analitica import ingestedFiles
from bson import json_util

entrega_reporte_micro_service = Blueprint("entrega_reporte_micro_service", __name__)

"""
    'OriginalFile',
    'FileName',
    'FileExt',
    'FileSize',
    'Url',
    'Status'
"""

@entrega_reporte_micro_service.route('/api/obtener_archivos', methods=['GET'])
def obtener_archivos():
    print("Obteniendo los archivos")
    archivos = list(ingestedFiles.find({}))
    archivos_enviar = json.loads(json_util.dumps(archivos))
    return jsonify({'archivos': archivos_enviar})


@entrega_reporte_micro_service.route('/api/entrega_reporte_xlsx', methods=['POST'])
def entrega_reporte_xlsx():
    print("entrega reporte xlsx")
    api_cls_to_xlsx_converter = 'https://v2.convertapi.com/convert/csv/to/xlsx?Secret=6mSJbYN6n0hm4GTj&StoreFile=true'
    data = request.json
    url_archivo = data['Url']
    data_post = {
        'File': url_archivo
    }
    post_response = requests.post(api_cls_to_xlsx_converter, data=data_post).json()
    url_xlsx =  post_response['Files'][0]['Url']
    nombre_xlsx = post_response['Files'][0]['FileName']

    return jsonify({'nombre_xlsx': nombre_xlsx, 'url_descarga_xlsx': url_xlsx})


@entrega_reporte_micro_service.route('/api/entrega_reporte_pdf', methods=['POST'])
def entrega_reporte_pdf():
    print("entrega reporte pdf")
    api_xlsx_to_pdf_converter = 'https://v2.convertapi.com/convert/csv/to/pdf?Secret=6mSJbYN6n0hm4GTj&StoreFile=true'
    data = request.json
    url_archivo = data['Url']
    data_post = {
        'File': url_archivo
    }
    post_response = requests.post(api_xlsx_to_pdf_converter, data=data_post).json()
    url_pdf =  post_response['Files'][0]['Url']
    nombre_pdf = post_response['Files'][0]['FileName']

    return jsonify({'nombre_pdf': nombre_pdf, 'url_descarga_pdf': url_pdf})

