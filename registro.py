from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, messagebox
import modules.mi_db as mi_db
import modules.export_pdf_excel as pdf_conversor


def all_workers():
    """Window displaying ALL shifts of ALL Workers"""
    window_all = tk.Toplevel()
    list_all_workers = []
    frm_show = ttk.Treeview(master=window_all,
                            columns=("ID", "DNI", "Entrada", "Salida", "Total"), selectmode="extended", show="headings")

    frm_show.heading(column=0, text="Nº Registro")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Entrada")
    frm_show.heading(column=3, text="Salida")
    frm_show.heading(column=4, text="Total")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#f0f0f0",
                    foreground="black", rowheight=25)
    list_all_workers = mi_db.show_all_turns_all_workers()
    count = 0
    for element in list_all_workers:
        try:
            frm_show.insert("", index=str(count),
                            values=(count, element[1], element[2], element[3],
                                    datetime.strptime(element[3], "%d/%m/%Y %H:%M:%S") - datetime.strptime(element[2], "%d/%m/%Y %H:%M:%S")))
        except TypeError:
            messagebox.showerror("Hay gente en Activo",
                                 "Los turnos que estan activos no aparecerán")
        count += 1
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


def datails_one_worker(dni):
    """Window that SHOWS the details of ONE Worker"""
    window_one = tk.Toplevel()
    list_all_workers = []
    frm_show = ttk.Treeview(master=window_one,
                            columns=("ID", "DNI", "Entrada", "Salida", "Total"), selectmode="extended", show="headings")

    frm_show.heading(column=0, text="Nº Registro")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Entrada")
    frm_show.heading(column=3, text="Salida")
    frm_show.heading(column=4, text="Total")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#f0f0f0",
                    foreground="black", rowheight=25)
    list_all_workers = mi_db.show_all_turns_one_worker(dni)
    count = 0
    for element in list_all_workers:
        try:
            frm_show.insert("", index=str(count),
                            values=(count, element[1], element[2], element[3],
                                    datetime.strptime(element[3], "%d/%m/%Y %H:%M:%S") - datetime.strptime(element[2], "%d/%m/%Y %H:%M:%S")))
        except TypeError:
            messagebox.showerror("Hay gente en Activo",
                                 "Los turnos que estan activos no aparecerán")
        count += 1
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


def one_workers():
    """SELECT DNI window to show ONE worker the shifts."""
    window_sni = tk.Toplevel()
    dni = ttk.Combobox(window_sni, background="green")
    list_all_workers_all_2 = []
    list_all_workers_all = mi_db.Worker.show_all(
        list_all_workers_all_2)
    list_all_workers_all_2.append(
        [x[0] for x in list_all_workers_all if x[1] not in list_all_workers_all_2])
    dni.config(values=list_all_workers_all_2[0])
    dni.pack()
    ttk.Button(window_sni, text="Ok",
               command=lambda dni=dni: datails_one_worker(dni.get())).pack()
    window_sni.mainloop()


def select_path(filename="Turnos"):
    if filename == "":
        filename = "My_Cronos_Turns"
    path = filedialog.askdirectory()
    save(path, filename)


def save(path, filename):
    print(path)
    pdf = mi_db.show_all_turns_all_workers()
    pdf_conversor.create_pdf(
        filename=filename, info_data=pdf, path=path)
    messagebox.showinfo(
        "PDF guardado", f"El informe en PDF ha sido guardado en {path}/{filename}")


def info_all():
    window_info_all = tk.Toplevel()
    ttk.Label(window_info_all, text="Guardar como:").pack()
    filename = ttk.Entry(window_info_all)
    filename.pack()
    path = ttk.Button(window_info_all, text="Carpeta",
                      command=lambda: select_path(filename.get()))

    path.pack()

    window_info_all.mainloop()


def info_one():
    pass


def main():
    window = tk.Tk()
    window.title("")
    window.iconbitmap("registro.ico")

    ttk.Button(window, text="Mostrar Registro Global",
               command=all_workers).pack()
    ttk.Button(window, text="Mostrar Registro de Trabajador",
               command=one_workers).pack()
    ttk.Button(window, text="Informe Global de Trabajadores",
               command=info_all).pack()
    ttk.Button(window, text="Informe de Trabajador",
               command=info_one).pack()
    window.mainloop()


if __name__ == "__main__":
    main()
