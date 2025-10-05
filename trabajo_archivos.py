# Trabajo con Archivos de Texto en Python
# Autor: Karen
# Objetivo: Practicar lectura y escritura de archivos de texto en Python

# 1. Escritura en un archivo de texto
# Creamos el archivo "my_notes.txt" en modo escritura ("w")
with open("my_notes.txt", "w") as archivo:
    archivo.write("Primera nota: Estoy practicando Python.\n")
    archivo.write("Segunda nota: Hoy aprendí a trabajar con archivos.\n")
    archivo.write("Tercera nota: Subiré este trabajo a GitHub.\n")

# 2. Lectura del archivo de texto
# Abrimos el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as archivo:
    # Leemos línea por línea
    linea = archivo.readline()
    while linea:  # Mientras haya contenido
        print(linea.strip())  # strip() quita saltos de línea extra
        linea = archivo.readline()

# Nota: No es necesario cerrar manualmente los archivos
# porque "with open()" lo hace automáticamente.
