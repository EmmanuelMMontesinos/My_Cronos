from tkinter import *
from tkinter import ttk, messagebox
import mi_db


"""Esta es la ventana del marcador numerico para la password"""
n_digitos = ""
password_check = ""
ventana_cronos = Tk()
ventana_cronos.title("Cronos")
ventana_cronos.iconbitmap("cronos.ico")
ventana_cronos.config(background="green")
frm_cronos = ttk.Frame(ventana_cronos, padding=20)

referencia = ttk.Label(ventana_cronos, text=n_digitos, background="green")
# Ventana de Cronos


def add_n_digitos(texto_boton):
    """Añade un digito si un boton con numero es pulsado"""
    global n_digitos, password_check
    n_digitos += "*"
    password_check += texto_boton
    referencia.config(text=n_digitos)


def key_presionada(event):
    if event.char.isdigit() and "0" <= event.char <= "9":
        texto_boton = event.char
        add_n_digitos(texto_boton)


def borrar_pantalla():
    global password_check, n_digitos
    password_check = ""
    n_digitos = ""
    referencia.config(text=n_digitos)

# Desde aqui comprueba el id(dni)


def mandar_check(check):
    # print(f"{check}")
    dni, nombre, password, horas, turno_activo = mi_db.Trabajador.check_password(
        self=mi_db.Trabajador, password=check)
    empleado = mi_db.Trabajador()
    empleado.nombre = nombre
    empleado.dni = dni
    empleado.password = password
    empleado.horas_semanales = horas
    empleado.entrada = turno_activo
    if turno_activo == None:
        turno = messagebox.askokcancel(title="Confirmación",
                                       message=f"{nombre} va ha iniciar turno")
    else:
        turno = messagebox.askokcancel(
            title="Confirmación", message=f"{nombre} va ha cerrar turno")

    if turno == True and turno_activo == None:
        empleado.add_Turno_entrar()
        messagebox.showinfo(
            title="Turno Iniciado", message=f"{empleado.nombre} ha iniciado el turno")

    elif turno == True and turno_activo != None:
        empleado.add_Turno_salir()
        messagebox.showinfo(
            title="Turno Terminado", message=f"{empleado.nombre} ha terminado el turno\n")


def main():
    global n_digitos, password_check

    for i in range(3):
        for j in range(1, 4):
            texto_boton = str(i*3+j)
            ttk.Button(ventana_cronos, text=texto_boton, command=lambda tb=texto_boton: add_n_digitos(
                tb)).grid(row=i, column=j-1)
    texto_boton = "0"
    ttk.Button(ventana_cronos, text=texto_boton, command=lambda tb=texto_boton: add_n_digitos(
        tb)).grid(row=3, column=1)
    ttk.Button(ventana_cronos, text="OK", command=lambda pc=password_check: mandar_check(
        password_check)).grid(row=3, column=0)
    ttk.Button(ventana_cronos, text="Borrar", command=lambda: borrar_pantalla()
               ).grid(row=3, column=2)
    referencia.grid(row=4, column=1)
    # frm_cronos.pack()

    ventana_cronos.mainloop()


if __name__ == "__main__":
    main()
