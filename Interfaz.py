from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import os
import tkinter as tk
from tkinter import messagebox
import csv
import os
from tkinter.scrolledtext import ScrolledText
import Logica as log
from PIL import ImageTk, Image
import Analisis as an

######################### PRELIMINARES ###############################################

base_facturacion="base_de_facturaciones.csv"
base_personas = "base_de_usuarios.csv"
no_de_identidad = [] ####
actividad = []
Cant_actividad = []


############################ REGISTRAR USUARIO ###########################################

def reg_usuario():

    
    num_identidad = str(id_usuario.get())
    nombre = nombre_usuario.get()
    edad = edad_usuario.get()
    meses = meses_usuario.get()



    fila = {
        'No. identidad': num_identidad,
        'Nombre': nombre,
        'Edad': edad,
        'Meses': meses,
        'Monto acumulado': 0
    }


    # Verificar si ya existe el archivo
    archivo_existe = os.path.isfile(base_personas)

    with open(base_personas, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe:
            escritor.writeheader()
        escritor.writerow(fila)
        
    id_usuario.set("")
    nombre_usuario.set("")
    edad_usuario.set("")
    meses_usuario.set("")


######################### BOTÓN DE GUARDAR ##################################

def guardar():
    global no_de_identidad
    global actividad
    global Cant_actividad

    no_de_identidad.append(cedula_usuario_fact.get())
    actividad.append(lista_actividad.get())
    Cant_actividad.append(cant_actividad.get())

########################### BOTÓN DE ENVIAR ################################


def enviar():
    global no_de_identidad
    global actividad
    global Cant_actividad
  
    archivo_existe = os.path.isfile(base_personas)
                                  
    if not archivo_existe:
        messagebox.showwarning("Error", "No hay registros aún")
    else:
        while True:
            df = pd.read_csv(base_personas)
            num_identidad = cedula_usuario_fact.get()
          
            try: 
                #Acumula el costo y los meses al archivo base personas:             
                df['No. identidad'] = df['No. identidad'].astype(str)
                indice = df['No. identidad']==num_identidad
                df.loc[indice, 'Meses']+=1
                

                clases_spinning = 7000
                clases_fisioterapia = 10000
                clases_rumba = 5000
                clases_forta = 6500              
                
                calcular_total = 0

                for i in range(len(actividad)):
                    if actividad[i] == 'Fisioterapia':
                        calcular_total += (Cant_actividad[i]*clases_fisioterapia)
                    elif actividad[i] == 'Spinning':
                        calcular_total += (Cant_actividad[i]*clases_spinning)
                    elif actividad[i] == 'Rumba':
                        calcular_total += (Cant_actividad[i]*clases_rumba)
                    else:
                        calcular_total += (Cant_actividad[i]*clases_forta)                    

                
                etiqueta_total.set(calcular_total)

                df.loc[indice, 'Monto acumulado']+=calcular_total
                df.to_csv(base_personas, index=False)

                #Aquí identifica existencia de archivo facturación y añade diccionario de fila a csv

                fila = {
                            'No. de identidad': [],
                            'Actividad': [],
                            'Cant. Actividad': [],                            
                        }

                archivo_existe = os.path.isfile(base_facturacion)

                with open(base_facturacion, 'a', newline='') as f: ###############
                    escritor = csv.DictWriter(f, fieldnames=fila.keys())
                    if not archivo_existe:
                        escritor.writeheader()

                    for i in range(len(no_de_identidad)):
                        fila = {
                            'No. de identidad': no_de_identidad[i],
                            'Actividad': actividad[i],
                            'Cant. Actividad': Cant_actividad[i],                            
                        }

                        escritor.writerow(fila)  

                no_de_identidad.clear()
                actividad.clear()
                Cant_actividad.clear()     
              
                break
            except:
                messagebox.showwarning("Error", "Este usuario aun no se ha registrado")
                continue
          
##################################### BOTON DE VER USUARIO ###########################################
#Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def ver_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()
    
    
    #hace:

    lista=log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).mostrar_registro()#################3---------#######

    nombre_usuario.set(lista[1])#----
    edad_usuario.set(lista[2])#----
    meses_usuario.set(lista[3])#---

################################ BOTON MODIFICAR USUARIO ###########################################################
 
 #Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def modificar_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()

    #hace:
    
    log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).editar_usuario()

######################################### BOTON DE ELIMINAR #######################################
#Ingredientes
#base_facturacion="base_de_facturaciones.csv"
#base_personas = "base_de_usuarios.csv"

