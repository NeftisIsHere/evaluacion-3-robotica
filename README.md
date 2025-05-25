# Funcionamiento del programa

Para usar el programa correctamente se debe usar un virtual environment, para realizar lo siguiente:

Instrucciones Windows
- Se recomienda utilizar Powershell.
- Ejecutar los siguientes comandos en la carpeta fuente:
```
python -m venv .env
.\.env\Scripts\Activate.ps1
pip install -r requirements.txt
```
Estarás en el ambiente virtual si ves el (.env) frente al command prompt. 
Para usar el programa ejecutar el siguiente comando:
```
py .\menu.py
```

En Linux/Mac:
```
python3 -m venv .env
source .\.env\Scripts\activate
pip install -r requirements.txt
```
Estarás en el ambiente virtual si ves el (.env) frente al command prompt. 
Para usar el programa ejecutar el siguiente comando:
```
python3 .\menu.py
```
