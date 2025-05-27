import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from tkinter import messagebox
import random
import math
import csv
import os
import io
from tkinter.scrolledtext import ScrolledText

base_facturacion="base_de_facturaciones.csv"
base_personas = "base_de_usuarios.csv"
No_de_identidad = []
actividad = []
Cant_actividad = []

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


######################### BOTÓN DE FACTURACIÓN ##################################

def guardar():

  global no_de_identidad
  global Actividad
  global Cant_actividad

  No_de_identidad.append(cedula_usuario.get())
  actividad.append(actividad_lista.get())
  Cant_actividad.append(cant_actividad.get())

########################### bOTÓN DE ENVIAR ################################


def enviar():

  global no_de_identidad
  global actividad
  global Cant_actividad
  

  df = pd.read_csv(base_personas)
  archivo_existe = os.path.isfile(base_personas)
                                  
  if not archivo_existe:
      messagebox.showwarning("Error", "No hay registros aún")
  else:
      while True:
          df = pd.read_csv(base_personas)
          try:
              num_identidad = cedula_usuario.get()
              df['No.identidad'] = df['No. identidad'].astype(str)
              indice = df['No. identidad']==num_identidad
              df.loc[indice, 'Meses']+=1
                
              #Aquí identifica existencia de facturación y añade diccionario a csv

              archivo_existe = os.path.isfile(base_facturacion)

              with open(base_facturacion, 'a', newline='') as f:
                  escritor = csv.DictWriter(f, fieldnames=fila.keys())
                  if not archivo_existe:
                      escritor.writeheader()
                  for i in range(len(no_de_identidad)):
                      fila = {
                            'No. de identidad': no_de_identidad[i],
                            'Actividad': actividad[i],
                            'Cant. Actividad': Cant_actividad[i],                            
                        }

                  escritor.writerow(fila)

                
              clases_spinning = 7000
              clases_fisioterapia = 10000
              clases_rumba = 5000
              clases_forta = 6500              
                
              calcular_total = 0

              for i in range(len(actividad)):
                  if actividad[i] == 'Fisioterapia':
                      calcular_total += (Cant_actividad[i]*clases_fisioterapia)
                  elif actividad[i] == 'Spinning':
                      calcular_total += (Cant_actividad[i]*clases_spinning)
                  elif actividad[i] == 'Rumba':
                      calcular_total += (Cant_actividad[i]*clases_rumba)
                  else:
                      calcular_total += (Cant_actividad[i]*clases_forta)                    

                
              etiqueta_total.set(calcular_total)

                
              df.loc[indice, 'Monto acumulado']+=calcular_total
              df.to_csv(base_personas, index=False)

              break
          except:
              messagebox.showwarning("Error", "Este usuario aun no se ha registrado")
              continue