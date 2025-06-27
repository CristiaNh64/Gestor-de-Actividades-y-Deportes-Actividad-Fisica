import tkinter as tk
from tkinter import messagebox # Importamos messagebox para mostrar mensajes

# Ventana que pricipal que se vera en el programa
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212")
ventana_principal.title("Proyecto GYM")

# Variable para almacenar el nombre de usuario
nombre_usuario = ""

# Funcion utilizada para ir cambiando de ventanas
def limpiar_ventana():
    # Destruye todos los widgets hijos de la ventana principal
    for widget in ventana_principal.winfo_children():
        widget.destroy()



