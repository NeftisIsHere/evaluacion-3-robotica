from json import *
from funciones import *
from pwinput import pwinput
import tabulate



# Menú principal
acceso = False
limpiar_pantalla()
print("Bienvenido al programa de manejo de datos de CEMEX Ventures")

while acceso == False:
    print("MENU\n1) Iniciar sesión\n2) Registrar Usuario\n3) Salir")
    print("Ingrese la opción a ejecutar")
    opcion = validar_numero()
    
    if opcion == 1:
        # Iniciar sesión
        limpiar_pantalla()

        # Se quitan los espacios al inicio y final del username.
        user = input("Ingrese el nombre de usuario:\n").strip()
        # Se usa pwinput para más privacidad.
        password = pwinput("Ingrese la contraseña:\n", )
        # Se llama la función que verifica y permite el acceso al programa.
        acceso=verificar_usuario(user, password)
        
    elif opcion == 2:
        # Registrarse
        limpiar_pantalla()
        # Se quitan los espacios al inicio y final del username.
        user = input("Ingrese el nombre de usuario:\n").strip()
        password = pwinput("Ingrese la contraseña:\n")
        
        # Se llama la función para crear el nuevo usuario
        registrar_usuario(user,password)
        print("Usuario Registrado correctamente.")
        
    elif opcion == 3:
        # Salir
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción invalida.")        
    input("Presiona enter para continuar.")
    limpiar_pantalla()

while acceso == True:
    print("ADMINISTRADOR DE PROYECTOS\n1) Crear nuevo proyecto\n2) Editar proyecto existente\n3) Eliminar Proyecto\n4) Generar reporte\n5) Salir")
    print("Ingrese la opción a ejecutar:")
    opcion = validar_numero()

    if opcion == 1:
        limpiar_pantalla()
        print("Creando nuevo proyecto.")
        nombre = input("Introduce el nombre del proyecto:\n").strip()
        print("Introduce la cantidad de hormigón utilizado (KG):")
        material = validar_numero()
        print("Introduce la cantidad de fallas técnicas ocurridas durante el proyecto:")
        fallas = validar_numero()
        while True:
            print("Ingrese estado del proyecto:\n1) Completado\n2) En progreso\n3) Finalizado")
            numero_estado = validar_numero()
            if numero_estado == 1:
                estado = "Completado"
                break
            elif numero_estado == 2:
                estado = "En progreso"
                break
            elif numero_estado== 3:
                estado = "Cancelado"
                break
            else:
                print("Opción inválida.")
        crear_proyecto(nombre, material, fallas, estado)
            
    elif opcion == 2:
        limpiar_pantalla()
        modificar_proyecto()
      
    elif opcion == 3:
        limpiar_pantalla()     
        borrar_proyecto()


    elif opcion == 4:
        mostrar_tabla_completa()

    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")

    input("Presiona enter para continuar.")
    limpiar_pantalla()


