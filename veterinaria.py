import random

registros = {}

def validar_id(id_mascota):
    if id_mascota.isdigit() and len(id_mascota) == 5:
        return True
    else:
        return False

def registrar_mascota():
    id_mascota = input("Ingrese el ID de la mascota: ")
    while not validar_id(id_mascota):
        print("ID inválido. Debe ser numérico y tener una longitud de 5 caracteres.")
        id_mascota = input("Ingrese el ID de la mascota: ")

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    while nombre_mascota.strip() == "":
        print("El nombre de la mascota no puede estar vacío.")
        nombre_mascota = input("Ingrese el nombre de la mascota: ")

    nombre_dueno = input("Ingrese el nombre del dueño: ")
    while nombre_dueno.strip() == "":
        print("El nombre del dueño no puede estar vacío.")
        nombre_dueno = input("Ingrese el nombre del dueño: ")

    tipo = input("Ingrese el tipo de mascota (Perro o Gato): ")
    while tipo.lower() != "perro" and tipo.lower() != "gato":
        print("Tipo de mascota inválido. Debe ser 'Perro' o 'Gato'.")
        tipo = input("Ingrese el tipo de mascota (Perro o Gato): ")

    if id_mascota not in registros:
        registros[id_mascota] = {
            "nombre_mascota": nombre_mascota,
            "nombre_dueno": nombre_dueno,
            "tipo": tipo.lower()
        }
        print("Mascota registrada con éxito.")
    else:
        print("El ID de la mascota ya está en uso.")

def listar_registros():
    if len(registros) == 0:
        print("No hay registros de mascotas.")
    else:
        print("Registros de mascotas:")
        for id_mascota, datos in registros.items():
            print(f"ID Mascota: {id_mascota}")
            print(f"Nombre: {datos['nombre_mascota']}")
            print(f"Tipo: {datos['tipo']}")
            print(f"Dueño de la Mascota:")
            print(f"Sr/a: {datos['nombre_dueno']}")
            print(f"A su mascota le faltan {random.randint(1, 10)} vacunas")
            print("---------------------")

def buscar_mascota():
    id_mascota = input("Ingrese el ID de la mascota que desea buscar: ")
    if id_mascota in registros:
        datos = registros[id_mascota]
        print(f"ID Mascota: {id_mascota}")
        print(f"Nombre: {datos['nombre_mascota']}")
        print(f"Tipo: {datos['tipo']}")
        print(f"Dueño de la Mascota:")
        print(f"Sr/a: {datos['nombre_dueno']}")
        print(f"A su mascota le faltan {random.randint(1, 10)} vacunas")
    else:
        print("No se encontró una mascota con ese ID.")

def imprimir_reportes():
    tipo_mascota = input("¿De qué tipo de mascota desea ver los reportes? (1. Perros, 2. Gatos): ")
    while tipo_mascota != "1" and tipo_mascota != "2":
        print("Opción inválida.")
        tipo_mascota = input("¿De qué tipo de mascota desea ver los reportes? (1. Perros, 2. Gatos): ")

    tipo_mascota = "perro" if tipo_mascota == "1" else "gato"
    contador_mascotas = 0

    print("REPORTES")
    for id_mascota, datos in registros.items():
        if datos["tipo"] == tipo_mascota:
            contador_mascotas += 1
            print(f"ID Mascota: {id_mascota}")
            print(f"Nombre: {datos['nombre_mascota']}")
            print(f"Tipo: {datos['tipo']}")
            print(f"Dueño de la Mascota:")
            print(f"Sr/a: {datos['nombre_dueno']}")
            print(f"A su mascota le faltan {random.randint(1, 10)} vacunas")
            print("---------------------")

    print(f"Hay en total {contador_mascotas} {tipo_mascota}s Registrados.")

while True:
    print("----- MENÚ -----")
    print("1. Grabar/Registrar Mascota")
    print("2. Listar Todos los registros")
    print("3. Buscar Mascota")
    print("4. Imprimir Reportes por tipo mascota")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_mascota()
    elif opcion == "2":
        listar_registros()
    elif opcion == "3":
        buscar_mascota()
    elif opcion == "4":
        imprimir_reportes()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")
