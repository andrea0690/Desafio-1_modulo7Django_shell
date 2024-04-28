# DesafioADL - Proyecto Django

Este proyecto tiene como objetivo proporcionar instrucciones paso a paso para crear y gestionar un proyecto en Django. A continuación se describen las tareas y sub-tareas involucradas en el proceso de creación y configuración de un proyecto Django.

Desafio Dia 2 - Modulo 7 shell

## Lista de Instrucciones

### Importación Inicial
Para comenzar la shell de django, ejecuta el siguiente comando:
```
python3 manage.py shell
```

### Importación Inicial
Para comenzar, importa todas las funciones del archivo `services.py`:
```python
from desafioadl.services import *
```


### Ejecutación de instrucciones

```python
tarea = crear_nueva_tarea('Levantar un proyecto en django')
crear_sub_tarea(tarea, 'Crear la carpeta en el directorio')
crear_sub_tarea(tarea, 'Crear virtualizacion')
crear_sub_tarea(tarea, 'Instalar ultima version de django')
crear_sub_tarea(tarea, 'Instalar psycopg2')
crear_sub_tarea(tarea, 'Instalar python-dotenv')
crear_sub_tarea(tarea, 'Instalar crear proyecto y app')
crear_sub_tarea(tarea, 'Crear modelos y realizar migraciones')
crear_sub_tarea(tarea, 'Instalar liberia extraña')
elimina_sub_tarea(9)
elimina_tarea(1)
recupera_tareas_y_sub_tareas(1)

imprimir_en_pantalla()
[1] Levantar un proyecto en django
    [1] Crear la carpeta en el directorio
    [2] Crear virtualizacion
    [3] Instalar ultima version de django
    [4] Instalar psycopg2
    [5] Instalar crear proyecto y app
    [6] Crear modelos y realizar migraciones

    ```

### Salida de la consola
Para salir de la consola de django ejecuta:
```python
exit()
```

