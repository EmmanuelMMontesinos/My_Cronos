from tkinter import *
from tkinter import ttk, messagebox
import mi_db


# Ventana de Cronos
def cronos():
    """Esta es la ventana del marcador numerico para la password"""
    ventana_inicio.destroy()
    ventana_cronos = Tk()
    ventana_cronos.title("Cronos")
    ventana_cronos.config(background="green")
    frm_cronos = ttk.Frame(ventana_cronos, padding=20)

    n_digitos = ""
    password_check = ""
    referencia = ttk.Label(text=n_digitos, background="green")

    def add_n_digitos(texto_boton):
        """Añade un digito si un boton con numero es pulsado"""
        nonlocal n_digitos, password_check
        n_digitos += "*"
        password_check += texto_boton
        referencia.config(text=n_digitos)

    def key_presionada(event):
        if event.char.isdigit() and "0" <= event.char <= "9":
            texto_boton = event.char
            add_n_digitos(texto_boton)

    def borrar_pantalla():
        nonlocal password_check, n_digitos
        password_check = ""
        n_digitos = ""
        referencia.config(text=n_digitos)

# Desde aqui comprueba el id(dni)
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
    ventana_cronos.bind('<Key>', key_presionada)
    ventana_cronos.mainloop()


# Ventana de Gestion
def gestion():
    def enviar_mi_db(pk):
        nombre, dni, password, horas_semanales = pk
        solicitud = mi_db.Trabajador()
        solicitud.nombre = nombre.get()
        solicitud.dni = dni.get()
        solicitud.password = password.get()
        solicitud.horas_semanales = horas_semanales.get()
        try:
            solicitud.add_Trabajador()
        except Exception as e:
            mensaje = f"Error al procesar peticion, asegurese de que NO esta ya registrado\n{e}"
            messagebox.showerror("Error", mensaje)
        else:
            mensaje = f"""Agregado: {solicitud.nombre} DNI: {solicitud.dni}"""
            messagebox.showinfo("Agregado", mensaje)

    def add_trabajador():

        ventana_gestion.destroy()
        ventana_add = Tk()
        ventana_add.title("Agregar Trabajador")
        frm_add = ttk.Frame(ventana_add, padding=20)
        ttk.Label(text="Nombre").grid(column=0, row=0)
        nombre = ttk.Entry()
        nombre.grid(column=1, row=0)
        ttk.Label(text="DNI").grid(column=0, row=1)
        dni = ttk.Entry()
        dni.grid(column=1, row=1)
        ttk.Label(text="Password").grid(column=0, row=2)
        password = ttk.Entry()
        password.grid(column=1, row=2)
        ttk.Label(text="Horas Semanales").grid(column=0, row=3)
        horas_semanales = ttk.Entry()
        horas_semanales.grid(column=1, row=3)
        ttk.Button(text="Agregar", command=lambda pk=[nombre, dni, password, horas_semanales]: enviar_mi_db(pk)).grid(
            columnspan=1, row=4)
        ttk.Button(text="Salir", command=ventana_add.destroy).grid(
            column=2, row=4)
        frm_add.pack()
        ventana_add.mainloop()
    ventana_inicio.destroy()
    ventana_gestion = Tk()
    ventana_gestion.title("Gestión")
    frm_gestion = ttk.Frame(ventana_gestion, padding=20)
    ttk.Button(text="Agregar", command=add_trabajador).grid(column=0, row=0)
    frm_gestion.pack()
    ventana_gestion.mainloop()


ventana_inicio = Tk()
ventana_inicio.title("Inicio")
frm = ttk.Frame(ventana_inicio, padding=20)
frm.grid()
ttk.Button(frm, text="Cronos", command=cronos).grid(column=0, row=0)
ttk.Button(frm, text="Gestión Empleados",
           command=gestion).grid(column=0, row=1)

ttk.Button(frm, text="Salir", command=ventana_inicio.destroy).grid(
    column=0, row=2)

ventana_inicio.mainloop()
