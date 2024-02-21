import tkinter as tk
from tkinter import ttk, messagebox
import modules.mi_db as mi_db


def send_mi_db(pk):
    """Manages the ENTRY of a NEW worker to the DB"""
    name, dni, turn_id_entry, hour_week = pk
    request = mi_db.Worker()
    request.name = name.get()
    request.dni = dni.get()
    request.turn_id_entry = turn_id_entry.get()
    request.hour_week = hour_week.get()
    try:
        request.add_worker()
    except Exception as e:
        response = f"Error al procesar petición, asegúrese de que NO está ya registrado\n{e}"
        messagebox.showerror("Error", response)
    else:
        response = f"""Agregado: {request.name} DNI: {request.dni}"""
        messagebox.showinfo("Agregado", response)


def send_mi_db_update(pk, dni):
    request = mi_db.Worker()
    request.dni = dni
    name, dni, turn_id_entry, hours_week = pk
    update = {"name": name.get(), "dni": dni.get(),
              "turn_id_entry": turn_id_entry.get(), "hours_week": hours_week.get()}
    request.update_worker(update)
    messagebox.showinfo(title="Trabajador modificado",
                        message=f"{name.get()} {dni.get()} ha sido actualizado")


def add_worker():
    """Add Worker window"""
    window_add = tk.Toplevel()
    window_add.title("Agregar Trabajador")
    ttk.Label(window_add, text="Nombre").pack()
    name = ttk.Entry(window_add)
    name.pack()
    ttk.Label(window_add, text="DNI").pack()
    dni = ttk.Entry(window_add)
    dni.pack()
    ttk.Label(window_add, text="Identificador de Turno").pack()
    turn_id_entry = ttk.Entry(window_add)
    turn_id_entry.pack()
    ttk.Label(window_add, text="Horas Semanales").pack()
    hour_week = ttk.Entry(window_add)
    hour_week.pack()
    ttk.Button(window_add, text="Agregar", command=lambda pk=(
        name, dni, turn_id_entry, hour_week): send_mi_db(pk)).pack()
    ttk.Button(window_add, text="Salir", command=window_add.destroy).pack()


def show_workers():
    """window of Show ALL Workers"""
    window_show = tk.Toplevel()
    window_show.title("list_workers Trabajadores")
    list_workers = []
    frm_show = ttk.Treeview(master=window_show,
                            columns=("Nº Trabajador", "DNI", "Nombre", "turn_id_entry", "Horas Semanales"), selectmode="extended", show="headings")
    frm_show.heading(column=0, text="Nº Trabajador")
    frm_show.heading(column=1, text="DNI")
    frm_show.heading(column=2, text="Nombre")
    frm_show.heading(column=3, text="Identificador de turno")
    frm_show.heading(column=4, text="Horas Semanales")
    list_workers = mi_db.Worker.show_all(list_workers)
    count = 0
    for element in list_workers:
        frm_show.insert("", index=count,
                        values=((count+1), element[0], element[1], element[2], element[3]))
        count += 1
    for i, item in enumerate(frm_show.get_children()):
        if i % 2 == 0:
            frm_show.item(item, tags=("even",))
        else:
            frm_show.item(item, tags=("odd",))
    # frm_show.column("DNI", width=100, anchor="w")
    # frm_show.column("name", width=100)
    # frm_show.column("turn_id_entry", width=100)
    # frm_show.column("Horas Semanales", width=100)
    frm_show.tag_configure("even", background="#f0f0f0", foreground="black")
    frm_show.tag_configure("odd", background="white", foreground="black")
    frm_show.pack()


def delete(dni, window) -> None:
    """delete worker"""
    dni = dni.get()
    worker = mi_db.Worker()
    worker.dni = dni
    elements = worker.show_all()
    for element in elements:
        if dni in element[0]:
            response = worker.delete_worker()
            print(response)
            messagebox.showinfo(title="Borrado Exitoso",
                                message=f"{dni} ha sido borrado")
            window.destroy()
            return

    messagebox.showerror(
        title="Error", message=f"{dni} NO existe en la Base de Datos")
    window.destroy()


def del_worker():
    """window to delete Worker for a DNI"""
    window_del = tk.Toplevel()
    window_del.title("Eliminar Trabajador")
    ttk.Label(window_del, text="DNI del trabajador").pack()
    dni = tk.Entry(window_del)
    dni.pack()
    ttk.Button(window_del, text="OK",
               command=lambda dni=dni: delete(dni, window_del)).pack()


def upgrade_worker(dni, window):
    dni_old = dni.get()
    if dni_old == "":
        return messagebox.showerror(message="Introduzca un DNI")
    window_upgrade = tk.Toplevel()
    worker = mi_db.Worker()
    worker.dni = dni.get()
    try:
        result = worker.show_worker()
        ttk.Label(window_upgrade, text="Nombre").pack()
        name = ttk.Entry(window_upgrade)
        name.pack()
        ttk.Label(window_upgrade, text="DNI").pack()
        dni = ttk.Entry(window_upgrade)
        dni.pack()
        ttk.Label(window_upgrade, text="Identificador de Turno").pack()
        turn_id_entry = ttk.Entry(
            window_upgrade)
        turn_id_entry.pack()
        ttk.Label(window_upgrade, text="Horas Semanales").pack()
        hour_week = ttk.Entry(window_upgrade)
        hour_week.pack()
        ttk.Button(window_upgrade, text="Agregar", command=lambda pk=(
            name, dni, turn_id_entry, hour_week): send_mi_db_update(pk, dni_old)).pack()
        ttk.Button(window_upgrade, text="Salir",
                   command=window_upgrade.destroy).pack()
        window.destroy()
    except Exception as e:
        messagebox.showerror(
            message=f"{dni_old} no existe en la Base de Datos\n{e}")
        window_upgrade.destroy()
        window.destroy()


def update_worker():
    window_update = tk.Toplevel()
    window_update.title("Editar Trabajador")
    ttk.Label(window_update, text="DNI del trabajador").pack()
    dni = tk.Entry(window_update)
    dni.pack()

    ttk.Button(window_update, text="OK", command=lambda dni=dni:
               upgrade_worker(dni, window_update)).pack()


def main():
    """window main"""
    window_gestion = tk.Tk()
    window_gestion.title("")
    window_gestion.iconbitmap("gestion.ico")
    window_gestion.configure(highlightbackground="blue", highlightthickness=2)

    ttk.Button(window_gestion, text="Agregar Trabajador",
               command=add_worker).pack(expand=True)
    ttk.Button(window_gestion, text="Mostrar Todos los Trabajadores",
               command=show_workers).pack(expand=True)
    ttk.Button(window_gestion, text="Editar Trabajador",
               command=update_worker).pack(expand=True)
    ttk.Button(window_gestion, text="Eliminar Trabajador",
               command=del_worker).pack(expand=True)

    window_gestion.mainloop()


if __name__ == "__main__":
    main()
