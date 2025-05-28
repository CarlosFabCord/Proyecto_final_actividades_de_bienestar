import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image

def pasar_a_pil(grafico):
  buffer = io.BytesIO() #Vincula a un método de io
  canvas = FigureCanvasAgg(grafico) #vincaula a un método de FigureCanvas y usará la figura para crear un canvas
  canvas.draw()
  canvas.print_png(buffer)
  buffer.seek(0)
  return Image.open(buffer) #abre lo que hay en el buffer      

class Analisis:
  def __init__(self,base_personas,base_facturacion):
    self.base_personas=base_personas
    self.base_facturacion=base_facturacion


  def graficar_barras(self):

    tabla_actividad=self.base_facturacion[self.base_facturacion['Actividad']=="RUMBA"]
    sin_duplicados_rumba=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=self.base_facturacion[self.base_facturacion['Actividad']=="SPINING"]
    sin_duplicados_spining=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=self.base_facturacion[self.base_facturacion['Actividad']=="FORTALECIMIENTO"]
    sin_duplicados_fortalecimiento=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=self.base_facturacion[self.base_facturacion['Actividad']=="FISIOTERAPIA"]
    sin_duplicados_fisioterapia=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")


    df_rumba=pd.DataFrame(sin_duplicados_rumba)
    df_spining=pd.DataFrame(sin_duplicados_spining)
    df_fortalecimiento=pd.DataFrame(sin_duplicados_fortalecimiento)
    df_fisioterapia=pd.DataFrame(sin_duplicados_fisioterapia)
    df_rumba['No. de identidad'].value_counts().sum()
    valor_rumba = df_rumba['No. de identidad'].value_counts().sum()
    valor_spining = df_spining['No. de identidad'].value_counts().sum()
    valor_fortalecimiento = df_fortalecimiento['No. de identidad'].value_counts().sum()
    valor_fisioterapia = df_fisioterapia['No. de identidad'].value_counts().sum()

    diccionario_valores = {
    'Rumba': int(valor_rumba),
    'Spinning': int(valor_spining),
    'Fortalecimiento': int(valor_fortalecimiento),
    'Fisioterapia': int(valor_fisioterapia)
    }

    db = pd.DataFrame(diccionario_valores)
    cantidad_clases = db[['Rumba', 'Spinning', 'Fortalecimiento', 'Fisioterapia']]
    clases = ['Spinning','Fisioterapia','Rumba','Fortalecimiento']
    grafico_pie = sns.barplot(data= db, x= clases , y= cantidad_clases)
    plt.title("Grafico de usuarios por clase", fontsize=7)
    plt.xlabel(clases, fontsize=6)
    plt.ylabel(cantidad_clases, fontsize=6)
    plt.tick_params(axis='x', labelsize=6)
    return pasar_a_pil(grafico_pie)
  
  def grafico_circular(self): 
    
    colores = ["red","green", "blue", "yellow"]
    grafico = plt.pie(self.base_facturacion['Actividad'], labels=self.base_facturacion['Actividad'].index, colors=colores, shadow=True, textprops={'fontsize':6})
    plt.title("Inscripciones por actividad")
    return pasar_a_pil(grafico)

  def total_usuarios(self):
    cantidad_total = self.base_personas['No. identidad'].sum()
    return cantidad_total
    
  def incompletos(self):                                             
    columnas_verificar = ["No. identidad", "Nombre", "Edad", "Meses"]
  
    filas_nulos = self.base_personas[self.base_personas[columnas_verificar].isnull().any(axis=1)]

    cantidad_filas_nulas = len(filas_nulos)

    return cantidad_filas_nulas

  def promedio_pagos(self):
    pagos = self.base_personas["Valor_acomulado"].sum()
    promedio = pagos/len(self.base_personas["Valor_acomulado"])
    return promedio
    
  def actividad_mas_demandada(self):
    actividad = max(self.base_facturacion["Actividad"].value_counts().tolist())
    return actividad
  
  def mas_paga(self):
      archivo_existe = os.path.isfile(self.base_personas)
      if archivo_existe==True:
        pagos =  max(self.base_personas["Valor acomulado"].tolist())
        return pagos
      else:
        messagebox.showerror("Error", "El archivo no existe")
  
  