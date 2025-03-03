import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Agregar la ruta raíz del proyecto para importar turing_machine.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from turing_machine import MultiTapeTuringMachine

# Ruta absoluta del archivo de configuración
CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "machine_config.json"))

# Ruta para guardar los gráficos
RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))

# Crear la carpeta "results/" si no existe
os.makedirs(RESULTS_DIR, exist_ok=True)

def medir_tiempos(max_n):
    """Ejecuta la máquina para diferentes valores de n y mide el tiempo."""
    tiempos = []
    valores = list(range(1, max_n + 1))

    print("\n📊 **Datos de prueba:**")
    for n in valores:
        inicio = time.perf_counter()  # ⏱ Mayor precisión
        maquina = MultiTapeTuringMachine(CONFIG_PATH, n)
        maquina.run()
        fin = time.perf_counter()  # ⏱ Mayor precisión

        tiempo_total = fin - inicio
        tiempos.append(tiempo_total)
        print(f"  - Fibonacci({n}): {tiempo_total:.8f} s")  # Mayor precisión en la impresión

    return valores, tiempos

def generar_dispersión(valores, tiempos):
    """Genera gráfico de dispersión."""
    scatter_path = os.path.join(RESULTS_DIR, "scatter_plot.png")
    plt.figure(figsize=(8, 5))
    plt.scatter(valores, tiempos, color='blue', label="Datos observados", alpha=0.7)
    plt.xlabel("Número de Fibonacci (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución de la Máquina de Turing")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(scatter_path)
    plt.close()
    print(f"📁 Imagen guardada: {scatter_path}")