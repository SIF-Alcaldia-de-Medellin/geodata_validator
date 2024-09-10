import pandas as pd
import re

def column_validator(gdf):
    """
    The function `column_validator` checks for potential issues in the column names of a GeoDataFrame.
    
    :param gdf: The `column_validator` function you provided is designed to validate the column names of
    a GeoDataFrame (`gdf`). It checks for two potential problems in the column names:
    :return: The `column_validator` function returns a list of problems related to the columns of a
    GeoDataFrame `gdf`. The problems include messages about column names exceeding 30 characters or
    containing spaces, dashes, special characters, or uppercase letters.
    """
    problems = []

    for col in gdf.columns:
        if len(col) > 30:
            problems.append(f"El nombre del atributo '{col}' excede los 30 caracteres.")
        if re.search(r'[^_a-z]', col):
            problems.append(f"El nombre del atributo '{col}' contiene espacios, guiones, caracteres especiales o letras mayúsculas.")
            
    return problems
    
def row_validator(gdf):
    """
    The function `row_validator` checks for null values in numeric columns and numeric values in
    non-numeric columns in a given DataFrame.
    
    :param gdf: The `row_validator` function you provided is designed to check for potential issues in a
    pandas DataFrame `gdf`. It looks for columns with null values in numeric columns and columns with
    numeric values in non-numeric columns
    :return: The `row_validator` function returns a list of problems found in the input DataFrame `gdf`.
    The problems can include messages indicating columns that contain null values or columns that
    contain numeric values in non-numeric columns.
    """
    problems = []
    
    for col in gdf.columns:
        if pd.api.types.is_numeric_dtype(gdf[col]):
            if gdf[col].isnull().any():
                problems.append(f"La columna '{col}' contiene valores nulos.")
        elif pd.api.types.is_string_dtype(gdf[col]):
            invalids = gdf[col].apply(lambda x: bool(re.search(r'[0-9]', str(x))) if pd.notnull(x) else False)
            if invalids.any():
                problems.append(f"La columna '{col}' contiene valores numéricos en columnas no numéricas.")
                
    return problems

def unique_validator(gdf, column_name):
    """
    The function `unique_validator` checks if a specified column in a pandas DataFrame has duplicate
    values and returns a corresponding message.
    
    :param gdf: A GeoDataFrame (gdf) is a tabular data structure that contains a GeoSeries. It is
    essentially a pandas DataFrame with an additional column that holds geometry data. This allows for
    spatial operations and analysis to be performed on the data
    :param column_name: The `column_name` parameter is the name of the column in the GeoDataFrame
    (`gdf`) that you want to validate for uniqueness
    :return: The function `unique_validator` returns a list containing a message indicating whether
    there are duplicate values in the specified column of the given DataFrame `gdf`. The message will
    either state "No tiene campos duplicados en la columna '{column_name}'" if there are no duplicates,
    or "Tiene campos duplicados en la columna '{column_name}'" if there are duplicates. If an exception
    occurs during
    """
    try:
        column_name = column_name.lower()
        unique_series = gdf.nunique()
        unique_series.index = [index.lower() for index in unique_series.index]
        return [f"No tiene campos duplicados en la columna '{column_name}'" if unique_series[column_name] == len(gdf) else f"Tiene campos duplicados en la columna '{column_name}'"]
    except Exception:
        return [f"Ha ocurrido un error al validar si existen campos nulos en la columna {column_name}"]