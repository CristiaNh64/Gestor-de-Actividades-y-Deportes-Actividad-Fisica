import tkinter as tk

# Diccionario de consejos para los ejercicios
consejos_ejercicios = {
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

# =============================================================================
# La Ventana de Consejos (¡para que siempre tengas la posta!)
# =============================================================================
def mostrar_ventana_consejos(root, ejercicio_seleccionado, navigate_back_func):
    """
    Muestra la ventana con un consejo específico para el ejercicio seleccionado.

    Args:
        root (tk.Tk): La ventana principal de Tkinter.
        ejercicio_seleccionado (str): El nombre del ejercicio para el cual mostrar el consejo.
        navigate_back_func (function): Función para volver a la ventana anterior.
    """
    consejo = consejos_ejercicios.get(ejercicio_seleccionado, "¡Buenísimo ejercicio! Seguí así.")

    tk.Label(root,
             text=f"Consejo para: {ejercicio_seleccionado}",
             font=("Inter", 18, "bold"),
             fg="#00FF00",
             bg="#121212").pack(pady=30)

    tk.Label(root,
             text=consejo,
             font=("Inter", 14),
             fg="#FFFFFF",
             bg="#121212",
             wraplength=500, # Para que el texto se ajuste al ancho
             justify="center").pack(pady=20, padx=20)

    # Botón para volver a la ventana de actividades
    boton_volver = tk.Button(root,
                            text="Volver a Actividades",
                            command=navigate_back_func,
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