def eliminar_usuario():
    
    #recoge:

        #externos:
    global base_personas
    global base_facturacion

    buscar=id_usuario.get()
    nombre_de_buscado= nombre_usuario.get()
    edad_de_buscado= edad_usuario.get()

    #hace:
    
    log.usuario(buscar, base_personas, base_facturacion, nombre_de_buscado, edad_de_buscado).elim_usuario()




################################### BOTÓN GENERAR LISTADO ################################################

def abrir_ventana_secundaria(): #######------#######
    archivo_existe = os.path.isfile(base_facturacion)
        
    if archivo_existe==True:
         
        df = pd.read_csv(base_personas)
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Datos de usuario")
        nueva_ventana.geometry("800x400")
        tk.Label(nueva_ventana, text="Inforamción Usuarios").pack(pady=20)

        text_area = ScrolledText(nueva_ventana, width= 90, height= 15)
        text_area.pack()

        text_area.delete("1.0",tk.END)
        text_area.insert(tk.END, df)
    
        tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack()
    else:
        arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
        messagebox.showerror("Error", arc_inexistente)

    

############################### BOTÓN DE ACTUALIZAR ######################################################

def actualizar():

    global base_personas,base_facturacion   

    grafico_derecha = an.Analisis(base_personas,base_facturacion).grafico_circular() #grafíco izquierda
    mostrar_imagenes_graf_2(grafico_derecha)

    incompletos = an.Analisis(base_personas,base_facturacion).incompletos()  
    data_incomp.set(incompletos)

    cliente_max_paga = an.Analisis(base_personas,base_facturacion).mas_paga()
    user_etiq_max.set(cliente_max_paga)

    act_mas_demandada = an.Analisis(base_personas, base_facturacion).actividad_mas_demandada()
    mas_demanda.set(act_mas_demandada)

    total_usuarios_fun = an.Analisis(base_personas,base_facturacion).total_usuarios()
    user_total.set(total_usuarios_fun)

    prome_de_pagos=an.Analisis(base_personas, base_facturacion).promedio_pagos()
    data_prom.set(prome_de_pagos)

    grafico_izquierda = an.Analisis(base_personas,base_facturacion).graficar_barras() #grafico derecha
    mostrar_imagenes_graf_1(grafico_izquierda)

       



    

def mostrar_imagenes_graf_1(pil_img):
  image_tk = ImageTk.PhotoImage(pil_img)
  imagen_de_grafico1.configure(image=image_tk)
  imagen_de_grafico1.image = image_tk 


