# Librerías estandar
from datetime import datetime
import json
from pathlib import Path
import platform
import subprocess
# Librerías de terceros
import bcrypt
from prettytable import PrettyTable



def limpiar_pantalla():
    # Se usa el comando adecuado para limpiar la consola según el sistema operativo.
    if platform.system() == 'Windows':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)


def validar_numero():
    # Codigo bastante auto explicatorio, se verifica que sea tanto positivo como un numero.
    while True:
        try:
            opcion = int(input("").strip())
            if opcion >= 0:
                return opcion
            print("Error, el número debe ser positivo.")
        except:
            print("Por favor, ingrese un valor numerico.")
       
# =======================================================================
# MANEJO DE USUARIOS
# =======================================================================

def registrar_usuario(usuario, password):
    limpiar_pantalla()
    # se pasa la contraseña a bytes:
    byte_password = password.encode('utf-8')
    # La key es el saltaedo que se usa para que incluso 2 contraseñas identicas tengan distinto hash.
    key = bcrypt.gensalt()
    # Se encripta la contraseña y convierte a texto
    hashed_password = bcrypt.hashpw(byte_password,key).decode('utf-8')
    
    archivo_usuarios = Path('./datos/users.json')
    
    # Cargar la lista de usuarios desde el json a un diccionario,
    # De no existir o estar vacía, se crea una lista nueva.
    try:
        with open(archivo_usuarios, "r") as archivo:
            lista_usuarios = json.load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado, creando lista de usuarios.")
        lista_usuarios = {}
    except json.JSONDecodeError:
        print("Creando nueva lista")
        lista_usuarios = {}
    
    
    # En caso de existir ya el usuario, no se realizan cambios. De lo contrario, se guarda en el archivo .json
    if usuario in lista_usuarios:
        print("El usuario ya existe")
    else:
        lista_usuarios[usuario] = hashed_password
        with open(archivo_usuarios, "w") as archivo:
            json.dump(lista_usuarios, archivo, indent=4)
 
 
def verificar_usuario(usuario, password):
    limpiar_pantalla
    archivo_usuarios = Path('./datos/users.json')
    
    try:
        with open(archivo_usuarios, "r") as lista_usuarios:
            diccionario = json.load(lista_usuarios)
            
            # Si el usuario se encuentra en el diccionario, se verifica que el hash corresponda a el usuario
            # Si no corresponden, devuelve el error correspondiente.
            if usuario in diccionario:
                password = password.encode('utf-8')
                hashed_password = diccionario[usuario].encode('utf-8')
                # Se convierten la contraseña ingresada y el hash de la contraseña a bytes y se comparan.
                if bcrypt.checkpw(password,hashed_password):
                    return True
                else:
                    print("Contraseña incorrecta")
                    return False
            else:
                print("Usuario Incorrecto")
                return False
                        
    except json.JSONDecodeError as e:
        print("No existen usuarios.")
        return False


# =======================================================================
# FIN DE MANEJO DE USUARIOS
# =======================================================================
# MANEJO DE JSONS
# =======================================================================


