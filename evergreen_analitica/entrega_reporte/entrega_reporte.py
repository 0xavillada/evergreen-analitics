# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import Blueprint
import json, os, requests

entrega_reporte_micro_service = Blueprint("entrega_reporte_micro_service", __name__)

@entrega_reporte_micro_service.route('/api/entrega_reporte_xlsx', methods=['POST'])
def entrega_reporte_xlsx():
    print("entrega reporte xlsx")


@entrega_reporte_micro_service.route('/api/entrega_reporte_pdf', methods=['POST'])
def entrega_reporte_pdf():
    print("entrega reporte pdf")
