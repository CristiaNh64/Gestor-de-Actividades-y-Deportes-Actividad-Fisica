import tkinter as tk

#Creamos la ventana que se vera durante todo el programa
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212")

#Funcion utilizada para ir cambiando de ventanas
def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()

#La primer ventana de la app, la que le aparece al usuario para ingresar su nombre        
ventana_bienvenida = tk.Label(ventana_principal, text="BIENVENIDO! \U0001F44C \U0001F44C \U0001F44C")


ventana_bienvenida.pack()
ventana_principal.mainloop()
