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
