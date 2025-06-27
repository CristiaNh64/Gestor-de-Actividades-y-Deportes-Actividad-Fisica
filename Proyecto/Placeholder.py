# --- Funciones placeholder para las siguientes ventanas (las implementaremos después) ---

def mostrar_ventana_actividades():
    limpiar_ventana()
    # Esta será la segunda ventana: Gestión de Actividades
    label_proximamente = tk.Label(ventana_principal,
                                  text=f"¡Bienvenido, {nombre_usuario}! Aquí irán tus actividades.",
                                  font=("Inter", 16),
                                  fg="#FFFFFF",
                                  bg="#121212")
    label_proximamente.pack(pady=50)

# --- Inicio de la aplicación ---
# Llamamos a la función para mostrar la primera ventana al iniciar
mostrar_ventana_bienvenida()

# Inicia el bucle principal de Tkinter
ventana_principal.mainloop()