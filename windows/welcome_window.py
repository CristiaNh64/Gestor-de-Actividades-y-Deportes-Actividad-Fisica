import tkinter as tk
from tkinter import messagebox

# =============================================================================
# La primera ventana: ¡Bienvenida y a pedir el nombre, ché!
# =============================================================================
def mostrar_ventana_bienvenida(root, nombre_usuario_var, navigate_to_activities_func):
    """
    Muestra la ventana de bienvenida para que el usuario ingrese su nombre.

    Args:
        root (tk.Tk): La ventana principal de Tkinter.
        nombre_usuario_var (tk.StringVar): Variable Tkinter para el nombre del usuario.
        navigate_to_activities_func (function): Función para navegar a la ventana de actividades.
    """
    tk.Label(root,
             text="¡Bienvenido a tu App de Ejercicios!",
             font=("Inter", 18, "bold"),
             fg="#00FF00", # Verde que te quiero verde
             bg="#121212").pack(pady=50)

    tk.Label(root,
             text="Dale, ¿cómo te llamás?", # Un poco más cercano
             font=("Inter", 14),
             fg="#FFFFFF", # Blanco como la nieve
             bg="#121212").pack(pady=10)

    entrada_nombre = tk.Entry(root,
                             font=("Inter", 14),
                             width=30,
                             bg="#333333", # Fondo un toque más claro
                             fg="#FFFFFF", # Texto blanco
                             insertbackground="#00FF00", # Cursor verde, ¡que se vea!
                             bd=0, # Sin borde, ¡bien liso!
                             relief="flat") # Estilo plano
    entrada_nombre.pack(pady=20)
    entrada_nombre.focus_set() # Para que el cursor ya esté ahí listo para escribir

    # Función anidada que se dispara cuando le das al botón "Continuar"
    def guardar_nombre_e_iniciar_app():
        nombre = entrada_nombre.get().strip() # Agarro lo que escribió y le saco los espacios de más

        if nombre: # Si escribió algo, ¡bien!
            nombre_usuario_var.set(nombre) # Guardamos el nombre en la variable compartida
            messagebox.showinfo("¡Qué grande!", f"¡Dale, {nombre_usuario_var.get()}! ¡Vamos a meterle pata!") # Mensaje de bienvenida con onda
            navigate_to_activities_func() # Y nos vamos a la siguiente pantalla
        else: # Si no escribió nada, ¡a avisarle!
            messagebox.showwarning("¡Atención, che!", "Por favor, ingresá tu nombre para seguir, ¡no te hagas el vivo!")

    # El botón "Continuar", ¡la puerta de entrada a la acción!
    boton_continuar = tk.Button(root,
                                text="Continuar",
                                command=guardar_nombre_e_iniciar_app, # Llama a la función al hacer clic
                                font=("Inter", 14, "bold"),
                                bg="#00FF00", # Verde potente
                                fg="#121212", # Texto oscuro
                                activebackground="#00CC00", # Verde un poco más oscuro cuando lo apretás
                                activeforeground="#FFFFFF", # Texto blanco cuando lo apretás
                                cursor="hand2", # El cursor se pone en forma de manito
                                bd=0, # Sin borde
                                relief="raised", # Efecto de relieve
                                padx=20, # Espacio horizontal
                                pady=10, # Espacio vertical
                                width=15) # Ancho fijo, ¡para que quede prolijo!
    boton_continuar.pack(pady=30)