import requests
import json
from pymongo import MongoClient  # Libreria de 'pymongo' está instalado

class CapturaDatos:
    def __init__(self):
        self.dataJson = []
        self.finalJson = []

    @staticmethod
    def captura(self):
        resultado_busqueda = requests.get("https://www.datos.gov.co/resource/m5pi-7cau.json")
        self.dataJson = resultado_busqueda.json()
        self.limpieza()  # Llama a limpieza después de capturar los datos
    @staticmethod
    def limpieza(self):
        cleaned_data = []
        for ind in range(len(self.dataJson)):
            jsonClean = {
                "year": "",
                "quarter": "",
                "provider": "",
                "income": "",
                "amountSMS": ""
            }
            # Limpieza de proveedores
            proveedor = self.dataJson[ind]['proveedor']
            if proveedor == "ALMACENES EXITO INVERSIONES S.A.S":
                jsonClean['provider'] = "MOVIL EXITO"
            elif proveedor == "AVANTEL S.A.S":
                jsonClean['provider'] = "WOM"
            elif proveedor == "VIRGIN MOBILE COLOMBIA S.A.S.":
                jsonClean['provider'] = "VIRGIN MOBILE"
            elif proveedor == "SUMA MOVIL S.A":
                jsonClean['provider'] = "SUMA MOVIL"
            elif proveedor == "COLOMBIA MOVIL S.A ESP":
                jsonClean['provider'] = "CLARO"
            elif proveedor == "COMUNICACION CELULAR S A COMCEL S A":
                jsonClean['provider'] = "CLARO"
            elif proveedor == "LOGISTICA FLASH COLOMBIA S.A.S":
                jsonClean['provider'] = "FLASH"
            elif proveedor == "EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A ESP":
                jsonClean['provider'] = "ETB"
            elif proveedor == "SECTROC MOBILE GROUP SAS":
                jsonClean['provider'] = "SECTROC"
            elif proveedor == "COMUNICACIONES EXITO S.A.S":
                jsonClean['provider'] = "MOVIL EXITO"
            elif proveedor == "PARTNERS TELECOM COLOMBIA S.A.S":
                jsonClean['provider'] = "PARTNERS"
            elif proveedor == "LIWA S.A.S ESP":
                jsonClean['provider'] = "UFF MOVIL S.A.S"
            elif proveedor == "LOV TELECOMUNICACIONES SAS":
                jsonClean['provider'] = "UFF"
            elif proveedor == "COLOMBIA TELECOMUNICACIONES S.A.S":
                jsonClean['provider'] = "MOVISTAR"

            jsonClean['year'] = self.dataJson[ind].get['anno']
            jsonClean['quarter'] = self.dataJson[ind].get['trimestre']
            jsonClean['income'] = self.dataJson[ind].get['ingreso_por_mensajes']
            jsonClean['amountSMS'] = self.dataJson[ind].get['cantidad_de_mensajes']
            self.finalJson.append(jsonClean)
            return self.finalJson





