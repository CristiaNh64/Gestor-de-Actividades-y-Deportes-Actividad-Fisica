# =============================================================================
# Funciones de Utilidad
# Ayudantes para tareas comunes en la aplicación.
# =============================================================================

def limpiar_ventana(root):
    """
    Función para limpiar todos los widgets de una ventana Tkinter.
    La deja pelada para poner el contenido nuevo.

    Args:
        root (tk.Tk): La ventana principal de Tkinter.
    """
    for widget in root.winfo_children():
        widget.destroy()



