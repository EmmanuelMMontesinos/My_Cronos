# My_Cronos - Sistema de Control de Turnos

My_Cronos es una aplicación diseñada para facilitar el control de entrada y salida de los trabajadores de una empresa. La aplicación consta de tres componentes principales: my_cronos, registro y gestión.

## Indice

- [Componentes del Sistema](#componentes)
- [Requisitos del sistema](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Componentes

### 1. My_Cronos

![My_Cronos](image.png)<br>
My_Cronos es un teclado numérico que permite a los trabajadores ingresar su contraseña para registrar su entrada o salida de turno. La contraseña tiene un máximo de 8 dígitos y se utiliza para validar la identidad del trabajador.

### 2. Registro

![Registro](image-1.png)<br>
El componente de Registro proporciona diversas opciones para visualizar el historial de turnos de los trabajadores. Tanto globalmente cono por trabajador.

### 3. Gestión

![Gestión](image-2.png)<br>
La aplicación de Gestión es esencial para administrar la base de datos de trabajadores. Permite crear nuevos trabajadores, ver la información existente de los trabajadores y eliminar registros de la base de datos según sea necesario. Esta funcionalidad es fundamental para el correcto funcionamiento del sistema.

***<strong><em>IMPORTANTE:</em></strong>***
    Las contraseñas son para identificar rapidamente al trabajador, NO esta diseñado para matener ningun tipo de
    seguridad con el registro y/o muestra de las mismas.

## Requisitos

    Python 3.10
    Bibliotecas requeridas: tkinter, sqlite3
Si no quiere descargarse el Relase situado en el apartado de la derecha -->
Puede hacerlo clonando este repositorio.

## Instalación

        git clone <https://github.com/EmmanuelMMontesinos/My_Cronos>

Navega al directorio del proyecto:

        cd my_cronos

Ejecuta la aplicación principal:

        python my_cronos.py

## Uso

1- Abre la aplicación my_cronos.py para acceder al teclado numérico.<br>
2- Ingresa la contraseña del trabajador (máximo 8 dígitos).<br>
3- Utiliza la aplicación de Registro para ver el historial de turnos.<br>
4- Utiliza la aplicación de Gestión para administrar la base de datos de trabajadores, incluyendo la creación, visualización y eliminación de registros.

## Contribuir

Si deseas contribuir a My_Cronos, por favor sigue estos pasos:

    Haz un fork del repositorio.
    Crea una nueva rama para tu función: git checkout -b nueva-funcionalidad
    Haz tus cambios y haz commit: git commit -m 'Agrega nueva funcionalidad'
    Sube tus cambios a tu repositorio: git push origin nueva-funcionalidad
    Envía un pull request al repositorio principal.

## Licencia

My_Cronos se distribuye bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.
