# Notepad
import os
import tkinter as tk # Este se usa para poder usar tk.END y definir el final de un objeto
from tkinter import Tk
from tkinter import Text
from tkinter import Button
from tkinter import filedialog
import os
# usamos pathActual para saber en que carpeta estamos, y usarla para abrir y guardar archivos
pathActual = os.path.dirname(os.path.abspath(__file__))

# Iniciar tkinter
root = Tk()
# Agregar titulo a la ventana
root.title("Notepad")
# Definir tamano de la ventanda en pixeles, horizontalXvertical
root.geometry("800x600")

# Se crea el Text donde se ingresara todo el text
textbox = Text(root,
               height=20,  # Tamano del contenido en altura
               width=70,  # Tamano del contenido en ancho
               background="#f2f2f2",  # Color del fondo (Gris claro, en hexadecimal)
               foreground="black",  # Color del texto
               font=("Helvetica", 18))  # Tamano de la letra y la fuente
# .pack() agrega el item a la vista
textbox.pack()


# Lee un archivo basado en la ubicacion que se le envie como parametro
def leer(filename):
    return open(filename, "r")

# Funcion para ponerle el focus al textinput
def focus():
    textbox.focus()

# Funcion para limpiar el contenido del text input
def limpiarTexto():
    textbox.delete("1.0", tk.END)

# Funcion para cargar archivo
def cargarArchivo():
    # lector va devolver un string con la ubicacion del archivo
    lector = filedialog.askopenfilename(
      initialdir=pathActual, # Donde abrira incialmente la ventana
      title="Seleccione el archivo .txt", # El titulo de la ventana
      filetypes=(("txt files", "*.txt"), ("all files", "*.*")) # Definimos los tipos de archivos a abrir como una tupla
    )
    # Si lector es vacio, significa que el usuario cerro la ventana o le dio cancel
    if lector is '': 
        return # No abrimos nada, solo terminamos la funcion haciendo un Return
    
    # Limpiamos el texto que exista en ese momento 
    limpiarTexto()
    # Leemos el contenido del archivo, lector nos da la ubicacion
    file = leer(lector)
    # Insertamos lo que leimos del archivo en el textbox
    textbox.insert(tk.END, file.read())

# Funcion para guardar el archivo
def guardarArchivo():
    # Se abre la ventana para decir donde guardar el nuevo archivo.
    # lector va a guardar la configuracion de donde guardar el archivo
    lector = filedialog.asksaveasfile(
      initialdir=pathActual, # Se define que carpeta abrira por defecto
      initialfile="nuevo.txt", # Se define el nombre inicial del archivo por defecto
      mode='w', # Se abre la pantalla en modo w=write (escritura)
      defaultextension=".txt" # Se define que la extension a usar es .txt
    )     

    # Si lector es None, significa que el usuario le dio Cancel o cerro la ventana
    if lector is None:
        return # No guardamos nada, solo terminamos la funcion haciendo un Return
    
    # textoAGuardar va a almacenar el contenido de textbox, desde la primer posicion (1.0) hasta el final (tk.END)
    textoAGuardar = str(textbox.get(1.0, tk.END))
    # se usa lector para usar .write() (write=escribir) con el texto a almacenar
    lector.write(textoAGuardar)
    # Se cierra el lector
    lector.close()

# Se crea el boton de Cargar
botonCargar = Button(root, text="Cargar",
                     command=cargarArchivo, height=3, width=10)

# Se agregar el boton Cargar a la vista
botonCargar.pack()

# Se crea el boton de Guardar
botonGuardar = Button(root, text="Guardar",
                      command=guardarArchivo, height=3, width=10)

# Se agregar el boton Guardar a la vista
botonGuardar.pack()

# Se crea el boton de Nuevo
botonGuardar = Button(root, text="Nuevo",
                      command=limpiarTexto, height=3, width=10)

# Se agregar el boton Nuevo a la vista
botonGuardar.pack()

# Se hace focus al texto para escribir
textbox.focus()
# Se centra la pantalla de la aplicacion
root.eval('tk::PlaceWindow . center')
# Se inicia la aplicacion
root.mainloop()
