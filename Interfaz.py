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
import Logica as log

######################### PRELIMINARES ###############################################

base_facturacion="base_de_facturaciones.csv"
base_personas = "base_de_usuarios.csv"
no_de_identidad = []
actividad = []
Cant_actividad = []

############################# FUNCIONES ##################################################

############################ REGISTRAR USUARIO ########################################
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
  global actividad
  global Cant_actividad

  no_de_identidad.append(cedula_usuario.get())
  actividad.append(actividad_lista.get())
  Cant_actividad.append(cant_actividad.get())

########################### BOTÓN DE ENVIAR ################################


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
          
##################################### BOTON DE VER USUARIO ###########################################
#Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def ver_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()
    
    
    #hace:

    lista=log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).mostrar_registro()#################3---------#######

    nombre_usuario.set(lista[1])#----
    edad_usuario.set(lista[2])#----
    meses_usuario.set(lista[3])#---


######################################### BOTON DE ELIMINAR #######################################
#Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def eliminar_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()

    #hace:
    
    log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).elim_usuario()


##########################################################################################################
 
 #Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def modificar_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()

    #hace:
    
    log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).editar_datos()


##############################################################################################################################3