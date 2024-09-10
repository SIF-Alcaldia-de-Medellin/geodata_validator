from datetime import datetime
import os
from utils.functions import *
from utils.validators import *
import warnings

warnings.filterwarnings("ignore")

shapefiles = input("Ingrese los nombre de la capas sepadas por coma sin usar su extensión(.shp):\n").split(",")

for shapefile in shapefiles:
    current_dir = os.getcwd()
    shapefile_path = os.path.join(current_dir, "shapes", f"{shapefile}.shp")

    gdf = load_geodataframe(shapefile_path)

    problems = {
        "columna": column_validator(gdf),
        "fila": row_validator(gdf),
        "idop_idgeo": unique_validator(gdf, "IDOP_idgeo")
    }

    with open(f"problems.log", "a") as logger:
        logger.write("Fecha Reporte: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")
        logger.write(f"Capa del reporte: {shapefile}\n")
        for key, problems_list in problems.items():
            if problems_list:
                msg = f"Problemas en {key}:"
                logger.write(f"{msg}\n")
                print(msg)
                for problem in problems_list:
                    msg = f"\t- {problem}"
                    logger.write(f"{msg}\n")
                    print(msg)
                print()
            else:
                msg = f"La {key} cumplen con los estándares de Grupo Geográfico"
                logger.write(f"{msg}\n")
                print(msg)
            logger.write(f"\n")
            print()
        logger.close()

    try:
        gdf = change_field_names(gdf)
        gdf = transform_nulls(gdf)

        gdf.to_file(os.path.join(current_dir,"shapes", f"{shapefile}_fixed"))

        print(f"Se ha guardado el shapefile con los nombres de columna en minúsculas y los valores nulos corregidos. La encontraras en la carpeta: {shapefile}_fixed")
    except Exception as e:
        print(f"Ha ocurrido un error al guardar el shapefile: {e}")
        exit(1)
