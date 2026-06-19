# Modulo que usaré para trabajar con las fechas
from datetime import datetime


def cargar_empleados():
    """Carga los empleados desde el archivo CSV y devuelve una lista de diccionarios."""

    empleados = []

    try:
        with open("empleados.csv", "r", encoding="utf-8") as archivo:
            next(archivo)  # Salta la línea del encabezado

            for linea in archivo:
                try:

                    legajo, nombre, saldo = linea.strip().split(",")

                    empleado = {
                        "legajo": legajo,
                        "nombre": nombre,
                        "saldo": int(saldo)
                    }

                    empleados.append(empleado)

                except ValueError as error:
                    # Se produce si faltan columnas o si saldo no puede convertirse a entero.
                    print(
                        f"Ha ocurrido un error al procesar la línea: {error}")

        return empleados

    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")


def carga_solicitud():
    """Carga las solicitudes de vacaciones registradas en el archivo CSV."""

    solicitudes = []

    try:
        with open("vacaciones.csv", "r", encoding="utf-8") as archivo:
            next(archivo)  # Saltea el encabezado

            for linea in archivo:
                try:

                    legajo, fecha, estado = linea.strip().split(",")

                    solicitud = {
                        "legajo": legajo,
                        "fecha": fecha,
                        "estado": estado
                    }

                    solicitudes.append(solicitud)

                except ValueError:
                    print(f"Linea con formato incorrecto: {linea.strip()}")

        return solicitudes

    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")


def validar_legajo(empleados):
    """Solicita un legajo y verifica que exista en la lista de empleados."""

    while True:

        try:
            id = input("Ingrese su legajo: ")

            if not id.isdigit():
                raise ValueError("El legajo debe ser numérico.")

        except ValueError as error:
            print("Ha ocurrido el siguiente error:", error)
            continue

        for empleado in empleados:
            if empleado["legajo"] == id:

                print("\n🤖 Legajo validado correctamente.")
                return id

        print("Legajo no encontrado, intente nuevamente.")


def consultar_saldo(legajo, empleados):
    """Consulta si el empleado posee días de vacaciones disponibles."""

    for empleado in empleados:

        if empleado["legajo"] == legajo:

            if empleado["saldo"] > 0:

                print(
                    f"\n🤖 Actualmente disponés de {empleado['saldo']} días de vacaciones."
                )

                return True

            else:
                return False


def solicitar_validar_dias(legajo, empleados):
    """Solicita la cantidad de días y valida que no excedan el saldo disponible."""

    saldo = 0

    for empleado in empleados:

        if empleado["legajo"] == legajo:
            saldo = empleado["saldo"]

    while True:

        dias = input("\n¿Cuantos dias de vacaciones querés solicitar?\n>>> ")

        if not dias.isdigit():
            print("Error, ingresá un numero entero válido.")
            continue

        dias = int(dias)

        if dias <= saldo:

            print("\n🤖 Cantidad de días válida.")
            return dias

        else:
            print("No tenés los días suficientes, intenta con menos.")


def solicitar_fecha():
    """Solicita una fecha y valida que respete el formato dd/mm/aaaa."""

    while True:

        try:

            fecha = input("\nIngresá la fecha de inicio (dd/mm/aaaa): ")

            # Verifica formato y validez de la fecha ingresada.
            datetime.strptime(fecha, "%d/%m/%Y")

            return fecha

        except ValueError:
            print("Fecha inválida. Intente nuevamente.")


def fecha_disponible(fecha):
    """Verifica que la fecha solicitada no se encuentre pendiente o aprobada."""

    solicitudes = carga_solicitud()

    for solicitud in solicitudes:

        if solicitud["estado"] in ("pendiente", "aprobada"):

            if solicitud["fecha"] == fecha:
                return False

    return True


def revisar_solicitud_rrhh():
    """Simula la revisión de la solicitud por parte de RRHH."""

    print("\n🤖 Enviando solicitud a Recursos Humanos...")
    print("🤖 Solicitud recibida por RRHH.")
    print("🤖 RRHH está revisando la solicitud...")

    return "aprobada"


def enviar_rrhh(legajo, fecha):
    """Envía la solicitud a RRHH y registra el resultado final."""

    try:

        estado = revisar_solicitud_rrhh()

        with open("vacaciones.csv", "a", encoding="utf-8") as archivo:

            archivo.write(f"\n{legajo},{fecha},{estado}")

        print("\n🤖 Tu solicitud fue aprobada.")
        print("🤖 Las vacaciones fueron registradas correctamente.")
        print(f"🤖 Fecha de inicio aprobada: {fecha}")

    except Exception as error:

        print(f"Se produjo un error al registrar la solicitud: {error}")


def chatbot_vacaciones():
    """Coordina el flujo completo de solicitud de vacaciones."""

    print("\n🤖 Bot de Gestión de Vacaciones")
    print("Hola. Voy a ayudarte a gestionar tu solicitud de vacaciones.\n")

    empleados = cargar_empleados()

    legajo = validar_legajo(empleados)

    if not consultar_saldo(legajo, empleados):
        print("No posee días disponibles.")
        return

    dias = solicitar_validar_dias(legajo, empleados)

    while True:

        fecha = solicitar_fecha()

        if fecha_disponible(fecha):

            enviar_rrhh(legajo, fecha)
            break

        else:

            print("\n🤖 La fecha seleccionada ya se encuentra registrada.")
            print("🤖 Por favor, seleccioná otra fecha.")


# Main
chatbot_vacaciones()