def mostrar_imagenes_graf_2(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    imagen_de_grafico2.configure(image=image_tk)
    imagen_de_grafico2.image = image_tk




##############################################################################################################################

                                                        #INTERFAZ

###############################################################################################################################

#etiquetas que faltan
#user_total --
#user_etiq_max --
#boton_imprimir_usuarios ¿¿¿¿¿¿¿
#data_incomp--
#etiqueta_total--
#los cuadros de texto de usuarios aun no devuelve los valores que debe mostrar al hacerle ver usuario

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

boton_actualizar_reporte = tk.Button(fra_ter_der_int, text="Actualizar", command=actualizar, font=("Calibri", 13), width=12)##
boton_actualizar_reporte.place(y=47, x=96)

fra_ter_izq_int=tk.Frame(frame_tercero_izquierda, bg="white", width=385, height=89)
fra_ter_izq_int.place(x=31, y=0)

etiq_user_max_pago = tk.Label(fra_ter_izq_int, bg="white", text="Usuario que más ha pagado:", font=("Calibri", 9, "bold") )
etiq_user_max_pago.place(y=14, x=21)

user_etiq_max = tk.IntVar()
user_etiq_max_label=tk.Label(fra_ter_izq_int, bg="white", text="", textvariable=user_etiq_max, font= ("Calibri", 20, "bold") )
user_etiq_max_label.place(x=172, y=29)

#################### Frame segundo

frame_segundo= tk.Frame(reporte_frame, bg="#eff1f3", width=800, height=294)
frame_segundo.place(x=0, y=172)

frame_segundo_izquierda = tk.Frame(frame_segundo, width=425, height=294)
frame_segundo_izquierda.place(x=0, y=0)

frame_segundo_derecha = tk.Frame(frame_segundo, width=375, height=294)
frame_segundo_derecha.place(x=424, y=0)

fra_seg_izq_int= tk.Frame(frame_segundo_izquierda, bg="white", width=385, height=276)
fra_seg_izq_int.place(x=31, y=9)

imagen_de_grafico1= tk.Label(fra_seg_izq_int, bg="white")###########
imagen_de_grafico1.place(x=0, y=0)

fra_seg_der_int= tk.Frame(frame_segundo_derecha, bg="white", width=338, height=276)
fra_seg_der_int.place(x=8, y=9)

imagen_de_grafico2= tk.Label(fra_seg_der_int, bg="white")############
imagen_de_grafico2.place(x=0, y=0)

################################### FRAME PRIMERO

frame_primero= tk.Frame(reporte_frame, bg="#eff1f3", width=800, height=189)
frame_primero.place(x=0, y=0)

#######################################################################################

icono_pil_1 = Image.open("total_usuarios_logo.png").resize((60, 50), Image.Resampling.LANCZOS)
imagen_tk1 = ImageTk.PhotoImage(icono_pil_1)
etiqueta_logo1 = tk.Label(reporte_frame, image=imagen_tk1, bg="white")
etiqueta_logo1.image = imagen_tk1 
etiqueta_logo1.place(x=94, y=46)

icono_pil_2 = Image.open("datos_incompletos_logo.png").resize((60, 50), Image.Resampling.LANCZOS)
imagen_tk2 = ImageTk.PhotoImage(icono_pil_2)
etiqueta_logo2 = tk.Label(reporte_frame, image=imagen_tk2, bg="white")
etiqueta_logo2.image = imagen_tk1 
etiqueta_logo2.place(x=295, y=46)

icono_pil_3 = Image.open("pago_promedio_logo.png").resize((60, 50), Image.Resampling.LANCZOS)
imagen_tk3 = ImageTk.PhotoImage(icono_pil_3)
etiqueta_logo3 = tk.Label(reporte_frame, image=imagen_tk3, bg="white")
etiqueta_logo3.image = imagen_tk3 
etiqueta_logo3.place(x=491, y=46)

icono_pil_4 = Image.open("actividad_mas_demandada_logo.png").resize((60, 50), Image.Resampling.LANCZOS)
imagen_tk4 = ImageTk.PhotoImage(icono_pil_4)
etiqueta_logo4 = tk.Label(reporte_frame, image=imagen_tk4, bg="white")
etiqueta_logo4.image = imagen_tk4 
etiqueta_logo4.place(x=672, y=46)

#######################################################################################

frame_sup_1 = tk.Frame(frame_primero, bg="white", width=185, height=158)
frame_sup_1.place(x=31, y=15)

etiq_usuar_totales = tk.Label(frame_primero, bg="white", text="Usuarios totales", font=("Calibri", 11, "bold"))
etiq_usuar_totales.place(x=67, y=107)

user_total = tk.IntVar()
user_etiq_max_label=tk.Label(frame_primero, bg="white", textvariable=user_total, font= ("Calibri", 18, "bold") ) ########
user_etiq_max_label.place(x=70, y=128)

frame_sup_2 = tk.Frame(frame_primero, bg="white", width=185, height=158)
frame_sup_2.place(x=231, y=15)

etiq_incomp_data = tk.Label(frame_primero, bg="white", text="Datos incompletos", font=("Calibri", 11, "bold"))
etiq_incomp_data.place(x=256 , y=107)

data_incomp = tk.IntVar()
user_etiq_data_incompl=tk.Label(frame_primero, bg="white", textvariable=data_incomp, font= ("Calibri", 18, "bold") ) ########
user_etiq_data_incompl.place(x=259, y=128)

frame_sup_3 = tk.Frame(frame_primero, bg="white", width=173, height=158)
frame_sup_3.place(x=433, y=15)

etiq_pago_promedio = tk.Label(frame_primero, bg="white", text="Pago promedio", font=("Calibri", 11, "bold"))
etiq_pago_promedio.place(x=462, y=107)

data_prom = tk.DoubleVar()
user_etiq_prom=tk.Label(frame_primero, bg="white", textvariable=data_prom, font= ("Calibri", 18, "bold") )  #########
user_etiq_prom.place(x=465, y=128)

frame_sup_4 = tk.Frame(frame_primero, bg="white", width=148, height=158)
frame_sup_4.place(x=623, y=15)

etiq_mas_demandada = tk.Label(frame_primero, bg="white", text="Más demandada", font=("Calibri", 11, "bold"))
etiq_mas_demandada.place(x=644, y=107)

mas_demanda = tk.StringVar()
mas_demanda_etiq=tk.Label(frame_primero, bg="white", textvariable=mas_demanda, font=("Calibri", 16, "bold") )  ##########
mas_demanda_etiq.place(x=644,y=126)


###NOTA IMPORTANTE: Se necesita algo que inicialice la función para que aparezca el gráfico y todas las demás funciones relacionadas a etiquetas


# Usuarios ###############################################################################################

usuarios_frame = tk.Frame(marco_contenido, bg="#eff1f3")

marco_usuario = tk.LabelFrame(usuarios_frame, text="Ingreso Usuario", width=697, height=333, font=("Verdana", 11, "bold"))
marco_usuario.place(x=40, y=37)

id_usuario = tk.StringVar()
entrada_identidad_entry = tk.Entry(marco_usuario, textvariable=id_usuario, width=60, font=("helvetica", 10))
entrada_identidad_entry.place(x=176, y=41)

nombre_usuario = tk.StringVar()
entrada_nombre_us_entry = tk.Entry(marco_usuario, textvariable=nombre_usuario, width=60, font=("helvetica", 10))
entrada_nombre_us_entry.place(x=176, y=91)

edad_usuario = tk.StringVar()
entrada_edad_us_entry = tk.Entry(marco_usuario, textvariable=edad_usuario, width=60, font=("helvetica", 10))
entrada_edad_us_entry.place(x=176, y=142)

meses_usuario = tk.IntVar()
entrada_meses_us_entry = tk.Entry(marco_usuario, textvariable=meses_usuario, width=60, font=("helvetica", 10))
entrada_meses_us_entry.place(x=176, y=192)

etiq_cedula=tk.Label(marco_usuario, text="Cédula:", font=("calibri", 10))
etiq_cedula.place(x=102, y=40)

etiq_nombre=tk.Label(marco_usuario, text="Nombre de usuario:", font=("calibri", 10))
etiq_nombre.place(x=35, y=87)

etiq_edad=tk.Label(marco_usuario, text="Edad:", font=("calibri", 10))
etiq_edad.place(x=115, y=141)

etiq_meses=tk.Label(marco_usuario, text="Meses:", font=("calibri", 10))
etiq_meses.place(x=105, y=190)

bot_ver_usuario = tk.Button(usuarios_frame, text="Ver usuario", command=ver_usuario, font=("Calibri", 13), width=12)
bot_ver_usuario.place(x=595, y=392)
bot_registrar_usuario=tk.Button(usuarios_frame, text="Registrar", command=reg_usuario, font=("Calibri", 13), width=12)
bot_registrar_usuario.place(x=595, y=442)
bot_modificar_usuario=tk.Button(usuarios_frame, text="Modificar", command=modificar_usuario, font=("Calibri", 13), width=12)
bot_modificar_usuario.place(x=595, y=492)
bot_eliminar_usuario=tk.Button(usuarios_frame, text="Eliminar", command=eliminar_usuario, font=("Calibri", 13), width=12)
bot_eliminar_usuario.place(x=595, y=543)


# Facturacion ############################################################################################

facturacion_frame = tk.Frame(marco_contenido, bg="#eff1f3")

marco_facturacion = tk.LabelFrame(facturacion_frame, text="Facturación", width=697, height=333, font=("Verdana", 11, "bold"))
marco_facturacion.place(x=40, y=37)

cedula_usuario_fact = tk.StringVar()
entrada_cedula_entry = tk.Entry(marco_facturacion, width=60, textvariable=cedula_usuario_fact, font=("helvetica", 10))
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

etiq_cantidad=tk.Label(marco_facturacion, text="Cantidad:", font=("calibri", 10))
etiq_cantidad.place(x=350, y=101)


bot_guardar = tk.Button(facturacion_frame, text="Guardar", command=guardar, font=("Calibri", 13), width=12)
bot_guardar.place(x=595, y=392)
bot_enviar=tk.Button(facturacion_frame, text="Enviar", command=enviar, font=("Calibri", 13), width=12)
bot_enviar.place(x=595, y=442)


etiqueta_total = tk.IntVar()
etiqueta_total_label=tk.Label(facturacion_frame, bg="#eff1f3", text="prueba", textvariable=etiqueta_total, font= ("Calibri", 30, "bold") ) #######
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