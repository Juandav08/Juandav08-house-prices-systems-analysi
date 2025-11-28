import pandas as pd

# Cargar el dataset de entrenamiento
df = pd.read_csv("train.csv")

# Seleccionar las variables más relevantes para el análisis
vars_equipo1 = [
    "SalePrice",  # Variable objetivo - precio de venta
    "GrLivArea", "TotalBsmtSF", "GarageCars", "GarageArea", "LotArea",  # Características de tamaño
    "OverallQual", "OverallCond", "KitchenQual", "ExterQual",  # Variables de calidad
    "YearBuilt", "YearRemodAdd",  # Fechas importantes
    "FullBath", "TotRmsAbvGrd",  # Habitaciones y baños
    "Neighborhood"  # Ubicación
]

# Filtrar el dataframe con solo las columnas seleccionadas
df = df[vars_equipo1]

# Tratamiento de valores faltantes
# Para variables numéricas usamos la mediana (menos sensible a outliers)
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Para variables categóricas usamos la moda (valor más frecuente)
cat_cols = df.select_dtypes(include=["object"]).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# Mapeo de variables de calidad a valores numéricos
# Po=Poor, Fa=Fair, TA=Typical/Average, Gd=Good, Ex=Excellent
qual_map = {"Po":1, "Fa":2, "TA":3, "Gd":4, "Ex":5}

df["KitchenQual"] = df["KitchenQual"].map(qual_map)
df["ExterQual"] = df["ExterQual"].map(qual_map)

# Convertir variable categórica Neighborhood en variables dummy
df = pd.get_dummies(df, columns=["Neighborhood"], drop_first=True)

# Crear nuevas variables derivadas que pueden ser útiles
df["HouseAge"] = 2010 - df["YearBuilt"]  # Edad de la casa al momento de la venta
df["YearsSinceRemodel"] = 2010 - df["YearRemodAdd"]  # Años desde la última remodelación
df["TotalBathrooms"] = df["FullBath"]  # Por ahora solo consideramos baños completos

# Guardar el dataset procesado
df.to_csv("dataset_limpio_equipo1.csv", index=False)

# Verificar el resultado del procesamiento
print(df.shape)  # Dimensiones del dataset final
print(df.isnull().sum())  # Verificar que no queden valores nulos
print(df.head())  # Mostrar las primeras filas