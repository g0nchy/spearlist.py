# Spearlist - Generación de Wordlist para Ataques de Ingeniería Social Dirigida

Spearlist es un script de Python que genera una wordlist para su uso en ataques de ingeniería social dirigida. El script solicita al usuario que ingrese información personal y preferencias, y luego crea una wordlist basada en la entrada, con diferentes variaciones de los datos ingresados.

## Requisitos

- Python 3

## Solicitudes

El script te solicitará que ingreses (opcionalmente) la siguiente información:

- Nombre
- Apellido
- Apodo
- Nick
- Año de nacimiento (yyyy)
- Mes de nacimiento (mm)
- Día de nacimiento (dd)
- Equipo deportivo
- Banda musical
- Nombre de la mascota
- Nombre familiar
- Nombre de la pareja
- Año de aniversario de pareja (yyyy)
- Mes de aniversario de pareja (mm)
- Día de aniversario de pareja (dd)
- Contraseña antigua
- Palabra clave

## Opciones

Puedes elegir modificar la wordlist con las siguientes opciones:

- Minúsculas: Agregar todas las palabras en minúsculas a la wordlist.
- Mayúsculas: Agregar todas las palabras en mayúsculas a la wordlist.
- Capitalización: Agregar solo el primer carácter en mayúscula y el resto en minúscula a la wordlist.
- Leet Speak: Reemplazar ciertos caracteres con números para crear versiones leet speak de las palabras.
- Reversa: Agregar versiones revertidas de las palabras a la wordlist.

## Uso

Para generar la wordlist, sigue los siguientes pasos:

1. Clona o descarga el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Ejecuta el siguiente comando: `python3 spearlist.py`
4. Sigue las indicaciones en pantalla para ingresar la información y preferencias requeridas. El script generará la wordlist y la guardará en un archivo de texto con un nombre en el formato "wordlist-{nombre}-{apellido}.txt".

## Licencia

Este proyecto está bajo la Licencia MIT: consulta el archivo [LICENSE](LICENSE) para más detalles.
