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
    
    DataFrame_facturacion = pd.read_csv(self.base_facturacion)   

    
    sns.set_theme(style="whitegrid")

    tabla_actividad=DataFrame_facturacion[DataFrame_facturacion['Actividad']=="RUMBA"]
    sin_duplicados_rumba=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=DataFrame_facturacion[DataFrame_facturacion['Actividad']=="SPINING"]
    sin_duplicados_spining=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=DataFrame_facturacion[DataFrame_facturacion['Actividad']=="FORTALECIMIENTO"]
    sin_duplicados_fortalecimiento=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")

    tabla_actividad=DataFrame_facturacion[DataFrame_facturacion['Actividad']=="FISIOTERAPIA"]
    sin_duplicados_fisioterapia=tabla_actividad.drop_duplicates(subset='No. de identidad', keep="first")


    df_rumba=pd.DataFrame(sin_duplicados_rumba)
    df_spining=pd.DataFrame(sin_duplicados_spining)
    df_fortalecimiento=pd.DataFrame(sin_duplicados_fortalecimiento)
    df_fisioterapia=pd.DataFrame(sin_duplicados_fisioterapia)
        
    valor_rumba = df_rumba['No. de identidad'].value_counts().sum()
    valor_spining = df_spining['No. de identidad'].value_counts().sum()
    valor_fortalecimiento = df_fortalecimiento['No. de identidad'].value_counts().sum()
    valor_fisioterapia = df_fisioterapia['No. de identidad'].value_counts().sum()

    diccionario_valores = {
        'Rumba': [valor_rumba],
        'Spinning': [valor_spining],
        'Fortalecimiento': [valor_fortalecimiento],
        'Fisioterapia': [valor_fisioterapia]
        }

    db = pd.DataFrame(diccionario_valores,index=["clase", "Inscritos"]).T
    #cantidad_clases = db[['Rumba', 'Spinning', 'Fortalecimiento', 'Fisioterapia']]
    colores_personalizados = ['#139bb3', '#fbab3b', '#5e60ab', '#f1574b'] 
    clases = ['Spinning','Fisioterapia','Rumba','Fortalecimiento']
    plt.figure(figsize=(3.85,2.76), dpi=100)
    grafico_pie = sns.barplot(data=db, x=clases, y="Inscritos", hue=clases, palette=colores_personalizados, edgecolor=None)
    plt.title("Usuarios por actividad", fontsize=12)
    
    plt.grid(axis='y', color='lightgray', linestyle='--', linewidth=0.7)
    plt.tick_params(axis='x', labelsize=9)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    figura=grafico_pie.get_figure()
    return pasar_a_pil(figura)
  
  ################################################### CIRCULAR ####################################################3
  
  def grafico_circular(self): 
    DataFrame_facturacion = pd.read_csv(self.base_facturacion)
    conteos_de_actividad = DataFrame_facturacion['Actividad'].value_counts()

    colores = ["#286fb7", "#36a24b", "#f79033", "#716ab0"]
    
    fig, ax = plt.subplots(figsize=(3.38, 2.76), dpi=100)  
    wedges, _ = ax.pie(conteos_de_actividad, 
            colors=colores[:len(conteos_de_actividad)],
            wedgeprops=dict(width=0.6),
            startangle=90)

    
    ax.legend(
        wedges,
        conteos_de_actividad.index, 
        title="",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
        fontsize=9,
        frameon=False)

    centro = plt.Circle((0, 0), 0.70, fc='white') 
    fig.gca().add_artist(centro)

    ax.axis('equal')
    plt.title("Inscripciones por actividad", fontsize=10)
    plt.tight_layout()

    return pasar_a_pil(fig)
  
  ############################################################################################################

  def total_usuarios(self):

    DataFrame_personas = pd.read_csv(self.base_personas)
    cantidad_total = DataFrame_personas['No. identidad'].count()
    return cantidad_total
    
  def incompletos(self):

    DataFrame_personas = pd.read_csv(self.base_personas)

    columnas_verificar = ["No. identidad", "Nombre", "Edad", "Meses"]
  
    filas_nulos = DataFrame_personas[DataFrame_personas[columnas_verificar].isnull().any(axis=1)]
    cantidad_filas_nulas = len(filas_nulos)

    return cantidad_filas_nulas

  def promedio_pagos(self):

    DataFrame_personas = pd.read_csv(self.base_personas)
    promedio = DataFrame_personas["Monto acumulado"].mean()
    
    return round(promedio, 1)
    
  def actividad_mas_demandada(self):   
    
    DataFrame_facturacion = pd.read_csv(self.base_facturacion)
    conteo = DataFrame_facturacion["Actividad"].value_counts()
    actividad_mas_inscrita = conteo.idxmax() 
    actividad = actividad_mas_inscrita

    return actividad
  
  def mas_paga(self):      
      
      archivo_existe = os.path.isfile(self.base_personas)
      if archivo_existe==True:
        DataFrame_personas = pd.read_csv(self.base_personas)
        pagos =  max(DataFrame_personas["Monto acumulado"].tolist())
        return pagos
      else:
        messagebox.showerror("Error", "El archivo no existe")