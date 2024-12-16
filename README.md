#INSTRUCCIONES PUNTA A PUNTA

Para utilizar el programa como cliente y servidor desde un mismo host los pasos son los siguientes:
1)	Clonar el repositorio subido a github: 
SSH:  git@github.com:MarcoIppolito96/SIMPLE-API-redes.git
HTTPS: https://github.com/MarcoIppolito96/SIMPLE-API-redes.git
Ejemplo de uso: 
git clone git@github.com:MarcoIppolito96/SIMPLE-API-redes.git

2)	Instalación del entorno virtual: 
Posicionarse en una terminal o simbolo de sistema dentro de la carpeta raíz del proyecto y ejecutar:
 python -m venv env
Esto creará el entorno virtual. Luego (dentro de la misma carpeta raiz) habrá que activarlo con:
.\env\Scripts\activate
Y ejecutar el siguiente comando para instalar todas las dependencias y librerías necesarias para el correcto funcionamiento del mismo:
pip install -r .\requirements.txt

3)	Poner en funcionamiento el servidor:
Dirigirse a la carpeta ..\servidor_api y ejecutar el siguiente comando:
uvicorn main:app --reload --host 0.0.0.0

4) Para utilizar el programa como cliente, se debe abrir una terminal o simbolo de sistema (CMD) posicionarse dentro de la carpeta ..\cliente_api y ejecutar el siguiente comando:
python cliente.py
Luego de eso, tendrás en la consola el menú con las distintas opciones a elegir según las necesidades del usuario.
