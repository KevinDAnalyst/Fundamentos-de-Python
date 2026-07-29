import pandas as pd

# Crear un conjunto de datos básico
datos = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
    'Ventas': [1200, 250, 400, 800],
    'Stock': [15, 50, 30, 8]
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(datos)

# Filtrar productos con ventas mayores a 300
productos_top = df[df['Ventas'] > 300]

print("=== Productos Destacados ===")
print(productos_top)