import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


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
                messagebox.showerror("Error", arc_inexistente)
        
        except IndexError:
            messagebox.showerror("Error", "El usuario no existe")###

###############################################################################################
    def editar_usuario(self):
        try:        
            archivo_existe = os.path.isfile(self.base_personas)
            buscar = self.buscar
            if archivo_existe==True:
            
                data = pd.read_csv(self.base_personas)
                data["No. identidad"] = data["No. identidad"].astype(str)
                data["Edad"] = data["Edad"].astype(str)
                indice = data['No. identidad']==buscar
                data.loc[indice, 'Nombre'] = self.nombre_de_buscado
                data.loc[indice, 'Edad'] = self.edad_de_buscado
                data.to_csv(self.base_personas, index=False)

            else:
                arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
                messagebox.showerror("Error", arc_inexistente)

        except IndexError:
                messagebox.showerror("Error", "El proyecto no existe")

#################################################################################################

    def elim_usuario(self):

        try:
            buscar = self.buscar
            archivo_existe = os.path.isfile(self.base_personas) and os.path.isfile(self.base_facturacion)

            if archivo_existe==True:
            
                data = pd.read_csv(self.base_personas)
                data_fac = pd.read_csv(self.base_facturacion)

                data["No. identidad"] = data["No. identidad"].astype(str)
                data_fac["No. de identidad"] = data_fac["No. de identidad"].astype(str)

                indice = data[data['No. identidad']==buscar].index[0]
                indice_fac = data_fac[data_fac['No. de identidad']==buscar].index.tolist()

                data.drop(index=indice, inplace=True)
                for i in indice_fac:
                    data_fac.drop(index=i, inplace=True)

                data.to_csv(self.base_personas, index=False)
                data_fac.to_csv(self.base_facturacion, index=False)

            else:
                arc_inexistente="El archivo no se ha creado aún. Registre al menos un usuario"
                messagebox.showerror("Error", arc_inexistente)        

        except IndexError:
                messagebox.showerror("Error", "El usuario no existe")