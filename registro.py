import tkinter as tk
from tkinter import ttk, messagebox


def all_trabajadores():
    ventana = tk.Toplevel()


def main():
    ventana = tk.Tk()
    ventana.title("Registro de Horas")
    ventana.iconbitmap("registro.ico")
    ttk.Button(ventana, text="Global", command=all_trabajadores)
    ttk.Button(ventana, text="Trabajador", command=one_trabajadores)


if __name__ == "__main__":
    main()