def cargar_proyectos():
    try:
        # Se abre el archivo .json y devuelve los datos de este como diccionario
        with open('./datos/proyectos.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no se encuentra el archivo o hay problemas abriendolo, devuelve un diccionario vacío
        return {}


def guardar_proyecto(proyectos: dict):
    try:
        # Se abre el .json, se guardan los datos y devuelve verdadero para indicar que fue exitoso.
        with open('./datos/proyectos.json', "w") as f:
            json.dump(proyectos, f, indent=4)
            return True
    except Exception as e:
        # Se imprime el error en caso de no poder guardar el archivo.
        print(F"Error tipo: {e.__class__}\nMensaje del error: {e}")
        return False


# =======================================================================
# FIN DE MANEJO DE JSONS
# =======================================================================
# ADMINISTRADOR DE PROYECTOS
# =======================================================================
def crear_proyecto(nombre, material, fallas, estado):
    limpiar_pantalla()
    proyectos = cargar_proyectos()
    
    # De no existir proyectos, se empieza con la ID 0001
    if not proyectos:
        print("Creando primer proyecto...")
        id_proyecto = "0001"
    # De lo contrario, se obtiene la cantidad de proyectos y se asigna una ID incremental.
    else:
        max_id = max(int(k) for k in proyectos.keys())
        id_proyecto = f"{max_id + 1:04d}"
        
    # Se agrega el nuevo proyecto al diccionario
    proyectos[id_proyecto] = {
        "Nombre del proyecto": nombre,
        "Material Utilizado (KG)": material,
        "Fallas Tecnicas": fallas,
        "Estado": estado.upper() 
    }
    
    # Se guarda el diccionario en .json
    if guardar_proyecto(proyectos):
        print("¡Proyecto creado exitosamente!")
    else:
        print("Error al guardar el proyecto")


def modificar_proyecto():
    proyectos = cargar_proyectos()
    
    # De no existir el ID, se devuelve sin hacer nada
    if not proyectos:
        print("No existen proyectos.")
        return
    
    mostrar_tabla_nombre()
    print("Seleccione el ID del proyecto a modificar (No hace falta escribir los 0):")
    print("Escriba 0 para cancelar.")
    id_modificar = validar_numero()
    if id_modificar == 0:
        print("Cancelando...")
        return
    id_proyecto = F"{id_modificar:04d}"
    # Se guarda el proyecto especifico que modificar.
    if id_proyecto not in proyectos:
        print(f"No existe proyecto con id {id_proyecto}")
    else:
        proyecto_modificado = proyectos[id_proyecto]

        while True:
            limpiar_pantalla()
            print("¿Qué deseas modificar?")
            print(F"1) Nombre del proyecto (valor actual: {proyecto_modificado.get("Nombre del proyecto")})")
            print(F"2) Material Utilizado (Valor actual: {proyecto_modificado.get("Material Utilizado (KG)")})")
            print(F"3) Fallas Tecnicas (Valor actual: {proyecto_modificado.get("Fallas Tecnicas")})")
            print(F"4) Estado (Valor actual: {proyecto_modificado.get("Estado")})")
            print("5) Finalizar y guardar")
            print("6) Cancelar")
                        
            print("Ingrese su elección:")
            valor = validar_numero()
            
            # Se crea un menú para modificar los distintos valores.
            if valor == 1:
                nuevo_nombre = input("Nuevo nombre del proyecto: ").strip()
                proyecto_modificado['Nombre del proyecto'] = nuevo_nombre
                
                
            elif valor == 2:
                print("Nuevo material utilizado (KG):")
                nuevo_material = validar_numero()
                proyecto_modificado['Material Utilizado (KG)'] = nuevo_material
                
                
            elif valor == 3:
                print("Nuevo número de fallas técnicas:")
                nuevas_fallas = validar_numero()
                proyecto_modificado['Fallas Tecnicas'] = nuevas_fallas
                
                
            elif valor == 4:
                print("\nOpciones de estado:")
                print("1) Completado")
                print("2) En progreso")
                print("3) Cancelado")
                    
                # Sub menú para modificar los estados
                estado_op = validar_numero()
                if estado_op == 1:
                    proyecto_modificado['Estado'] = "COMPLETADO"
                elif estado_op == 2:
                    proyecto_modificado['Estado'] = "EN PROGRESO"
                elif estado_op == 3:
                    proyecto_modificado['Estado'] = "CANCELADO"
                else:
                    print("Opción no válida, no se modificó el estado")
                    input("Presione Enter para continuar...")
                
                
            elif valor == 5:
                # Cuando se selecciona esta opción, se guarda y se sale del loop.
                proyectos[id_proyecto] = proyecto_modificado
                guardar_proyecto(proyectos)
                print("Proyecto modificado correctamente.")
                break
                
                
            elif valor == 6:
                # Cuando se selecciona esta opción, no se guarda y se sale del loop.
                print("Saliendo sin guardar.")
                break
            
            input("Presiona enter para continuar...")


def borrar_proyecto():
    limpiar_pantalla()
    proyectos = cargar_proyectos()
    if not proyectos:
        print("No existen proyectos")
        return
    
    mostrar_tabla_nombre()    
    print("Seleccione el ID del proyecto a borrar (No hace falta escribir los 0):")
    print("Escriba 0 para cancelar.")

    borrar = validar_numero()

    if borrar == 0:
        print("Cancelando...")
        return
    # Se cambia el formato al formato utilizado en el .json
    id_proyecto = F"{borrar:04d}"
    
    # De existir el proyecto, se borra y guarda el nuevo diccionario, de lo contrario, no hace nada.
    if id_proyecto not in proyectos:
        print(F"No existe el proyecto con id {id_proyecto}.")
    else:
        del proyectos[id_proyecto]
        guardar_proyecto(proyectos)
        print("Proyecto borrado exitosamente.")
    

def mostrar_tabla_nombre():
    limpiar_pantalla()
    proyectos = cargar_proyectos()          
    if proyectos:
        # Crear tabla
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre del Proyecto"]
        tabla.align["Nombre del Proyecto"] = "l"  # Alineación izquierda
        
        # Llenar las filas de la tabla
        for id_proyecto, datos in proyectos.items():
            nombre = datos.get("Nombre del proyecto")
            tabla.add_row([id_proyecto, nombre])

        print(tabla)
    else:
        print("NO EXISTEN PROYECTOS")
        

def mostrar_tabla_completa():
    limpiar_pantalla()
    proyectos = cargar_proyectos()
    
    if not proyectos:
        print("No existen proyectos")
        return
    else:
        # Crear tabla
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre del Proyecto", "Material Utilizado (KG)", "Fallas", "Estado"]
        tabla.align["Nombre del Proyecto"] = "l"  # Alineación izquierda
                
        # Llenar las filas de la tabla
        for id_proyecto, datos in proyectos.items():
            nombre = datos.get("Nombre del proyecto")
            material = datos.get("Material Utilizado (KG)")
            fallas = datos.get("Fallas Tecnicas")
            estado = datos.get("Estado")
            tabla.add_row([id_proyecto, nombre, material, fallas, estado])

        print(tabla)                
        exportar_tabla(tabla)

def exportar_tabla(tabla):
    # Conseguir la fecha actual
    current_date = datetime.now()
    
    # Convertirla a formato AAAA/MM/DD
    fecha = current_date.strftime("%Y-%m-%d")
    
    # Directorio al que se exportará
    archivo_a_exportar = Path(F'./datos/tabla-exportada-{fecha}.txt')
    
    # Guardado del archivo .txt
    with open(archivo_a_exportar, "w") as f:
        print(tabla, file=f)
    
    print(F"Exportando la tabla a {archivo_a_exportar}")

# =======================================================================
# FIN DE ADMINISTRADOR DE PROYECTOS
# =======================================================================