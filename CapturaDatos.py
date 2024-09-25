import requests
import  json
import pymongo import MongoClient
class CapturDatos:

    def__init__(self):
    self.dataJson = []

    def Captura(self):
        resultado_busqueda = requests.get(f"https:/www.datos.gov.co/resource/mSpi-7cau.json")
        self.dataJson = resultado_busqueda.json()

        def limíeza(self):
            for ind in range(len(self.dataJson)):
                jsonClean ={
                    "year":"",
                    "Quarter":"",
                    "provider":"",
                    "Income":""
                }
                if self.dataJson[ind]['proveedor'] == "ALMACENES EXITO INVERSIONES S.A.S":
                    jsonClean['provider'] = "MOVIL EXITO"
                elif self.dataJson[ind]['proveedor'] == "AVANTEL S.A.S":
                    jsonClean['provider'] = "WOM"
                elif self.dataJson[ind]['proveedor']=="VIRGIN MOBILE COLOMBIA S.A.S.":
                    jsonClean['Provider']="VIRGIN MOBILE"
                elif self.dataJson[ind]['proveedor'] == "SUMA MOVIL  S.A EPS":
                    jsonClean['provider']="SUMA MOVIL"
                elif self.dataJson
