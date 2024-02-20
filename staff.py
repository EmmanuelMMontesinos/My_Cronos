import modules.mi_db as my_db


__staff = my_db.Staff.all_staff(self=my_db.Staff())


def update_staff() -> dict:
    global __staff
    __staff = my_db.Staff.all_staff(self=my_db.Staff())


def check_worker(dni) -> list:
    worker = my_db.Worker()
    worker.dni = dni
    result = worker.show_worker()
    if dni == result[0]:
        return True
    else:
        return False


def add_staff():
    print("Esta es una funcion para staff del negocio,\nsi usted no es parte del mismo podria estar incurriendo en un delito.")
    print("1-Continuar 2-Cerrar programa")
    confirmation = input("")
    if int(confirmation) == 1:
        dni = input("Ponga el DNI del trabajador que desea hacer Staff:\n")
        if check_worker(dni):
            password = input(f"Ingrese una contraseña para {dni}: ")
            staff_worker = my_db.Staff()
            staff_worker.dni, staff_worker.password = dni, password
            response = staff_worker.add_staff()
            print(response)
            input("Presione Intro para Salir")
            update_staff()
            print(dict(__staff))
            return


def show_staff() -> str:
    for element in __staff:
        print(f"{element[0]} --- {element[1]}")


def perfile_staff() -> None:
    dni = input("Ingrese su dni como staff: ")
    password = input("Ingrese su contraseña: ")
    request = my_db.Staff()
    request.dni, request.password = dni, password
    response = request.check_password()
    if response:
        print("Tus datos han sido validados correctamente")
    elif not response:
        print("Error: Contraseña invalida")
    else:
        print("Error: No consta como staff")


perfile_staff()
