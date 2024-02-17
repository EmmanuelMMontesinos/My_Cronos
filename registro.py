from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import modulos.mi_db as mi_db


def all_trabajadores():
    ventana_all = tk.Toplevel()
    lista = []
    frm_show = ttk.Treeview(master=ventana_all,
                            columns=("ID", "DNI", "Entrada", "Salida", "Total"), selectmode="extended", show="headings")

    frm_show.heading(column=0, text="Nº Registro")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Entrada")
    frm_show.heading(column=3, text="Salida")
    frm_show.heading(column=4, text="Total")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#f0f0f0",
                    foreground="black", rowheight=25)
    lista = mi_db.mostrar_all_horas()
    contador = 0
    for elemento in lista:
        try:
            frm_show.insert("", index=str(contador),
                            values=(contador, elemento[1], elemento[2], elemento[3],
                                    datetime.strptime(elemento[3], "%d/%m/%Y %H:%M:%S") - datetime.strptime(elemento[2], "%d/%m/%Y %H:%M:%S")))
        except TypeError:
            messagebox.showerror("Hay gente en Activo",
                                 "Los turnos que estan activos no aparecerán")
        contador += 1
    for i, item in enumerate(frm_show.get_children()):
        if i % 2 == 0:
            frm_show.item(item, tags=("even",))
        else:
            frm_show.item(item, tags=("odd",))
    # frm_show.column("DNI")
    # frm_show.column("Entrada", width=100)
    # frm_show.column("Salida", width=100)
    # frm_show.column("Total", width=100)
    frm_show.tag_configure("even", background="#f0f0f0", foreground="black")
    frm_show.tag_configure("odd", background="white", foreground="black")
    frm_show.pack()


def details_one_trabajadores(dni):
    ventana_one = tk.Toplevel()
    lista = []
    frm_show = ttk.Treeview(master=ventana_one,
                            columns=("ID", "DNI", "Entrada", "Salida", "Total"), selectmode="extended", show="headings")

    frm_show.heading(column=0, text="Nº Registro")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Entrada")
    frm_show.heading(column=3, text="Salida")
    frm_show.heading(column=4, text="Total")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#f0f0f0",
                    foreground="black", rowheight=25)
    lista = mi_db.mostrar_one_horas(dni)
    contador = 0
    for elemento in lista:
        try:
            frm_show.insert("", index=str(contador),
                            values=(contador, elemento[1], elemento[2], elemento[3],
                                    datetime.strptime(elemento[3], "%d/%m/%Y %H:%M:%S") - datetime.strptime(elemento[2], "%d/%m/%Y %H:%M:%S")))
        except TypeError:
            messagebox.showerror("Hay gente en Activo",
                                 "Los turnos que estan activos no aparecerán")
        contador += 1
    for i, item in enumerate(frm_show.get_children()):
        if i % 2 == 0:
            frm_show.item(item, tags=("even",))
        else:
            frm_show.item(item, tags=("odd",))
    # frm_show.column("DNI")
    # frm_show.column("Entrada", width=100)
    # frm_show.column("Salida", width=100)
    # frm_show.column("Total", width=100)
    frm_show.tag_configure("even", background="#f0f0f0", foreground="black")
    frm_show.tag_configure("odd", background="white", foreground="black")
    frm_show.pack()


def one_trabajadores():
    ventana_sni = tk.Toplevel()
    dni = ttk.Combobox(ventana_sni, background="green")
    lista_all_2 = []
    lista_all = mi_db.Trabajador.mostrar_Todos(lista_all_2)
    lista_all_2.append([x[0] for x in lista_all if x[1] not in lista_all_2])
    dni.config(values=lista_all_2[0])
    dni.pack()
    ttk.Button(ventana_sni, text="Ok",
               command=lambda dni=dni: details_one_trabajadores(dni.get())).pack()
    ventana_sni.mainloop()


def main():
    ventana = tk.Tk()
    ventana.title("")
    ventana.iconbitmap("registro.ico")

    ttk.Button(ventana, text="Mostrar Registro Global",
               command=all_trabajadores).pack()
    ttk.Button(ventana, text="Mostrar Registro de Trabajador",
               command=one_trabajadores).pack()
    ventana.mainloop()


if __name__ == "__main__":
    main()
