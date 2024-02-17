import tkinter as tk
from tkinter import ttk, messagebox
import mi_db


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
        mensaje = f"Error al procesar petición, asegúrese de que NO está ya registrado\n{e}"
        messagebox.showerror("Error", mensaje)
    else:
        mensaje = f"""Agregado: {solicitud.nombre} DNI: {solicitud.dni}"""
        messagebox.showinfo("Agregado", mensaje)


def add_trabajador():
    ventana_add = tk.Toplevel()
    ventana_add.title("Agregar Trabajador")
    ttk.Label(ventana_add, text="Nombre").pack()
    nombre = ttk.Entry(ventana_add)
    nombre.pack()
    ttk.Label(ventana_add, text="DNI").pack()
    dni = ttk.Entry(ventana_add)
    dni.pack()
    ttk.Label(ventana_add, text="Password").pack()
    password = ttk.Entry(ventana_add)
    password.pack()
    ttk.Label(ventana_add, text="Horas Semanales").pack()
    horas_semanales = ttk.Entry(ventana_add)
    horas_semanales.pack()
    ttk.Button(ventana_add, text="Agregar", command=lambda pk=(
        nombre, dni, password, horas_semanales): enviar_mi_db(pk)).pack()
    ttk.Button(ventana_add, text="Salir", command=ventana_add.destroy).pack()


def show_trabajadores():
    ventana_show = tk.Toplevel()
    ventana_show.title("Lista Trabajadores")
    lista = []
    frm_show = ttk.Treeview(master=ventana_show,
                            columns=("Nº Trabajador", "DNI", "Nombre", "Password", "Horas Semanales"), selectmode="extended", show="headings")
    frm_show.heading(column=0, text="Nº Trabajador")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Nombre")
    frm_show.heading(column=3, text="Password")
    frm_show.heading(column=4, text="Horas Semanales")
    lista = mi_db.Trabajador.mostrar_Todos(lista)
    contador = 0
    for elemento in lista:
        frm_show.insert("", index=contador,
                        values=((contador+1), elemento[0], elemento[1], elemento[2], elemento[3]))
        contador += 1
    for i, item in enumerate(frm_show.get_children()):
        if i % 2 == 0:
            frm_show.item(item, tags=("even",))
        else:
            frm_show.item(item, tags=("odd",))
    # frm_show.column("DNI", width=100, anchor="w")
    # frm_show.column("Nombre", width=100)
    # frm_show.column("Password", width=100)
    # frm_show.column("Horas Semanales", width=100)
    frm_show.tag_configure("even", background="#f0f0f0", foreground="black")
    frm_show.tag_configure("odd", background="white", foreground="black")
    frm_show.pack()


def eliminar(dni):
    dni = dni.get()
    resultado = mi_db.eliminar_Trabajador(dni)
    print(resultado)


def del_trabajador():
    ventana_del = tk.Toplevel()
    ventana_del.title("Eliminar Trabajador")
    ttk.Label(ventana_del, text="DNI del trabajador").pack()
    dni = tk.Entry(ventana_del)
    dni.pack()
    ttk.Button(ventana_del, text="OK",
               command=lambda dni=dni: eliminar(dni)).pack()


def main():
    ventana_gestion = tk.Tk()
    ventana_gestion.title("")
    ventana_gestion.iconbitmap("gestion.ico")
    ventana_gestion.configure(highlightbackground="blue", highlightthickness=2)

    ttk.Button(ventana_gestion, text="Agregar Trabajador",
               command=add_trabajador).pack(expand=True)
    ttk.Button(ventana_gestion, text="Mostrar Todos los Trabajadores",
               command=show_trabajadores).pack(expand=True)
    ttk.Button(ventana_gestion, text="Eliminar Trabajador",
               command=del_trabajador).pack(expand=True)

    ventana_gestion.mainloop()


if __name__ == "__main__":
    main()
