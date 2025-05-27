import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

base_personas = "base_de_usuarios.csv"
base_facturacion="base_de_facturaciones.csv"

class UsuarioAnalyzer():
   def __init__(self, df):
        self.df = df

   def mostrar_registro(self):
    try:
        buscar=usuario_registro.get()
        archivo_existe = os.path.isfile(base_personas)
        if archivo_existe==True:
           data = pd.read_csv(base_personas) #en mi caso lo convertiría en diccionario
           data["No. identidad"] = data["No. identidad"].astype(str)
           uni_fila=data[data['No. identidad']==buscar]
           lista=uni_fila.values.tolist()[0]
           nombre.set(lista[1])
           edad.set(lista[2])
           meses.set(lista[3])
        else:
           arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
           resultado.set(arc_inexistente)

    except IndexError:
      messagebox.showerror("Error", "El usuario no existe")


def editar_datos(self):

  try:
    buscar=usuario_registro.get()
    archivo_existe = os.path.isfile(base_personas)
    if archivo_existe==True:
      data = pd.read_csv(base_personas)
      data["No. identidad"] = data["No. identidad"].astype(str)
      indice = data['No. identidad']==buscar
      data.loc[indice, 'Nombre'] = nombre.get()
      data.loc[indice, 'Edad'] = edad.get()
      data.to_csv(base_personas, index=False)

    else:
      arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
      resultado.set(arc_inexistente)

  except IndexError:
        messagebox.showerror("Error", "El proyecto no existe")


def elim_usuario(self):

  try:
    buscar=usuario_registro.get()
    archivo_existe = os.path.isfile(base_personas), os.path.isfile(base_facturacion)

    if archivo_existe==True:
      data = pd.read_csv(base_personas)
      data_fac = pd.read_csv(base_facturacion)
      data["No. identidad"] = data["No. identidad"].astype(str)
      data_fac["No. identidad"] = data_fac["No. identidad"].astype(str)
      indice = data[data['No. identidad']==buscar].index
      indice_fac = data_fac[data_fac['No. identidad']==buscar].index
      data.drop(index=indice, inplace=True)
      data.drop(index=indice_fac, inplace=True)
      data.to_csv(base_personas, index=False)
      data.to_csv(base_facturacion, index=False)

    else:
      arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
      resultado.set(arc_inexistente)

  except IndexError:
        messagebox.showerror("Error", "El usuario no existe")