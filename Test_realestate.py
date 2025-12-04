import pandas as pd

# Leer CSV con ; como separador
df = pd.read_csv('assets/real_estate.csv', sep=';')

# Comprobación básica: que no esté vacío
if df.empty:
    raise ValueError("The dataset is empty!")

# Opcional: comprobar que existe alguna columna clave
required_columns = ["Price", "Area"]  # cambia estos nombres si son otros

missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

print("CSV loaded correctly and basic checks passed.")
