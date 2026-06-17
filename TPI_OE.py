def cargar_empleados():
    empleados= []
    try:
        with open("empleados.csv", "r", encoding= "utf-8")as archivo:
            next(archivo) # Hace que salte la linea del encabezado
            
            for linea in archivo:
                legajo, nombre, saldo = linea.strip().split(",")
                
                try:
                    empleado = {
                        "legajo": legajo,
                        "nombre": nombre,
                        "saldo": int(saldo)
                    }

                    
                    empleados.append(empleado)
                
                except ValueError as error: # Maneja el error si en el csv en la columna saldo no hay un int
                    print(f"Ha ocurrido un error de conversion: {error}")
                
                except KeyError as error: # Maneja un error en el csv, por si falta una columna
                    print(f"Falta la columna: {error}")
                

                
        return empleados
    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")

def carga_solicitud():
    solicitudes = []

    try:
        with open("solicitudes.csv", "r", encoding= "utf-8") as archivo:
            next(archivo) # Saltea el encabezado

            try:    
                for linea in archivo:
                    legajo, fecha, estado= linea.strip().split(",")

                    solicitud = {
                        "legajo": legajo,
                        "fecha": fecha,
                        "estado": estado
                        }
                    solicitudes.append(solicitud)
                    
            except ValueError as error: # Maneja un error en el csv, por si falta una columna
                    print(f"Linea con formato incorrecto: {linea.strip()}")
                    
        return solicitudes
        
    except FileNotFoundError:
        print("El archivo no existe en la ubicación brindada.")
    
def validar_legajo(empleados):
    try:
        id = input("Ingrese su legajo: ")

        if not id.isdigit():
            raise ValueError ("El legajo debe ser numérico.")
    
    except ValueError as error:
        print(error)
        return False

    for empleado in empleados:
        if empleado["legajo"] == id :
            return True
    
    return False


        




