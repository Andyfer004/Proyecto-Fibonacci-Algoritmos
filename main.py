from turing_machine import TuringMachine

def calcular_fibonacci(n):
    """Ejecuta la máquina de Turing y obtiene Fibonacci(n)."""
    maquina = TuringMachine("maquina_fibonacci.json")
    resultado = maquina.ejecutar()
    print(f"Resultado para Fibonacci({n}): {resultado}")

if __name__ == "__main__":
    n = int(input("Ingrese el número de Fibonacci a calcular: "))
    calcular_fibonacci(n)