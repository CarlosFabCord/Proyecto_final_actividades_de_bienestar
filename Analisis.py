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
    sns.barplot(data= db, x= clases , y= cantidad_clases)
    plt.title("Grafico de usuarios por clase", fontsize=7)
    plt.xlabel(clases, fontsize=6)
    plt.ylabel(cantidad_clases, fontsize=6)
    plt.tick_params(axis='x', labelsize=6)

  def grafico_circular(self): 
    
    colores = ["red","green", "blue", "yellow"]
    plt.pie(self.base_facturacion['Actividad'], labels=self.base_facturacion['Actividad'].index, colors=colores, shadow=True, textprops={'fontsize':6})
    plt.title("Inscripciones por actividad")

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