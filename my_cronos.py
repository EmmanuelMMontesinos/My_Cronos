from tkinter import *
from tkinter import ttk
import mi_db

# Ventana de Cronos


def cronos():
    """Esta es la ventana del marcador numerico para la password"""
    ventana_inicio.destroy()
    ventana_cronos = Tk()
    ventana_cronos.title("Cronos")
    frm_cronos = ttk.Frame(ventana_cronos, padding=20)
    n_digitos = ""
    password_check = ""
    referencia = ttk.Label(text=n_digitos)

    def add_n_digitos(texto_boton):
        """Añade un digito si un boton con numero es pulsado"""
        nonlocal n_digitos, password_check
        n_digitos += "*"
        password_check += texto_boton
        referencia.config(text=n_digitos)

    def borrar_pantalla():
        nonlocal password_check, n_digitos
        password_check = ""
        n_digitos = ""
        referencia.config(text=n_digitos)

    def mandar_check(check):
        print(f"{check}")

    for i in range(3):
        for j in range(1, 4):
            texto_boton = str(i*3+j)
            ttk.Button(text=texto_boton, command=lambda tb=texto_boton: add_n_digitos(
                tb)).grid(row=i, column=j-1)
    texto_boton = "0"
    ttk.Button(text=texto_boton, command=lambda tb=texto_boton: add_n_digitos(
        tb)).grid(row=3, column=1)
    ttk.Button(text="OK", command=lambda pc=password_check: mandar_check(
        password_check)).grid(row=3, column=0)
    ttk.Button(text="Borrar", command=lambda: borrar_pantalla()
               ).grid(row=3, column=2)
    referencia.grid(row=4, column=1)
    frm_cronos.pack()

    ventana_cronos.mainloop()


ventana_inicio = Tk()
ventana_inicio.title("Inicio")
frm = ttk.Frame(ventana_inicio, padding=20)
frm.grid()
ttk.Button(frm, text="Cronos", command=cronos).grid(column=0, row=0)
ttk.Button(frm, text="Gestión Empleados").grid(column=0, row=1)

ttk.Button(frm, text="Salir", command=ventana_inicio.destroy).grid(
    column=0, row=2)
ventana_inicio.mainloop()
