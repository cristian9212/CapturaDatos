import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from Capture import CapturaDatos

prueba = CapturaDatos()
prueba.Captura()
prueba.limpieza()

class PrepareData:

    def __init__(self):
        CapturaDatos()
        CapturaDatos().Captura()
        self.listData = CapturaDatos.limpieza()
        print(self.listData)


prueba = PrepareData()


