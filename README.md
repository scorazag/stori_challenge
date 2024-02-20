# Transaction Summary

El objetivo de el proyecto es poder hacer un resumen de las transacciones depositadas dentro de un csv y mandarlo atravez de un correo electronico.

El proyecto esta estructurado de la siguiente manera.
```bash
  ├── docker-compose.yml
  ├── mysql
  │   ├── database_stori.sql
  │   └── Dockerfile
  ├── __pycache__
  │   ├── database.cpython-310.pyc
  │   └── mail.cpython-310.pyc
  ├── pythonapp
  │   ├── database.py
  │   ├── Dockerfile
  │   ├── logo.jpg
  │   ├── mail.py
  │   ├── main.py
  │   ├── setup.py
  │   └── txns.csv
  └── README.md
```
Como podemos observar el proyecto se encuentra motado sobre docker y comprende 2 partes una que es mysql la cual contiene la base de datos  y la otra parte llamada pythonapp es la logica de el sistema.

```main.py``` es el archivo pirncipal para correr el systema el cual contiente los metodos necesarios para realizar el resumen como sacar el premnedio de debit y credo, hacer el conteo de transacciones por mes, obtener el balance total asi como extraer informacionde el archivo csn, adicional se apoya de dos archivos extras los cuales son ```mail.py``` el cual es el encardado de mandar el correo electronico y de ```database.py``` el cual realiza un INSERT a la BD declarada en la carpeta mysql

## Deployment

El primer paso para poder ejecutar el sistema es dar de alta una cuenta en https://ethereal.email/ ya que esta pagina nos permite simular un email y no comprometer datos sensibles. Esto nos dara un user,password asi como un host y un puerto los cuales podremos en el archivo ```mail.py``` esto con el fin de que simule el envio de un corre como se muestra acontinuacion.
![alt text for screen readers](/email.png)

adicionalmente es necesario modificar en archivo  ```txns.csv``` a gusto ya que de aqui es donde se toma la informacion para realizazr el resumen.

Para poder ejecutar este proyecto es nesesario tener instalado Docker asi como Docker compose, para ejecutar corra el siguiente comando:
```
  docker-compose up
```
Dando un resultado como el siguiente
![alt text for screen readers](/docker.png )



