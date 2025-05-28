import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


                    ################################ TRABAJAR CON REGISTROS #################################################

class usuario():
   def _init_(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado):
        
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

#----Referencia de ingredientes necesarios de la clase:-----#
#base_personas = "base_de_usuarios.csv" (en otro archivo: interfaz.py)
#base_facturacion="base_de_facturaciones.csv" (en otro archivo: Interfaz.py)

#def _init_(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado)
        
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
                arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
            

        except IndexError:
                messagebox.showerror("Error", "El proyecto no existe")

#################################################################################################

#----Referencia de ingredientes necesarios de la clase:-----
#base_personas = "base_de_usuarios.csv" (en otro archivo: interfaz.py)
#base_facturacion="base_de_facturaciones.csv" (en otro archivo: Interfaz.py)

#def _init_(self, buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado)
        
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


            
            
            
           


