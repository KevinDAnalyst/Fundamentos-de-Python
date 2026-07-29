import numpy as np

# Crear dos arreglos unidimensionales (vectores)
precios = np.array([100.0, 250.0, 500.0])
impuestos = np.array([0.13, 0.13, 0.13])

# Operación vectorial (cálculo masivo sin bucles for)
monto_impuesto = precios * impuestos
precio_total = precios + monto_impuesto

print("Precios base:", precios)
print("Monto de impuesto:", monto_impuesto)
print("Precio final:", precio_total)