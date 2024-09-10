import os
from utils.functions import *
from utils.validators import *
import warnings

warnings.filterwarnings("ignore")

shapefile = input("Ingrese el nombre de la capa a usar sin extensión(.shp): ")

current_dir = os.getcwd()
shapefile_path = os.path.join(current_dir, "shapes", f"{shapefile}.shp")

gdf = load_geodataframe(shapefile_path)

problems = {
    "columna": column_validator(gdf),
    "fila": row_validator(gdf),
    "idop_idgeo": unique_validator(gdf, "IDOP_idgeo")
}
        
for key, problems_list in problems.items():
    if problems_list:
        print(f"Problemas en {key}s:")
        for problem in problems_list:
            print(f"\t{problem}")
        print()
    else:
        print(f"Las {key}s cumplen con los estándares de Grupo Geográfico")
    print()
    
try:
    gdf = change_field_names(gdf)
    gdf = transform_nulls(gdf)

    gdf.to_file(os.path.join(current_dir,"shapes", f"{shapefile}_fixed"))

    print(f"Se ha guardado el shapefile con los nombres de columna en minúsculas y los valores nulos corregidos. La encontraras en la carpeta: {shapefile}_fixed")
except Exception as e:
    print(f"Ha ocurrido un error al guardar el shapefile: {e}")
    exit(1)
