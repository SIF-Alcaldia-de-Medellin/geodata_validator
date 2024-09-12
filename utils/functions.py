import geopandas as gpd
import pandas as pd

def change_field_names(gdf):
    """
    The function `change_field_names` changes the column names of a GeoDataFrame to lowercase.
    
    :param gdf: The function `change_field_names` takes a GeoDataFrame (`gdf`) as input and changes the
    column names to lowercase. This function is useful for standardizing the column names in a
    GeoDataFrame to make them consistent and easier to work with
    :return: The function `change_field_names` is returning the GeoDataFrame `gdf` with all column names
    converted to lowercase.
    """
    gdf.columns = [col.lower() for col in gdf.columns]
    
    return gdf

def load_geodataframe(shapefile_path):
    """
    The function `load_geodataframe` reads a shapefile and returns a GeoDataFrame, handling exceptions
    if any occur.
    
    :param shapefile_path: The `shapefile_path` parameter in the `load_geodataframe` function is a
    string that represents the file path to a shapefile. This function attempts to read the shapefile
    using GeoPandas (`gpd`) and returns a GeoDataFrame containing the spatial data from the shapefile.
    If
    :return: The function `load_geodataframe` is returning a GeoDataFrame object loaded from the
    shapefile located at the `shapefile_path`.
    """
    try:
        gdf = gpd.read_file(shapefile_path)
        return gdf
    except Exception as e:
        print(f"Error al cargar el shapefile: {e}")
        exit(1)
        
def transform_nulls(gdf):
    """
    The function `transform_nulls` replaces null values in numeric columns with 0 and in string columns
    with "No aplica" except for "N/A".
    
    :param gdf: A GeoDataFrame (gdf) is a tabular data structure that contains a geometry column
    representing geometries like points, lines, or polygons, along with other attribute columns. It is
    commonly used in geospatial analysis and visualization
    :return: The function `transform_nulls` is returning the GeoDataFrame `gdf` after transforming null
    values in numeric columns to 0 and in string columns to "No aplica" if the value is either null or
    "N/A".
    """
    for col in gdf.columns:
        if pd.api.types.is_numeric_dtype(gdf[col]):
            gdf[col] = gdf[col].apply(lambda x: x if pd.notna(x) else 0)
        elif pd.api.types.is_string_dtype(gdf[col]):
            gdf[col] = gdf[col].apply(lambda x: x if pd.notna(x) and x != "N/A" else "No aplica")
    
    return gdf

def transform_spaces(gdf):
    """
    The function `transform_spaces` replaces spaces in column names of a pandas DataFrame with
    underscores.
    
    :param gdf: The `transform_spaces` function takes a pandas DataFrame `gdf` as input and replaces any
    spaces in the column names with underscores. This function helps to standardize column names and
    make them more suitable for coding purposes
    :return: The function `transform_spaces` takes a pandas DataFrame `gdf` as input, replaces any
    spaces in the column names with underscores, and then returns the modified DataFrame `gdf`.
    """
    gdf.columns = [col.replace(" ", "_") for col in gdf.columns]
    return gdf