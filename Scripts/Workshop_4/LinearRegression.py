import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el dataset ya procesado y limpio
df = pd.read_csv("dataset_limpio_equipo1.csv")

# Definir variables independientes y dependiente para el modelado
X = df.drop("SalePrice", axis=1)  # Features (todas las variables excepto el precio)
y = df["SalePrice"]  # Target (variable que queremos predecir)

# División estratificada del dataset para entrenamiento y validación
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Implementación del modelo de regresión lineal
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

# Generar predicciones con el modelo lineal
y_pred_lin = lin_model.predict(X_test)

# Evaluación del rendimiento del modelo lineal
print("Linear Regression RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lin)))
print("Linear Regression R2:", r2_score(y_test, y_pred_lin))

# Visualización de predicciones vs valores reales
plt.figure(figsize=(8,8))
plt.scatter(y_test, y_pred_lin, alpha=0.5)
plt.xlabel("Real SalePrice")
plt.ylabel("Predicted SalePrice")
plt.title("Comparación entre Precios Reales y Predichos – Regresión Lineal")

# Línea de referencia perfecta (predicción = realidad)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')

plt.tight_layout()
plt.savefig("grafica_real_vs_pred_lin.png", dpi=300)
plt.show()

# Análisis de residuales para evaluar la distribución de errores
errors = y_test - y_pred_lin

plt.figure(figsize=(10,5))
sns.histplot(errors, bins=40, kde=True)
plt.title("Distribución de Residuales – Regresión Lineal")
plt.xlabel("Error de Predicción")

plt.tight_layout()
plt.savefig("grafica_residuales_lin.png", dpi=300)
plt.show()

# Implementación del modelo Random Forest como comparación
rf = RandomForestRegressor(
    n_estimators=200,  # Número de árboles en el bosque
    max_depth=10,      # Profundidad máxima para evitar overfitting
    random_state=42
)

rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Evaluación del modelo Random Forest
print("RandomForest RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf)))
print("RandomForest R2:", r2_score(y_test, y_pred_rf))

# Análisis de importancia de variables según Random Forest
importances = pd.Series(rf.feature_importances_, index=X.columns)

plt.figure(figsize=(12,6))
importances.sort_values(ascending=False).head(15).plot(kind='bar')
plt.title("Variables Más Influyentes en el Precio – Random Forest")
plt.ylabel("Importancia Relativa")

plt.tight_layout()
plt.savefig("grafica_feature_importance_rf.png", dpi=300)
plt.show()

# Matriz de correlación para identificar relaciones entre variables
plt.figure(figsize=(14,10))
sns.heatmap(df.corr(), cmap='coolwarm', center=0, square=False)

plt.title("Matriz de Correlación entre Variables", fontsize=14)
plt.tight_layout()

plt.savefig("grafica_correlation_matrix.png", dpi=300)
plt.show()