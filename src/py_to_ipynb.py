import os
import jupytext
from pathlib import Path

# Configuración
SRC_DIR = "src/"  # Ruta base (ajusta según tu estructura)
OUTPUT_DIR = "notebooks/"  # Carpeta destino para los notebooks

# Crear directorio de salida si no existe
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def convert_py_to_ipynb(py_path):
    """Convierte un archivo .py a .ipynb manteniendo estructura de carpetas"""
    # Generar ruta relativa dentro de src
    relative_path = os.path.relpath(py_path, start=SRC_DIR)
    
    # Crear estructura equivalente en notebooks
    ipynb_path = os.path.join(OUTPUT_DIR, relative_path).replace(".py", ".ipynb")
    os.makedirs(os.path.dirname(ipynb_path), exist_ok=True)
    
    # Leer el archivo .py y escribirlo como .ipynb
    with open(py_path, "r") as py_file:
        notebook = jupytext.read(py_file, fmt="py")
    with open(ipynb_path, "w") as ipynb_file:
        jupytext.write(notebook, ipynb_file, fmt="ipynb")
    
    print(f"Convertido: {relative_path} -> {ipynb_path}")

# Recorrer recursivamente src
for root, _, files in os.walk(SRC_DIR):
    for file in files:
        if file.endswith(".py") and file != "tempCodeRunnerFile.py":  # Ignorar archivos temporales
            convert_py_to_ipynb(os.path.join(root, file))

print("\n✅ Conversión completada. Archivos guardados en:", OUTPUT_DIR)