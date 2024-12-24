# Publicador Kafka #

Este programa sirve para mandar mensajes manualmente a topicos de apache kafka, para esto solo requiere el host de kafka, una lista de los topicos que se pueden elegir para publicar y el id del cliente, que es el identificador unico del publicador, en este caso nuestro programa.

## Info ##
- Hecho con Python 3.12

Para ejecutar el programa sigue estos pasos:
1. Crea un entorno virtual (en mi caso utilizo Conda):
> `conda create -n "publicador_kafka_venv" python=3.12`

2. Inicia el entorno virtual:
> `conda activate publicador_kafka_venv`

3. Instala las dependencias:
> `pip install -r requirements.txt`

4. Crea el .env a partir del example.env y llena las variables con la informacion correspondiente

5. Ejecuta el proyecto:
> `python main.py`

###### Developed by JiroFg ######
