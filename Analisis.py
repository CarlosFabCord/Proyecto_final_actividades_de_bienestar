import random
import math
import csv
import os
import pandas as pd
from tkinter.scrolledtext import ScrolledText
import io

base_personas = "base_de_usuarios.csv"

def reg_usuario():


    num_identidad = str(id_usuario.get())
    nombre = nombre_usuario.get()
    edad = edad_usuario.get()
    meses = meses_usuario.get()



    fila = {
        'No. identidad': num_identidad,
        'Nombre': nombre,
        'Edad': edad,
        'Meses': meses,
        'Monto acumulado': 0
    }


    # Verificar si ya existe el archivo
    archivo_existe = os.path.isfile(base_personas)

    with open(base_personas, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe:
            escritor.writeheader()
        escritor.writerow(fila)