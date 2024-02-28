import modules.mi_db as my_db


__staff = {}


def update_staff() -> dict:
    global __staff
    __staff = my_db.Staff.all_staff(self=my_db.Staff())
    return __staff


def check_worker(dni) -> list:
    worker = my_db.Worker()
    worker.dni = dni
    result = worker.show_worker()
    if result == None:
        return False
    if dni == result[0]:
        return True
    else:
        return False


def add_staff() -> None:
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
        else:
            print("Error: El usuario debe existir en la base de datos y no ser ya staff")
            input("Enter para continuar")


def show_staff() -> str:
    for element in __staff:
        print(f"{element[0]} --- {element[1]}")


def delete_staff(dni) -> str:
    staff = my_db.Staff()
    staff.dni = dni
    list_staff = update_staff()
    for staff_worker in list_staff:
        if dni in staff_worker[0]:
            print(f"{staff.delete_staff()}")
        else:
            print(f"Error, {dni} no consta como Staff")


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


def main() -> None:
    print("Bienveido al asistente de credenciales Staff para my_cronos server")
    check_exit = False
    while not check_exit:
        print("1-Añadir Trabajador a Staff")
        print("2-Mostrar todos los Staff con su hash")
        print("3-Validar staff")
        print("4-Borrar staff")
        print("0-Salir")
        select = input("")
        if int(select) == 1:
            add_staff()
        elif int(select) == 2:
            try:
                for staff in update_staff():
                    print(f"ID Staff: {staff[0]}")
                    print(f"Hash Staff: {staff[1]}")
            except Exception as e:
                print(F"Error: {e}")
        elif int(select) == 3:
            perfile_staff()
        elif int(select) == 4:
            dni = input("Ponga el DNI que quiere borrar: ")
            delete_staff(dni)
        elif int(select) == 0:
            check_exit = True


if __name__ == "__main__":
    main()
