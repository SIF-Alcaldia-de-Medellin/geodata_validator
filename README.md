# Validador y Transformador de shapefiles

Este script permite validar y transformar archivos shapefile mediante la biblioteca **GeoPandas**. Proporciona varias validaciones para los datos geoespaciales y, además, transforma los nombres de las columnas a minúsculas y corrige valores nulos. El resultado es un nuevo shapefile modificado con los cambios aplicados. Esto con el objetivo de brindar un reporte a traves de consola y generar las correcciones basicas para cumplir con los estandares de calidad de Grupo Geografico.

## Requisitos

Antes de ejecutar el programa, debes de tener instaladas los siguientes programas:

- Python 3.7+
- Pip 24+

### Instalación de dependencias

Para instalar las dependencias necesarias, puedes usar el archivo `requirements.txt` o instalar manualmente los paquetes.

Para instalar usando el archivo `requirements.txt` ingresas por consola el siguiente comando:

```sh
pip install -r requirements.txt
```

## Estructura del proyecto

- `main.py`: El archivo principal que ejecuta el proceso de validación y transformación del shapefile.

- `utils/functions.py`: Contiene las funciones auxiliares para cargar y transformar los datos.

- `utils/validators.py`: Incluye las funciones que validan las columnas, filas, y otros aspectos de los datos geoespaciales.

- `shapes/`: Carpeta donde se almacenan los shapefiles de entrada y salida.

## Instrucciones de uso

1. Clona este repositorio en tu máquina local o descarga el código fuente.

    ```sh
    git clone https://github.com/SIF-Alcaldia-de-Medellin/geodata_validator.git
    cd geodata_validator
    ```

2. Coloca el shapefile que deseas validar y transformar dentro de la carpeta `shapes/`. El archivo shapefile debe tener los archivos asociados como `.shx`, `.dbf`, y `.prj` en el mismo directorio. En caso de no contar con tal directorio creala en la raiz del proyecto. Si usas una terminal linux puedes usar este comando:

    ```sh
    mkdir shapes
    ```

3. Ejecuta el script main.py. El programa te pedirá ingresar el nombre del shapefile (sin la extensión .shp).

    ```bash
    python main.py
    ```

4. El script realizará las siguientes validaciones:

    - **Validación de columnas:** Verifica si las columnas cumplen con los estándares geoespaciales definidos.

    - **Validación de filas:** Revisa si hay problemas con los datos de las filas (valores nulos o incorrectos).

    - **Validación de campo IDOP_idgeo:** Asegura que el campo `IDOP_idgeo` sea único en todas las filas.

5. Si no se encuentran problemas, el script transformará los nombres de las columnas a minúsculas y corregirá los valores nulos.

6. El shapefile modificado se guardará en la carpeta `shapes/[nombre_original]_fixed` bajo un nuevo nombre: `[nombre_original]_fixed.shp`.

## Funcionalidades

- **load_geodataframe:** Carga el archivo shapefile como un GeoDataFrame utilizando GeoPandas.

- **column_validator:** Verifica que las columnas cumplan con los nombres y formatos esperados.

- **row_validator:** Revisa las filas del GeoDataFrame para detectar valores problemáticos.

- **unique_validator:** Valida que un campo especificado (en este caso, IDOP_idgeo) tenga valores únicos.

- **change_field_names:** Cambia los nombres de las columnas a minúsculas para cumplir con las convenciones geoespaciales.

- **transform_nulls:** Transforma los valores nulos en las columnas seleccionadas para evitar problemas en los datos.

## Licencia

Este proyecto está bajo la [licencia MIT](LICENSE).
