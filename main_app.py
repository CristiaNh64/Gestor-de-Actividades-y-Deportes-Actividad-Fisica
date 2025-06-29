import tkinter as tk
from windows.welcome_window import mostrar_ventana_bienvenida
from windows.activity_window import mostrar_ventana_actividades
from windows.timer_window import mostrar_ventana_temporizador
from windows.advice_window import mostrar_ventana_consejos
from utils.helpers import limpiar_ventana

# =============================================================================
# La Ventana Principal (donde se arma todo el quilombo)
# Es la ventana maestra que se va a ver durante todo el programa.
# =============================================================================
ventana_principal = tk.Tk()
ventana_principal.geometry("600x600")
ventana_principal.config(background="#121212") # Fondo oscuro para que pinte bien
ventana_principal.title("Proyecto GYM (¡A darle con todo!)") # Título más canchero
ventana_principal.resizable(False, False) # Para que no la puedas agrandar ni achicar, ¡fija como rulo de estatua!

# Variable StringVar de Tkinter para guardar el nombre del usuario, ¡así lo tenemos siempre a mano!
# Usamos StringVar para que los widgets puedan actualizarse automáticamente.
nombre_usuario_var = tk.StringVar()

# =============================================================================
# Funciones para la navegación entre ventanas
# Estas funciones son el "pegamento" que nos lleva de una pantalla a otra.
# =============================================================================

def navigate_to_welcome():
    """Navega a la ventana de bienvenida."""
    limpiar_ventana(ventana_principal)
    mostrar_ventana_bienvenida(ventana_principal, nombre_usuario_var, navigate_to_activities)

def navigate_to_activities():
    """Navega a la ventana de gestión de actividades."""
    limpiar_ventana(ventana_principal)
    mostrar_ventana_actividades(ventana_principal, nombre_usuario_var, navigate_to_timer, navigate_to_advice, navigate_to_welcome)

def navigate_to_timer(ejercicio_seleccionado):
    """Navega a la ventana del cronómetro para un ejercicio específico."""
    limpiar_ventana(ventana_principal)
    mostrar_ventana_temporizador(ventana_principal, ejercicio_seleccionado, navigate_to_activities)

def navigate_to_advice(ejercicio_seleccionado):
    """Navega a la ventana de consejos para un ejercicio específico."""
    limpiar_ventana(ventana_principal)
    mostrar_ventana_consejos(ventana_principal, ejercicio_seleccionado, navigate_to_activities)

# =============================================================================
# ¡A encender la App!
# =============================================================================
if __name__ == "__main__":
    # Arrancamos mostrando la primera ventana, ¡la bienvenida!
    navigate_to_welcome()

    # Y esto es lo que hace que la ventana se quede abierta y escuche lo que hacés
    ventana_principal.mainloop()