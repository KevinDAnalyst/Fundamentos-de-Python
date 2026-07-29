import matplotlib.pyplot as plt

# Datos de prueba
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
usuarios_nuevos = [150, 200, 350, 300, 500]

# Crear gráfico de líneas
plt.plot(meses, usuarios_nuevos, marker='o', color='b', linestyle='--')
plt.title("Crecimiento Mensual de Usuarios")
plt.xlabel("Mes")
plt.ylabel("Nuevos Registros")
plt.grid(True)

# Mostrar gráfico
plt.show()