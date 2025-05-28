import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk
from tkinter import messagebox
import random
import math
import csv
import os
import io
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

#etiquetas que faltan
#user_total
#user_etiq_max
#boton_imprimir_usuarios
#data_incomp

base_personas = "base_de_usuarios.csv" ###temporal aquí

def abrir_ventana_secundaria():
 
    df = pd.read_csv(base_personas)
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Datos de usuario")
    nueva_ventana.geometry("600x400")
    tk.Label(nueva_ventana, text="Inforamción Usuarios").pack(pady=20)

    text_area = ScrolledText(nueva_ventana, width= 70, height= 15)
    text_area.pack()

    text_area.delete("1.0",tk.END)
    text_area.insert(tk.END, df)
    
    tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack()

def prueba_botones():
    print("funciona")

from PIL import ImageTk
def mostrar_imagenes_graf_1(pil_img):
  image_tk = ImageTk.PhotoImage(pil_img)
  imagen_de_grafico1.configure(image=image_tk)
  imagen_de_grafico1.image = image_tk 

def mostrar_imagenes_graf_2(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    imagen_de_grafico2.configure(image=image_tk)
    imagen_de_grafico2.image = image_tk


ventana = tk.Tk() ##ventana
ventana.title("Gestor de actividades físicas")
ventana.geometry("1000x600")
ventana.configure(bg="#f0f0f0")
ventana.resizable(False, False)

#panel de navegación ###########################################################################
panel_de_navegacion = tk.Frame(ventana, bg="#08197a", width=200, height=600)
panel_de_navegacion.pack(side=tk.LEFT, fill=tk.Y) #tk.Y hace que se expanda y rellene su frame contenedor de manera vertical
panel_de_navegacion.pack_propagate(False)

titulo_panel_nav = tk.Label(panel_de_navegacion, text="Bienestar", bg="#08197a", fg="#e07c29", font=("Verdana", 20, "bold"))
titulo_panel_nav.pack(pady=20) #pady es un margen vertical desde la esquina superior del marco (frame) que lo contiene y dado en píxeles

titulo_panel_nav2 = tk.Label(panel_de_navegacion, text="Por un futuro más saludable", bg="#08197a", fg="#e07c29", font=("Verdana", 7, "bold"))
titulo_panel_nav2.place(x=28, y=50)

# área de contenido ############################################################################
marco_contenido = tk.Frame(ventana, bg="white", width=800, height=600)
marco_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
marco_contenido.pack_propagate(False)



#FRAMES

# Reporte ##############################################################################################
reporte_frame = tk.Frame(marco_contenido, bg="#eff1f3", width=800, height=600)

############################# FRAME TERCERO

frame_tercero = tk.Frame(reporte_frame, bg="#eff1f3", width=800, height=118)
frame_tercero.place(x=0, y=482)

frame_tercero_izquierda = tk.Frame(frame_tercero, width=425, height=118)
frame_tercero_izquierda.place(x=0, y=0)

frame_tercero_derecha = tk.Frame(frame_tercero, width=375, height=120)
frame_tercero_derecha.place(x=424, y=0)

fra_ter_der_int= tk.Frame(frame_tercero_derecha, bg="white", width=334, height=89)
fra_ter_der_int.place(x=8, y=0)

boton_imprimir_usuarios = tk.Button(fra_ter_der_int, text="Generar listado", command=abrir_ventana_secundaria, font=("Calibri", 13), width=12)##
boton_imprimir_usuarios.place(y=4, x=96)

boton_actualizar_reporte = tk.Button(fra_ter_der_int, text="Actualizar", command=prueba_botones, font=("Calibri", 13), width=12)##
boton_actualizar_reporte.place(y=47, x=96)

fra_ter_izq_int=tk.Frame(frame_tercero_izquierda, bg="white", width=385, height=89)
fra_ter_izq_int.place(x=31, y=0)

etiq_user_max_pago = tk.Label(fra_ter_izq_int, bg="white", text="Usuario que más ha pagado:", font=("Calibri", 9, "bold") )
etiq_user_max_pago.place(y=14, x=21)

user_etiq_max = tk.IntVar()
user_etiq_max_label=tk.Label(fra_ter_izq_int, bg="white", text="prueba", textvariable=user_etiq_max, font= ("Calibri", 20, "bold") )
user_etiq_max_label.place(x=172, y=29)

user_etiq_max.set("1130619640") ####para retirar

#################### Frame segundo

frame_segundo= tk.Frame(reporte_frame, bg="#eff1f3", width=800, height=294)
frame_segundo.place(x=0, y=172)

frame_segundo_izquierda = tk.Frame(frame_segundo, width=425, height=294)
frame_segundo_izquierda.place(x=0, y=0)

frame_segundo_derecha = tk.Frame(frame_segundo, width=375, height=294)
frame_segundo_derecha.place(x=424, y=0)

fra_seg_izq_int= tk.Frame(frame_segundo_izquierda, bg="white", width=385, height=276)
fra_seg_izq_int.place(x=31, y=9)

imagen_de_grafico1= tk.Label(fra_seg_izq_int, bg="white")
imagen_de_grafico1.place(x=0, y=0)

fra_seg_der_int= tk.Frame(frame_segundo_derecha, bg="white", width=338, height=276)
fra_seg_der_int.place(x=8, y=9)

imagen_de_grafico2= tk.Label(fra_seg_der_int, bg="white")
imagen_de_grafico1.place(x=0, y=0)

################################### FRAME PRIMERO

frame_primero= tk.Frame(reporte_frame, bg="#eff1f3", width=800, height=189)
frame_primero.place(x=0, y=0)

frame_sup_1 = tk.Frame(frame_primero, bg="white", width=185, height=158)
frame_sup_1.place(x=31, y=15)

etiq_usuar_totales = tk.Label(frame_primero, bg="white", text="Usuarios totales", font=("Calibri", 11, "bold"))
etiq_usuar_totales.place(x=67, y=107)

user_total = tk.IntVar()
user_etiq_max_label=tk.Label(frame_primero, bg="white", textvariable=user_etiq_max, font= ("Calibri", 18, "bold") ) ########
user_etiq_max_label.place(x=70, y=128)

frame_sup_2 = tk.Frame(frame_primero, bg="white", width=185, height=158)
frame_sup_2.place(x=231, y=15)

etiq_incomp_data = tk.Label(frame_primero, bg="white", text="Datos incompletos", font=("Calibri", 11, "bold"))
etiq_incomp_data.place(x=256 , y=107)

data_incomp = tk.IntVar()
user_etiq_data_incompl=tk.Label(frame_primero, bg="white", textvariable=user_etiq_max, font= ("Calibri", 18, "bold") ) ########
user_etiq_data_incompl.place(x=259, y=128)

frame_sup_3 = tk.Frame(frame_primero, bg="white", width=173, height=158)
frame_sup_3.place(x=433, y=15)

etiq_pago_promedio = tk.Label(frame_primero, bg="white", text="Pago promedio", font=("Calibri", 11, "bold"))
etiq_pago_promedio.place(x=462, y=107)

data_prom = tk.IntVar()
user_etiq_prom=tk.Label(frame_primero, bg="white", textvariable=user_etiq_max, font= ("Calibri", 18, "bold") )  #########
user_etiq_prom.place(x=465, y=128)

frame_sup_4 = tk.Frame(frame_primero, bg="white", width=148, height=158)
frame_sup_4.place(x=623, y=15)

etiq_mas_demandada = tk.Label(frame_primero, bg="white", text="Más demandada", font=("Calibri", 11, "bold"))
etiq_mas_demandada.place(x=644, y=107)

mas_demanda = tk.IntVar()
mas_demanda_etiq=tk.Label(frame_primero, bg="white", textvariable=user_etiq_max, font= ("Calibri", 18, "bold") )  ##########
mas_demanda_etiq.place(x=643, y=128)


###NOTA IMPORTANTE: Se necesita algo que inicialice la función para que aparezca el gráfico y todas las demás funciones relacionadas a etiquetas


# Usuarios ###############################################################################################

usuarios_frame = tk.Frame(marco_contenido, bg="#eff1f3")

marco_usuario = tk.LabelFrame(usuarios_frame, text="Ingreso Usuario", width=697, height=333, font=("Verdana", 11, "bold"))
marco_usuario.place(x=40, y=37)

id_usuario = tk.IntVar()
entrada_identidad_entry = tk.Entry(marco_usuario, textvariable=id_usuario, width=60, font=("helvetica", 10))
entrada_identidad_entry.place(x=176, y=41)

nombre_usuario = tk.StringVar()
entrada_nombre_us_entry = tk.Entry(marco_usuario, textvariable=nombre_usuario, width=60, font=("helvetica", 10))
entrada_nombre_us_entry.place(x=176, y=91)

edad_usuario = tk.StringVar()
entrada_edad_us_entry = tk.Entry(marco_usuario, textvariable=edad_usuario, width=60, font=("helvetica", 10))
entrada_edad_us_entry.place(x=176, y=142)

meses_usuario = tk.StringVar()
entrada_meses_us_entry = tk.Entry(marco_usuario, textvariable=meses_usuario, width=60, font=("helvetica", 10))
entrada_meses_us_entry.place(x=176, y=192)

etiq_cedula=tk.Label(marco_usuario, text="Cédula:", font=("calibri", 10))
etiq_cedula.place(x=102, y=50)

etiq_nombre=tk.Label(marco_usuario, text="Nombre de usuario:", font=("calibri", 10))
etiq_nombre.place(x=30, y=103)

etiq_edad=tk.Label(marco_usuario, text="Edad:", font=("calibri", 10))
etiq_edad.place(x=115, y=156)

etiq_meses=tk.Label(marco_usuario, text="Meses:", font=("calibri", 10))
etiq_meses.place(x=105, y=205)

bot_ver_usuario = tk.Button(usuarios_frame, text="Ver usuario", command=prueba_botones, font=("Calibri", 13), width=12)
bot_ver_usuario.place(x=595, y=392)
bot_registrar_usuario=tk.Button(usuarios_frame, text="Registrar", command=prueba_botones, font=("Calibri", 13), width=12)
bot_registrar_usuario.place(x=595, y=442)
bot_modificar_usuario=tk.Button(usuarios_frame, text="Modificar", command=prueba_botones, font=("Calibri", 13), width=12)
bot_modificar_usuario.place(x=595, y=492)
bot_eliminar_usuario=tk.Button(usuarios_frame, text="Eliminar", command=prueba_botones, font=("Calibri", 13), width=12)
bot_eliminar_usuario.place(x=595, y=543)


# Facturacion ############################################################################################

facturacion_frame = tk.Frame(marco_contenido, bg="#eff1f3")

marco_facturacion = tk.LabelFrame(facturacion_frame, text="Facturación", width=697, height=333, font=("Verdana", 11, "bold"))
marco_facturacion.place(x=40, y=37)

cedula_usuario = tk.IntVar()
entrada_cedula_entry = tk.Entry(marco_facturacion, width=60, textvariable=id_usuario, font=("helvetica", 10))
entrada_cedula_entry.place(x=176, y=41)

lista_actividad = tk.StringVar() #es la lista
lista_actividad_entry = ttk.Combobox(marco_facturacion, textvariable=lista_actividad)
lista_actividad_entry.configure(values = ("RUMBA", "FISIOTERAPIA", "SPINING", "FORTALECIMIENTO"))
lista_actividad_entry.place(x=176, y=101)
lista_actividad_entry.current(0)

etiq_cedula=tk.Label(marco_facturacion, text="Cédula:", font=("calibri", 10))
etiq_cedula.place(x=102, y=50)

etiq_actividad=tk.Label(marco_facturacion, text="Actividad:", font=("calibri", 10))
etiq_actividad.place(x=87, y=103)

cant_actividad = tk.IntVar()
entrada_cantidad_entry = tk.Entry(marco_facturacion, width=20, textvariable=cant_actividad, font=("helvetica", 10))
entrada_cantidad_entry.place(x=453, y=101)

etiq_cantidad=tk.Label(marco_facturacion, text="Cantidad:", font=("calibri", 10), width=20)
etiq_cantidad.place(x=358, y=101)


bot_guardar = tk.Button(facturacion_frame, text="Guardar", command=prueba_botones, font=("Calibri", 13), width=12)
bot_guardar.place(x=595, y=392)
bot_enviar=tk.Button(facturacion_frame, text="Enviar", command=prueba_botones, font=("Calibri", 13), width=12)
bot_enviar.place(x=595, y=442)


etiqueta_total = tk.IntVar()
etiqueta_total_label=tk.Label(facturacion_frame, bg="#eff1f3", text="prueba", textvariable=user_etiq_max, font= ("Calibri", 30, "bold") ) #######
etiqueta_total_label.place(x=102, y=392)

etiqueta_pesos = tk.Label(facturacion_frame, bg="#eff1f3", text="$", font= ("Calibri", 30, "bold"))
etiqueta_pesos.place(x=80,y=392)

etiq_debe_pagar = tk.Label(facturacion_frame, bg="#eff1f3", text="Total a pagar", font= ("Calibri", 15, "bold"))
etiq_debe_pagar.place(x=80, y=435)

#Conmutador #############################################################################################33


lista_nombres_frames = ["Reporte", "Usuarios", "Facturacion"]

nombres_de_frames = {
    "Reporte": reporte_frame,
    "Usuarios": usuarios_frame,
    "Facturacion": facturacion_frame
}

def conmutador(lista_nombres_frames):
    for frame in nombres_de_frames.values(): 
        frame.pack_forget()

    nombres_de_frames[lista_nombres_frames].pack(fill=tk.BOTH, expand=True) #fill=tk.BOTH, expand=True
    nombres_de_frames[lista_nombres_frames].pack_propagate()
    
    #fin

for name in lista_nombres_frames:
    button = tk.Button(panel_de_navegacion, text=name, bg="#34495e", fg="white", 
                       activebackground="#27b18e", activeforeground="white", 
                       relief=tk.FLAT, font=("calibri", 14), padx=10, pady=10, 
                       command=lambda n=name: conmutador(n))
    button.pack(fill=tk.X, padx=10, pady=5)


conmutador("Reporte")

ventana.mainloop()