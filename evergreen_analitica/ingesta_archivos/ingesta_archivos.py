# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import Blueprint
import json, os, requests

ingesta_archivos_micro_service = Blueprint("ingesta_archivos_micro_service", __name__)

@ingesta_archivos_micro_service.route('/api/ingesta_archivos_xlsx', methods=['POST'])
def entrega_reporte_xlsx():
    # El request debe venir con: 'Content-Type': 'application/json'
    data = request.json
    print("----------------------------")
    print(data["fileData"])
    print("----------------------------")
    return "datos de archivo guardados!!"