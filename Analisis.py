import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns


                    ################################ TRABAJAR CON REGISTROS #################################################

class usuario():
   def __init__(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado):
        
        self.buscar=buscar
        self.base_personas=base_personas
        self.base_facturacion=base_facturacion
        self.nombre_de_buscado=nombre_de_buscado
        self.edad_de_buscado=edad_de_buscado
        

####################################################################################################

   def mostrar_registro(self):

    try:        
        archivo_existe = os.path.isfile(self.base_personas)
        if archivo_existe==True:
           data = pd.read_csv(self.base_personas) #en mi caso lo convertiría en diccionario
           data["No. identidad"] = data["No. identidad"].astype(str)
           uni_fila=data[data['No. identidad']==self.buscar]
           lista=uni_fila.values.tolist()[0]
           return lista
        
        else:
           arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
           

    except IndexError:
      messagebox.showerror("Error", "El usuario no existe")###

###############################################################################################


#def __init__(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado)
        
        #self.buscar=buscar
        #self.base_personas=base_personas
        #self.base_facturacion=base_facturacion
        #self.nombre_de_buscado=nombre_de_buscado
        #self.edad_de_buscado=edad_de_buscado


def editar_datos(self):

        try:        
            archivo_existe = os.path.isfile(self.base_personas)
            
            if archivo_existe==True:
            
                data = pd.read_csv(self.base_personas)

                data["No. identidad"] = data["No. identidad"].astype(str)

                indice = data['No. identidad']==self.buscar

                data.loc[indice, 'Nombre'] = self.nombre_de_buscado
                data.loc[indice, 'Edad'] = self.edad_de_buscado

                data.to_csv(self.base_personas, index=False)

            else:
                arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
            

        except IndexError:
                messagebox.showerror("Error", "El usuario no existe")

#################################################################################################

#----Referencia de ingredientes necesarios de la clase:-----

#def init(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado)
        
        #self.buscar=buscar
        #self.base_personas=base_personas
        #self.base_facturacion=base_facturacion
        #self.nombre_de_buscado=nombre_de_buscado
        #self.edad_de_buscado=edad_de_buscado


def elim_usuario(self):
        
        try:

            archivo_existe = os.path.isfile(self.base_personas) and os.path.isfile(self.base_facturacion)

            if archivo_existe==True:
            
                data = pd.read_csv(self.base_personas)
                data_fac = pd.read_csv(self.base_facturacion)

                data["No. identidad"] = data["No. identidad"].astype(str)
                data_fac["No. identidad"] = data_fac["No. identidad"].astype(str)

                indice = data[data['No. identidad']==self.buscar].index
                indice_fac = data_fac[data_fac['No. identidad']==self.buscar].index

                data.drop(index=indice, inplace=True)
                data.drop(index=indice_fac, inplace=True)
                data.to_csv(self.base_personas, index=False)
                data.to_csv(self.base_facturacion, index=False)

            else:
                arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
            

        except IndexError:
                messagebox.showerror("Error", "El usuario no existe")

class Analisis():
  def __init__(self,base_personas,base_facturacion):
    self.base_personas=base_personas
    self.base_facturacion=base_facturacion


  def graficar_barras(self):

    cantidad_clases = self.base_facturacion['Clases Spinning','Clases Fisioterapia','Clases Rumba','Clases Fortalecimiento']
    clases = ['Spinning','Fisioterapia','Rumba','Fortalecimiento']
    grafico, ax = plt.subplots(1, 3, figsize=(9,3), dpi=100) 
    sns.barplot(data= self.df, x= clases , y= cantidad_clases, ax=ax[0])
    ax[0].set_title("Grafico de usuarios por clase", fontsize=7)
    ax[0].set_xlabel(clases, fontsize=6)
    ax[0].set_ylabel(cantidad_clases, fontsize=6)
    ax[0].tick_params(axis='x', labelsize=6)

    colores = ["red","green", "blue"]
    ax[1].pie(cantidad_clases, labels=cantidad_clases.index, colors=colores, shadow=True, textprops={'fontsize':6})
    ax[1].set_title("Inscripciones por actividad")
    grafico.tight_layout()   
    return pasar_a_pil(grafico)
  

  def total_usuarios(self):
    cantidad_total = self.df['No. identidad'].sum()
    return cantidad_total
    
  def incompletos(self):                                             
    columnas_verificar = ["No. identidad", "Nombre", "Edad", "Meses"]
  
    filas_nulos = self.df[self.df[columnas_verificar].isnull().any(axis=1)]

    cantidad_filas_nulas = len(filas_nulos)

    return cantidad_filas_nulas
    
  def promedio_pagos(self):
    pagos = self.df["Valor_acomulado"].sum()
    promedio = pagos/len(self.df["Valor_acomulado"])
    return promedio
    
  def actividad_mas_demandada(self):
    actividad = max(self.df["Actividad"].value_counts().tolist())
    return actividad