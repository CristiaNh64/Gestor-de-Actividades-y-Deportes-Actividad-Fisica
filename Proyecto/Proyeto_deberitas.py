import tkinter as tk
from tkinter import messagebox # Importamos messagebox para mostrar mensajes

# Ventana que pricipal que se vera en el programa
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212")
ventana_principal.title("Proyecto GYM")
ventana_principal.resizable(False,False) #Para que no se pueda agrandar mas de 600x600

# Variable para almacenar el nombre de usuario
nombre_usuario = ""

# Funcion utilizada para ir cambiando de ventanas
def limpiar_ventana():
    # Destruye todos los widgets de la ventana principal
    for widget in ventana_principal.winfo_children():
        widget.destroy()

def mostrar_ventana_bienvenida():
    limpiar_ventana()
    
    tk.Label(ventana_principal, text="¡Bienvenido a tu App de Ejercicios!", font=("Inter", 16),fg="white", bg="#121212").pack(pady=50)
    
    tk.Label(ventana_principal, text="Ingresa tu nombre:", font=("Inter", 12), fg="white", bg="#121212").pack()
    
    global entrada_nombre  # Necesario para acceder desde guardar_nombre_e_iniciar_app()
    entrada_nombre = tk.Entry(ventana_principal, 
                             font=("Inter", 14), 
                             width=30)
    entrada_nombre.pack(pady=20)
    
    # Botón "Continuar"
    boton_continuar = tk.Button(ventana_principal,
                                text="Continuar",
                                command=guardar_nombre_e_iniciar_app, # Llama a la función al hacer clic
                                font=("Inter", 14, "bold"),
                                bg="#00FF00", # Color de fondo del botón verde
                                fg="#121212", # Color de texto oscuro
                                activebackground="#00CC00", # Color al hacer clic
                                activeforeground="#FFFFFF", # Color de texto al hacer clic
                                cursor="hand2", # Cambia el cursor al pasar por encima
                                bd=0, # Sin borde
                                relief="raised", # Efecto de relieve
                                padx=20, # Padding horizontal
                                pady=10, # Padding vertical
                                width=15) # Ancho fijo para el botón
    boton_continuar.pack(pady=30)

# Función que se ejecuta cuando se presiona el botón "Continuar"
def guardar_nombre_e_iniciar_app():
    global nombre_usuario
    nombre = entrada_nombre.get().strip() # Obtenemos el texto y quitamos espacios extra

    if nombre: # Si el nombre no está vacío
        nombre_usuario = nombre
        messagebox.showinfo("¡Hola!", f"¡Hola, {nombre_usuario}! Vamos a empezar.") # Mensaje de bienvenida
        # Aquí llamaremos a la siguiente ventana de la aplicación
        mostrar_ventana_actividades() # Llamamos a la función de la siguiente ventana
    else:
        messagebox.showwarning("Atención", "Por favor, ingresa tu nombre para continuar.")

def mostrar_ventana_actividades():
    limpiar_ventana()
    
    # Mensaje de bienvenida
    tk.Label(ventana_principal,
             text=f"¡Bienvenido, {nombre_usuario}! Aquí irán tus actividades.",
             font=("Inter", 16),
             fg="white",
             bg="#121212").pack(pady=20)
    
    # Contenedor de ejercicios
    contenedor_ejercicios = tk.Frame(ventana_principal, bg="#121212")
    contenedor_ejercicios.pack()
    
    ventana_ejercicios = tk.Label(contenedor_ejercicios, bg="#121212")
    ventana_ejercicios.pack()
    
    ejercicios = ["Flexiones","Correr","Abdominales","Bicicleta","Caminar","Pilates","Ejercicios de Gimnasio","Saltar la cuerda","Nadar","Sentadillas","Plancha","Yoga","Danza"]
    
    for ejercicio in ejercicios:
        simple_ejer = tk.Frame(ventana_ejercicios, background="#1E1E1E")  # Fondo oscuro para el frame
        simple_ejer.pack(pady=3, padx=10, fill="x")
        boton_ejer = tk.Button(simple_ejer, 
                              text=ejercicio, 
                              background="#333333",  
                              fg="white",  
                              activebackground="#00CC00",  
                              font=("Inter", 12),
                              relief="flat",
                              borderwidth=0)
        boton_ejer.pack(fill="x", padx=5, pady=2)

# --- Inicio de la aplicación ---
# Llamamos a la función para mostrar la primera ventana al iniciar
mostrar_ventana_bienvenida()

# Inicia el bucle principal de Tkinter
ventana_principal.mainloop()
