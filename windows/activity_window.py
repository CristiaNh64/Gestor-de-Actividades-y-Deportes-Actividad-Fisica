import tkinter as tk
from tkinter import ttk, Menu, simpledialog, messagebox  # Todos los imports necesarios
from windows.timer_window import mostrar_ventana_temporizador
from windows.advice_window import mostrar_ventana_consejos

# =============================================================================
# La Ventana de Actividades (donde se ven los ejercicios, con scroll para no perderte nada)
# =============================================================================

def mostrar_ventana_actividades(root, nombre_usuario_var, navigate_to_timer_func, 
                              navigate_to_advice_func, navigate_to_welcome_func):
    """
    Muestra la ventana con la lista de actividades y el menú contextual.

    Args:
        root (tk.Tk): La ventana principal de Tkinter.
        nombre_usuario_var (tk.StringVar): Variable Tkinter para el nombre del usuario.
        navigate_to_timer_func (function): Función para navegar a la ventana del cronómetro.
        navigate_to_advice_func (function): Función para navegar a la ventana de consejos.
        navigate_to_welcome_func (function): Función para navegar a la ventana de bienvenida.
    """

    # --- Lista de ejercicios ---
    ejercicios_disponibles = [
        "Correr", "Flexiones", "Yoga", "Abdominales", "Bicicleta",
        "Caminar", "Pilates", "Levantamiento de Pesas", "Saltar la Cuerda",
        "Nadar", "Sentadillas", "Plancha", "Danza", "Estiramientos",
        "Zumba", "Boxeo de Sombra", "Calistenia", "Senderismo", "Remo",
        "Escalar", "CrossFit", "Spinning", "Baloncesto", "Fútbol", "Tenis"
    ]

    # --- Titulo ---
    tk.Label(root,
                text=f"¡Dale, {nombre_usuario_var.get()}! Elegí una actividad:",
                font=("Inter", 16, "bold"),
                fg="#00FF00",
                bg="#121212").pack(pady=20)

    # Un marco para que la lista y el scrollbar queden juntitos y prolijos
    frame_lista = tk.Frame(root, bg="#1E1E1E", bd=2, relief="groove")
    frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

    #  La Listbox para mostrar los ejercicios
    listbox_ejercicios = tk.Listbox(
        frame_lista,
        width=40,
        height=15,
        font=("Inter", 14),
        bg="#282828",
        fg="#E0E0E0",
        selectbackground="#00FF00",
        selectforeground="#121212",
        bd=0,
        highlightthickness=0,
        relief="flat"
    )
    listbox_ejercicios.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    # La barra de desplazamiento (Scrollbar) para que puedas ir para arriba y para abajo
    scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=listbox_ejercicios.yview)
    scrollbar.pack(side="right", fill="y")

    # Unimos la lista con la barra de desplazamiento, ¡que trabajen juntos!
    listbox_ejercicios.config(yscrollcommand=scrollbar.set)

    # Metemos cada ejercicio en la lista
    for ejercicio in ejercicios_disponibles:
        listbox_ejercicios.insert(tk.END, ejercicio)

    # --- Funciones para gestión de ejercicios ---
    def agregar_ejercicio():
        nuevo_ejercicio = simpledialog.askstring(
            "Agregar Ejercicio",
            "Nombre del nuevo ejercicio:",
            parent=root
        )
        if nuevo_ejercicio and nuevo_ejercicio.strip():
            ejercicios_disponibles.append(nuevo_ejercicio.strip())
            listbox_ejercicios.insert(tk.END, nuevo_ejercicio.strip())

    def quitar_ejercicio():
        seleccionado = listbox_ejercicios.curselection()
        if seleccionado:
            listbox_ejercicios.delete(seleccionado[0])
            ejercicios_disponibles.pop(seleccionado[0])
        else:
            messagebox.showwarning("Atención", "Selecciona un ejercicio primero")

    # --- Botones de gestión ---
    frame_botones = tk.Frame(root, bg="#121212")
    frame_botones.pack(pady=10)

    btn_agregar = tk.Button(
        frame_botones,
        text="➕ Agregar Ejercicio",
        command=agregar_ejercicio,
        font=("Inter", 12),
        bg="#1E1E1E",
        fg="#00FF00",
        activebackground="#00CC00",
        activeforeground="#121212",
        cursor="hand2",
        bd=0,
        relief="raised",
        padx=15,
        pady=5
    )
    btn_agregar.pack(side="left", padx=10)

    btn_quitar = tk.Button(
        frame_botones,
        text="➖ Quitar Ejercicio",
        command=quitar_ejercicio,
        font=("Inter", 12),
        bg="#1E1E1E",
        fg="#FF5555",
        activebackground="#CC0000",
        activeforeground="#121212",
        cursor="hand2",
        bd=0,
        relief="raised",
        padx=15,
        pady=5
    )
    btn_quitar.pack(side="left", padx=10)

    # --- Botón Volver ---
    tk.Button(
        root,
        text="Volver a la Bienvenida",
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
        pady=5
    ).pack(pady=20)

    # --- Menú contextual ---
    def mostrar_menu_contextual(event):
        try:
            index = listbox_ejercicios.nearest(event.y)
            # Asegurarse de que se hizo clic sobre un elemento válido
            if index != -1 and listbox_ejercicios.bbox(index):
                listbox_ejercicios.selection_clear(0, tk.END) # Limpia cualquier selección anterior
                listbox_ejercicios.selection_set(index) # Selecciona el elemento clicado
                ejercicio = listbox_ejercicios.get(index)
                
                # Creamos el menú contextual (desplegable)
                menu_contextual = tk.Menu(root, tearoff=0, bg="#333333", fg="white",
                            activebackground="#00FF00", activeforeground="#121212")
                menu_contextual.add_command(
                    label="Iniciar Cronómetro",
                    command=lambda: navigate_to_timer_func(ejercicio)
                )
                menu_contextual.add_command(
                    label="Ver Consejo",
                    command=lambda: navigate_to_advice_func(ejercicio)
                )
                menu_contextual.tk_popup(event.x_root, event.y_root)
        except Exception as e:
            print(f"Error al mostrar menú: {e}")

    listbox_ejercicios.bind("<Button-3>", mostrar_menu_contextual)

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