import requests
import json
import pymongo
from pymongo import MongoClient

class CapturarDatos:
    def __init__(self):
        self.dataJson = []

    def captura(self):
        resultado_busqueda = requests.get("https://www.datos.gov.co/resource/mSpi-7cau.json")
        self.dataJson = resultado_busqueda.json()
        print(f"Tipo de datos: {type(self.dataJson)}")  # Imprimir el tipo de datos
        print(f"Contenido de dataJson: {self.dataJson}")  # Imprimir todo el contenido

    def limpieza(self):
        cleaned_data = []
        provider_mapping = {
            "ALMACENES EXITO INVERSIONES S.A.S": "MOVIL EXITO",
            "AVANTEL S.A.S": "WOM",
            "VIRGIN MOBILE COLOMBIA S.A.S.": "VIRGIN MOBILE",
            "SUMA MOVIL S.A": "SUMA MOVIL",
            "COLOMBIA MOVIL S.A ESP": "CLARO",
            "COMUNICACION CELULAR S A COMCEL S A": "CLARO",
            "LOGISTICA FLASH COLOMBIA S.A.S": "FLASH",
            "EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A ESP": "ETB",
            "SECTROC MOBILE GROUP SAS": "SECTROC",
            "COMUNICACIONES EXITO S.A.S": "MOVIL EXITO",
            "PARTNERS TELECOM COLOMBIA S.A.S": "PARTNERS",
            "LIWA S.A.S ESP": "UFF MOVIL S.A.S",
            "LOV TELECUMICACIONES SAS": "UFF",
            "COLOMBIA TELECUMINICAIONES S.A.S": "MOVISTAR"
        }

        if isinstance(self.dataJson, list):  # Asegurarse de que self.dataJson sea una lista
            for entry in self.dataJson:
                jsonClean = {
                    "year": entry.get('anno', ''),
                    "Quarter": entry.get('trimestre', ''),
                    "provider": provider_mapping.get(entry.get('proveedor'), entry['proveedor']),
                    "Income": entry.get('ingreso_por_mensajes', '')
                }
                cleaned_data.append(jsonClean)
                print(jsonClean)
        else:
            print("Los datos no están en el formato esperado (deben ser una lista).")

        return cleaned_data

if __name__ == "__main__":
    prueba = CapturarDatos()
    prueba.captura()
    prueba.limpieza()
