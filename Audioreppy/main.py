import tkinter as tk
from tkinter import filedialog
import pygame

def reproducir():
    pygame.mixer.music.load(ruta_archivo.get())
    pygame.mixer.music.play()

def detener():
    pygame.mixer.music.stop()

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[('Archivos de audio', '*.mp3;*.wav')])
    ruta_archivo.set(archivo)

# Inicializar pygame
pygame.mixer.init()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reproductor de Música")

# Etiqueta y campo de entrada para la ruta del archivo
ruta_archivo = tk.StringVar()
etiqueta_archivo = tk.Label(ventana, text="Archivo:")
etiqueta_archivo.pack()
campo_archivo = tk.Entry(ventana, textvariable=ruta_archivo, state='readonly')
campo_archivo.pack()

# Botón para seleccionar archivo
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()

# Botón para reproducir
boton_reproducir = tk.Button(ventana, text="Reproducir", command=reproducir)
boton_reproducir.pack()

# Botón para detener
boton_detener = tk.Button(ventana, text="Detener", command=detener)
boton_detener.pack()

# Ejecutar la interfaz de usuario
ventana.mainloop()
