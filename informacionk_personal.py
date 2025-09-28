# Tarea: Trabajando con Diccionarios en Python

# 1) Crear el diccionario con información personal
informacion_personal = {
    "nombre": "María Gómez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniera de Sistemas"
}

print("Diccionario inicial:", informacion_personal)

# 2) Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# 3) Agregar un nuevo dato (telefono si no existe)
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# 4) Eliminar la edad
informacion_personal.pop("edad")

# 5) Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
