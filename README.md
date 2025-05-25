# Evaluación 3 - Introducción a la Programación y Robótica Aplicada 
Este proyecto es una aplicación de consola simple para demostrar los conocimientos adquiridos durante la unidad 3.
Requiere una minima configuración

### Funcionamiento del programa

Para usar el programa correctamente se debe usar un virtual environment, para realizar lo siguiente:
<details open>
<summary ><h2>Instrucciones Windows</h2></summary>

Se recomienda utilizar Powershell.

Ejecutar los siguientes comandos en la carpeta fuente:
```
python -m venv .env
.\.env\Scripts\Activate.ps1
pip install -r requirements.txt
```

Estarás en el ambiente virtual si ves el (.env) frente al command prompt. 
Para usar el programa se debe estar en el ambiente virtual y ejecutar el siguiente comando:
```
py .\menu.py
```
</details>

<details open>
<summary><h2>Instrucciones Linux/Mac</h2></summary>
Cualquier terminal POSIX debería servir.
Ejecutar los siguientes comandos en la carpeta fuente:

```
python3 -m venv .env
source .\.env\Scripts\activate
pip install -r requirements.txt
```

Estarás en el ambiente virtual si ves el (.env) frente al command prompt. 
Para usar el programa se debe estar en el ambiente virtual y ejecutar el siguiente comando:
```
python3 .\menu.py
```
</details>
