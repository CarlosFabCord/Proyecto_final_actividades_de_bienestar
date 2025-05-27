import pandas as pd
import random
import math
import csv
import os
from tkinter.scrolledtext import ScrolledText
import io

proyecto = "base_de_proyectos.csv"

def reg_proyect():
    # Datos de ejemplo
    id_proyecto = ['agua', 'piedra', 'perro', 'bolt', 'seboltian']
    longitud_Oper = ['10', '20', '30', '40', '50']
    angulo = ['5', '15', '25', '35', '45']
    operacion = ['res1', 'res2', 'res3', 'res4', 'res5']

    # Verificar si ya existe el archivo
    archivo_existe = os.path.isfile(proyecto)

    with open(proyecto, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=['Id_proyecto', 'Longitud', 'Angulo', 'Resultado'])
        
        if not archivo_existe:
            escritor.writeheader()

        # Escribir fila por fila
        for i in range(len(id_proyecto)):
            fila = {
                'Id_proyecto': id_proyecto[i],
                'Longitud': longitud_Oper[i],
                'Angulo': angulo[i],
                'Resultado': operacion[i]
            }
            escritor.writerow(fila)

reg_proyect()