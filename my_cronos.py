from tkinter import *
from tkinter import ttk, messagebox
import modules.mi_db as mi_db


"""This is the turn_id_activate dialer window."""
digit_reference = ""
turn_id_check = ""
window_cronos = Tk()
window_cronos.title("Cronos")
window_cronos.iconbitmap("cronos.ico")
window_cronos.config(background="green")
frm_cronos = ttk.Frame(window_cronos, padding=20)

refernce = ttk.Label(window_cronos, text=digit_reference, background="green")
# Window of Cronos


def add_digit_reference(text_button):
    """Adds a digit if a button with a number is pressed."""
    global digit_reference, turn_id_check
    digit_reference += "*"
    turn_id_check += text_button
    refernce.config(text=digit_reference)


def key_press(event):
    if event.char.isdigit() and "0" <= event.char <= "9":
        text_button = event.char
        add_digit_reference(text_button)


def borrar_pantalla():
    global turn_id_check, digit_reference
    turn_id_check = ""
    digit_reference = ""
    refernce.config(text=digit_reference)

# Desde aqui comprueba el id(dni)


def send_check(check):
    # print(f"{check}")
    try:
        dni, name, turn_id_activate, hours, turn_on = mi_db.Worker.check_id_turn(
            self=mi_db.Worker, id_turn=check)
        worker_person = mi_db.Worker()
        worker_person.name = name
        worker_person.dni = dni
        worker_person.turn_id_activate = turn_id_activate
        worker_person.hours_semanales = hours
        worker_person.entry = turn_on
        if turn_on == None:
            turno = messagebox.askokcancel(title="Confirmación",
                                           message=f"{name} va ha iniciar turno")

        else:
            turno = messagebox.askokcancel(
                title="Confirmación", message=f"{name} va ha cerrar turno")

        if turno == True and turn_on == None:
            worker_person.add_turn_entry()
            messagebox.showinfo(
                title="Turno Iniciado", message=f"{worker_person.name} ha iniciado el turno")
            borrar_pantalla()

        elif turno == True and turn_on != None:
            worker_person.add_turn_out()
            messagebox.showinfo(
                title="Turno Terminado", message=f"{worker_person.name} ha terminado el turno\n")
            borrar_pantalla()
    except Exception as e:
        messagebox.showerror(
            f"{e}", "No hay trabajadores en la Base de Datos, puede añadirlos desde el programa gestión")


def main():
    global digit_reference, turn_id_check

    for i in range(3):
        for j in range(1, 4):
            text_button = str(i*3+j)
            ttk.Button(window_cronos, text=text_button, command=lambda tb=text_button: add_digit_reference(
                tb)).grid(row=i, column=j-1)
    text_button = "0"
    ttk.Button(window_cronos, text=text_button, command=lambda tb=text_button: add_digit_reference(
        tb)).grid(row=3, column=1)
    ttk.Button(window_cronos, text="OK", command=lambda pc=turn_id_check: send_check(
        turn_id_check)).grid(row=3, column=0)
    ttk.Button(window_cronos, text="Borrar", command=lambda: borrar_pantalla()
               ).grid(row=3, column=2)
    refernce.grid(row=4, column=1)
    # frm_cronos.pack()

    window_cronos.mainloop()


if __name__ == "__main__":
    main()
