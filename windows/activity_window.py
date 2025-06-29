import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from windows.timer_window import mostrar_ventana_temporizador # Importamos la función del temporizador
from windows.advice_window import mostrar_ventana_consejos # Importamos la función de consejos

# =============================================================================
# La Ventana de Actividades (donde se ven los ejercicios, con scroll para no perderte nada)
# =============================================================================
def mostrar_ventana_actividades(root, nombre_usuario_var, navigate_to_timer_func, navigate_to_advice_func, navigate_to_welcome_func):
    """
    Muestra la ventana con la lista de actividades y el menú contextual.

    Args:
        root (tk.Tk): La ventana principal de Tkinter.
        nombre_usuario_var (tk.StringVar): Variable Tkinter para el nombre del usuario.
        navigate_to_timer_func (function): Función para navegar a la ventana del cronómetro.
        navigate_to_advice_func (function): Función para navegar a la ventana de consejos.
        navigate_to_welcome_func (function): Función para navegar a la ventana de bienvenida.
    """
    tk.Label(root,
             text=f"¡Dale, {nombre_usuario_var.get()}! Elegí una actividad o sumate una nueva:", # Más onda acá también
             font=("Inter", 16, "bold"),
             fg="#00FF00", # Verde que resalta
             bg="#121212").pack(pady=20)

    # Un marco para que la lista y el scrollbar queden juntitos y prolijos
    frame_lista = tk.Frame(root, bg="#1E1E1E", bd=2, relief="groove")
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

    # --- Funciones para el menú desplegable (que ahora navegan a las nuevas ventanas) ---
    def iniciar_cronometro_nav(ejercicio_seleccionado):
        navigate_to_timer_func(ejercicio_seleccionado)

    def ver_consejo_nav(ejercicio_seleccionado):
        navigate_to_advice_func(ejercicio_seleccionado)

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
                menu_contextual = tk.Menu(root, tearoff=0,
                                         bg="#333333", fg="white",
                                         activebackground="#00FF00", activeforeground="#121212",
                                         relief="flat", bd=0)
                menu_contextual.add_command(label="Iniciar Cronómetro",
                                            command=lambda: iniciar_cronometro_nav(ejercicio_seleccionado))
                menu_contextual.add_command(label="Ver Consejo",
                                            command=lambda: ver_consejo_nav(ejercicio_seleccionado))
                # Mostrar el menú en la posición del clic del ratón
                menu_contextual.post(event.x_root, event.y_root)
        except tk.TclError:
            # Esto puede ocurrir si se hace clic fuera de un elemento de la lista
            pass

    # Vinculamos el clic derecho del ratón (Button-3) al Listbox
    listbox_ejercicios.bind("<Button-3>", mostrar_menu_contextual)
    # También podemos vincular el doble clic izquierdo para iniciar el cronómetro directamente
    listbox_ejercicios.bind("<Double-Button-1>", lambda event: iniciar_cronometro_nav(listbox_ejercicios.get(listbox_ejercicios.nearest(event.y))))

    # Botón para volver a la ventana de bienvenida, ¡por si te arrepentís!
    boton_volver = tk.Button(root,
                            text="Volver a la Bienvenida", # Más descriptivo
                            command=navigate_to_welcome_func,
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