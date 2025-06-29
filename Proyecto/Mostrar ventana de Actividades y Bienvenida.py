import tkinter as tk
from tkinter import messagebox
from tkinter import ttk # Importamos ttk para un Scrollbar con mejor estilo

# =============================================================================
# La Ventana Principal (donde se arma todo el quilombo)
# Es la ventana maestra que se va a ver durante todo el programa.
# =============================================================================
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212") # Fondo oscuro para que pinte bien
ventana_principal.title("Proyecto GYM (¡A darle con todo!)") # Título más canchero
ventana_principal.resizable(False, False) # Para que no la puedas agrandar ni achicar, ¡fija como rulo de estatua!

# Variable global para guardar el nombre del usuario, ¡así lo tenemos siempre a mano!
nombre_usuario = ""
# Variable global para el campo donde se escribe el nombre
entrada_nombre = None

# Función para limpiar la ventana, ¡la dejamos pelada para poner lo nuevo!
def limpiar_ventana():
    for widget in ventana_principal.winfo_children():
        widget.destroy()

# =============================================================================
# Las Ventanas que vamos a ir mostrando (una por una, sin apuro)
# =============================================================================

# La primera ventana: ¡Bienvenida y a pedir el nombre, ché!
def mostrar_ventana_bienvenida():
    limpiar_ventana() # Primero limpiamos todo, obvio

    tk.Label(ventana_principal,
             text="¡Bienvenido a tu App de Ejercicios!",
             font=("Inter", 18, "bold"),
             fg="#00FF00", # Verde que te quiero verde
             bg="#121212").pack(pady=50)

    tk.Label(ventana_principal,
             text="Dale, ¿cómo te llamás?", # Un poco más cercano
             font=("Inter", 14),
             fg="#FFFFFF", # Blanco como la nieve
             bg="#121212").pack(pady=10)

    global entrada_nombre # ¡Lo hacemos global para que el botón lo agarre!
    entrada_nombre = tk.Entry(ventana_principal,
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
        global nombre_usuario # Accedemos al nombre global
        nombre = entrada_nombre.get().strip() # Agarro lo que escribió y le saco los espacios de más

        if nombre: # Si escribió algo, ¡bien!
            nombre_usuario = nombre
            messagebox.showinfo("¡Qué grande!", f"¡Dale, {nombre_usuario}! ¡Vamos a meterle pata!") # Mensaje de bienvenida con onda
            mostrar_ventana_actividades() # Y nos vamos a la siguiente pantalla
        else: # Si no escribió nada, ¡a avisarle!
            messagebox.showwarning("¡Atención, che!", "Por favor, ingresá tu nombre para seguir, ¡no te hagas el vivo!")

    # El botón "Continuar", ¡la puerta de entrada a la acción!
    boton_continuar = tk.Button(ventana_principal,
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

# =============================================================================
# La Ventana de Actividades (donde se ven los ejercicios, con scroll para no perderte nada)
# =============================================================================
def mostrar_ventana_actividades():
    limpiar_ventana() # Limpiamos la ventana, como siempre

    tk.Label(ventana_principal,
             text=f"¡Dale, {nombre_usuario}! Elegí una actividad o sumate una nueva:", # Más onda acá también
             font=("Inter", 16, "bold"),
             fg="#00FF00", # Verde que resalta
             bg="#121212").pack(pady=20)

    # Un marco para que la lista y el scrollbar queden juntitos y prolijos
    frame_lista = tk.Frame(ventana_principal, bg="#1E1E1E", bd=2, relief="groove")
    frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

    # La Listbox para mostrar los ejercicios, ¡que no se te escape ninguno!
    listbox_ejercicios = tk.Listbox(frame_lista,
                                    width=40, # Ancho de la lista
                                    height=15, # Cuántos ejercicios se ven de una
                                    font=("Inter", 14),
                                    bg="#282828", # Fondo oscuro de la listbox
                                    fg="#E0E0E0", # Color de texto claro
                                    selectbackground="#00FF00", # Color de selección (verde)
                                    selectforeground="#121212", # Texto oscuro cuando seleccionado
                                    bd=0, # Sin borde de la listbox
                                    highlightthickness=0, # Elimina el borde de selección azul por defecto
                                    relief="flat") # Estilo plano
    listbox_ejercicios.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    # La barra de desplazamiento (Scrollbar) para que puedas ir para arriba y para abajo
    scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=listbox_ejercicios.yview)
    scrollbar.pack(side="right", fill="y")

    # Unimos la lista con la barra de desplazamiento, ¡que trabajen juntos!
    listbox_ejercicios.config(yscrollcommand=scrollbar.set)

    # Acá la lista de ejercicios que ya te dejamos armados, ¡para arrancar!
    ejercicios_disponibles = [
        "Correr", "Flexiones", "Yoga", "Abdominales", "Bicicleta",
        "Caminar", "Pilates", "Levantamiento de Pesas", "Saltar la Cuerda",
        "Nadar", "Sentadillas", "Plancha", "Danza", "Estiramientos",
        "Zumba", "Boxeo de Sombra", "Calistenia", "Senderismo", "Remo",
        "Escalar", "CrossFit", "Spinning", "Baloncesto", "Fútbol", "Tenis"
    ]

    # Metemos cada ejercicio en la lista
    for ejercicio in ejercicios_disponibles:
        listbox_ejercicios.insert(tk.END, ejercicio) # Los agregamos al final

    # --- Funciones para el menú desplegable ---
    def iniciar_cronometro(ejercicio_seleccionado):
        messagebox.showinfo("Cronómetro", f"¡Dale! A iniciar el cronómetro para: {ejercicio_seleccionado}")
        # Aquí iría la lógica para la ventana del cronómetro (Mini Proyecto 2)
        # Por ahora, solo es un mensaje.

    def ver_consejo(ejercicio_seleccionado):
        # Aquí podrías tener un diccionario o una base de datos de consejos
        consejos = {
            "Correr": "¡No te olvides de calentar y estirar! Empezá tranqui.",
            "Flexiones": "Mantené la espalda recta y bajá hasta que el pecho casi toque el suelo.",
            "Yoga": "Concentrate en tu respiración y no te forces de más.",
            "Abdominales": "Controlá el movimiento y no tires del cuello.",
            "Bicicleta": "Ajustá bien el asiento para evitar lesiones de rodilla.",
            "Caminar": "¡Mantené un buen ritmo y disfrutá del paisaje!",
            "Pilates": "La clave está en el control y la precisión de cada movimiento.",
            "Levantamiento de Pesas": "Usá pesos adecuados y pedí ayuda si es necesario para las posturas.",
            "Saltar la Cuerda": "Aterrizá suavemente sobre las puntas de los pies para proteger tus rodillas.",
            "Nadar": "Respirá por un lado y coordiná el movimiento de brazos y piernas.",
            "Sentadillas": "Asegurate de que tus rodillas no sobrepasen la punta de tus pies.",
            "Plancha": "Contraé el abdomen y los glúteos, mantené una línea recta del cuerpo.",
            "Danza": "Calentá bien todo el cuerpo antes de empezar a bailar.",
            "Estiramientos": "Estirá suavemente y mantené cada posición al menos 20 segundos.",
            "Zumba": "¡Soltate y divertite! La energía es lo más importante.",
            "Boxeo de Sombra": "Concentrate en la técnica y la velocidad de tus golpes.",
            "Calistenia": "Empezá con ejercicios básicos y andá progresando de a poco.",
            "Senderismo": "Usá buen calzado y llevá agua, ¡el camino puede ser largo!",
            "Remo": "Usá las piernas para empujar, no solo los brazos.",
            "Escalar": "Desarrollá la fuerza de agarre y la técnica de pies.",
            "CrossFit": "Es un entrenamiento intenso, escuchá a tu cuerpo y andá a tu ritmo.",
            "Spinning": "Ajustá la altura del asiento y el manillar para una postura cómoda.",
            "Baloncesto": "Practicá el dribling y los pases, no solo los tiros.",
            "Fútbol": "Mejorá tu control de balón y el trabajo en equipo.",
            "Tenis": "Trabajá en tu saque y en la velocidad de tus movimientos."
        }
        consejo = consejos.get(ejercicio_seleccionado, "¡Buenísimo ejercicio! Seguí así.")
        messagebox.showinfo(f"Consejo para {ejercicio_seleccionado}", consejo)
        # Aquí iría la lógica para la cuarta ventana: Mostrar consejo

    def mostrar_menu_contextual(event):
        # Obtener el índice del elemento sobre el que se hizo clic
        try:
            index = listbox_ejercicios.nearest(event.y)
            # Asegurarse de que se hizo clic sobre un elemento válido
            if index != -1 and listbox_ejercicios.bbox(index) is not None:
                listbox_ejercicios.selection_clear(0, tk.END) # Limpia cualquier selección anterior
                listbox_ejercicios.selection_set(index) # Selecciona el elemento clicado
                ejercicio_seleccionado = listbox_ejercicios.get(index)

                # Creamos el menú contextual (desplegable)
                menu_contextual = tk.Menu(ventana_principal, tearoff=0,
                                         bg="#333333", fg="white",
                                         activebackground="#00FF00", activeforeground="#121212",
                                         relief="flat", bd=0)
                menu_contextual.add_command(label="Iniciar Cronómetro",
                                            command=lambda: iniciar_cronometro(ejercicio_seleccionado))
                menu_contextual.add_command(label="Ver Consejo",
                                            command=lambda: ver_consejo(ejercicio_seleccionado))
                # Mostrar el menú en la posición del clic del ratón
                menu_contextual.post(event.x_root, event.y_root)
        except tk.TclError:
            # Esto puede ocurrir si se hace clic fuera de un elemento de la lista
            pass

    # Vinculamos el clic derecho del ratón (Button-3) al Listbox
    listbox_ejercicios.bind("<Button-3>", mostrar_menu_contextual)
    # También podemos vincular el doble clic izquierdo para iniciar el cronómetro directamente
    listbox_ejercicios.bind("<Double-Button-1>", lambda event: iniciar_cronometro(listbox_ejercicios.get(listbox_ejercicios.nearest(event.y))))


    # Botón para volver a la ventana de bienvenida, ¡por si te arrepentís!
    boton_volver = tk.Button(ventana_principal,
                            text="Volver a la Bienvenida", # Más descriptivo
                            command=mostrar_ventana_bienvenida,
                            font=("Inter", 12),
                            bg="#555555",
                            fg="#FFFFFF",
                            activebackground="#777777",
                            activeforeground="#FFFFFF",
                            cursor="hand2",
                            bd=0,
                            relief="raised",
                            padx=10,
                            pady=5)
    boton_volver.pack(pady=20)


# =============================================================================
# ¡A encender la App!
# =============================================================================
# Arrancamos mostrando la primera ventana, ¡la bienvenida!
mostrar_ventana_bienvenida()

# Y esto es lo que hace que la ventana se quede abierta y escuche lo que hacés
ventana_principal.mainloop()