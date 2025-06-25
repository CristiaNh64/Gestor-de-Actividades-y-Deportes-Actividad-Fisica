import tkinter as tk

#Creamos la ventana que se vera durante todo el programa
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212")
ventana_principal.title("Proyecto GYM")

#Funcion utilizada para ir cambiando de ventanas
def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()

ventana_principal.mainloop()