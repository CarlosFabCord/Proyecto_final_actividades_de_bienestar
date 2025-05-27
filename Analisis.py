import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image

sns.set_theme()

def pasar_a_pil(grafico):
  buffer = io.BytesIO() 
  canvas = FigureCanvasAgg(grafico) 
  canvas.draw()
  canvas.print_png(buffer)
  buffer.seek(0)
  return Image.open(buffer) 
base_personas = "base_de_usuarios.csv"
base_facturacion="base_de_facturaciones.csv"

class usuario_analisis():
   def __init__(self, df):
        self.df = df

   def mostrar_registro(self):
    try:
        buscar=usuario_registro.get()
        archivo_existe = os.path.isfile(base_personas)
        if archivo_existe==True:
           data = pd.read_csv(base_personas)
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
      arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
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


class graficos(usuario_analisis):
  def _init_(self, data_frame):
    self.df= data_frame

  def graficar_barras(self):
    df = pd.read_csv(base_facturacion)
    db = pd.read_csv(base_personas)
    edad = db["Edad"]
    cantidad_clases = df['Clases Spinning','Clases Fisioterapia','Clases Rumba','Clases Fortalecimiento']
    clases = ['Spinning','Fisioterapia','Rumba','Fortalecimiento']
    grafico, ax = plt.subplots(1, 3, figsize=(9,3), dpi=100) 
    sns.barplot(data= self.df, x= clases , y= cantidad_clases, ax=ax[0])
    ax[0].set_title("Grafico de usuarios por clase", fontsize=7)
    ax[0].set_xlabel(clases, fontsize=6)
    ax[0].set_ylabel(cantidad_clases, fontsize=6)
    ax[0].tick_params(axis='x', labelsize=6)

    sns.histplot(edad, bins = 10, kde = True, ax =ax[1])
    ax[1].title("Histograma de edades")
    ax[1].set_xlabel("Edades", fontsize=7)
    ax[1].set_ylabel("Frecuencia", fontsize=7)

    colores = ["red","green", "blue"]
    ax[2].pie(cantidad_clases, labels=cantidad_clases.index, colors=colores, shadow=True, textprops={'fontsize':6})
    ax[2].set_title("Inscripciones por actividad")
    grafico.tight_layout()   
    return pasar_a_pil(grafico)
  