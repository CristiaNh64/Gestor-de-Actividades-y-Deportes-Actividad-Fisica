import tkinter as tk
from tkinter import messagebox

# =============================================================================
# La Ventana del Cronómetro (¡a medir el tiempo de la actividad!)
# =============================================================================
def mostrar_ventana_temporizador(root, ejercicio_seleccionado, navigate_back_func):
    """
    Muestra la ventana del cronómetro para un ejercicio específico.

    Args:
        root (tk. Tk): La ventana principal de Tkinter.
        ejercicio_seleccionado (str): El nombre del ejercicio a cronometrar.
        navigate_back_func (function): Función para volver a la ventana anterior.
    """
    global tiempo_transcurrido_segundos, corriendo_temporizador, id_after_temporizador
    tiempo_transcurrido_segundos = 0
    corriendo_temporizador = False
    id_after_temporizador = None # Para guardar el ID del after y poder cancelarlo

    tk.Label(root,
             text=f"¡A cronometrar: {ejercicio_seleccionado}!",
             font=("Inter", 18, "bold"),
             fg="#00FF00",
             bg="#121212").pack(pady=30)

    # Etiqueta para mostrar el tiempo
    label_tiempo = tk.Label(root,
                            text="00:00:00",
                            font=("Inter", 48, "bold"),
                            fg="#FFFFFF",
                            bg="#121212")
    label_tiempo.pack(pady=40)

    def actualizar_temporizador():
        """Actualiza el tiempo mostrado en el cronómetro."""
        global tiempo_transcurrido_segundos, corriendo_temporizador, id_after_temporizador
        if corriendo_temporizador:
            tiempo_transcurrido_segundos += 1
            horas = tiempo_transcurrido_segundos // 3600
            minutos = (tiempo_transcurrido_segundos % 3600) // 60
            segundos = tiempo_transcurrido_segundos % 60
            label_tiempo.config(text=f"{horas:02d}:{minutos:02d}:{segundos:02d}")
            id_after_temporizador = root.after(1000, actualizar_temporizador) # Llama a sí misma después de 1 segundo

    def iniciar_pausar_temporizador():
        """Inicia o pausa el cronómetro."""
        global corriendo_temporizador, id_after_temporizador
        corriendo_temporizador = not corriendo_temporizador
        if corriendo_temporizador:
            boton_iniciar_pausar.config(text="Pausar", bg="#FFCC00") # Amarillo para pausar
            actualizar_temporizador()
        else:
            boton_iniciar_pausar.config(text="Reanudar", bg="#00FF00") # Verde para reanudar
            if id_after_temporizador:
                root.after_cancel(id_after_temporizador) # Cancela la llamada futura

    def detener_temporizador():
        """Detiene el cronómetro y guarda el tiempo."""
        global corriendo_temporizador, id_after_temporizador, tiempo_transcurrido_segundos
        if id_after_temporizador:
            root.after_cancel(id_after_temporizador)
        corriendo_temporizador = False
        messagebox.showinfo("Tiempo Registrado",
                            f"¡Muy bien! Registraste {label_tiempo.cget('text')} en {ejercicio_seleccionado}.")
        # Aquí iría la lógica para guardar el tiempo en algún registro o base de datos.
        navigate_back_func() # Vuelve a la pantalla de actividades

    # Frame para los botones de control del temporizador
    frame_botones_temporizador = tk.Frame(root, bg="#121212")
    frame_botones_temporizador.pack(pady=20)

    boton_iniciar_pausar = tk.Button(frame_botones_temporizador,
                                     text="Iniciar",
                                     command=iniciar_pausar_temporizador,
                                     font=("Inter", 14, "bold"),
                                     bg="#00FF00", fg="#121212",
                                     activebackground="#00CC00", activeforeground="#FFFFFF",
                                     cursor="hand2", bd=0, relief="raised", padx=15, pady=8, width=10)
    boton_iniciar_pausar.pack(side="left", padx=10)

    boton_detener = tk.Button(frame_botones_temporizador,
                              text="Detener",
                              command=detener_temporizador,
                              font=("Inter", 14, "bold"),
                              bg="#FF0000", fg="#FFFFFF", # Rojo para detener
                              activebackground="#CC0000", activeforeground="#FFFFFF",
                              cursor="hand2", bd=0, relief="raised", padx=15, pady=8, width=10)
    boton_detener.pack(side="left", padx=10)

    # Botón para volver a la ventana de actividades (cancelando el temporizador si está activo)
    boton_volver = tk.Button(root,
                            text="Volver a Actividades",
                            command=lambda: [detener_temporizador(), navigate_back_func()] if corriendo_temporizador else navigate_back_func(),
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