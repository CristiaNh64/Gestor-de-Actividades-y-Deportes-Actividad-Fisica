import tkinter


ventana__principal = tkinter.Tk()
ventana__principal.geometry("500x500")
ventana__principal.configure(background="black")
ventana__principal.title("PROYECTO 1")

Ventana__Usuario = tkinter.Frame(ventana__principal,bg="beige")
Ventana__Usuario.configure(width=300,height=300)
Ventana__Usuario.pack()

boton_continuar = tkinter.Button(ventana__principal, text="Continuar")
boton_continuar.config(command="ingrese nombre")
boton_continuar.pack()


ventana__principal.mainloop()



