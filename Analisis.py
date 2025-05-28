import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns

class graficos:
  def init(self, data_frame):
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