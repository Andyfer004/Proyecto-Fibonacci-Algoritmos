import time
from turing_machine import SingleTapeTuringMachine

def calcular_fibonacci():
    print("\n🔗 Ingrese el valor de n para Fibonacci: ", end="")
    n = int(input())

    print("\n🚀 Inicializando la Máquina de Turing...")
    maquina = SingleTapeTuringMachine("machine_config.json", n)

    print("⚙️ Ejecutando cálculo...")

    inicio = time.time()  
    resultado, traza = maquina.run()
    fin = time.time() 
    tiempo_ejecucion = fin - inicio 

    print("\n✨ --- TRAZA DE EJECUCIÓN --- ✨")
    for i, config in enumerate(traza):
        cinta_estilizada = "".join(config['cinta']).replace('0', '0').replace('1', '1')
        print(f"🔹 Paso {i+1}: Estado = {config['estado']}, Cinta = [{cinta_estilizada}], Cabezal = {config['cabezal']}")

    print("\n🎉 --- RESULTADO FINAL --- 🎉")
    print(f"✅ Fibonacci({n}) = {resultado}")
    print(f"⏱️ Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos\n")


def main():
    print("🌟 Bienvenido al Calculador de Fibonacci con Máquina de Turing 🌟")
    print("💻 Este programa simula una Máquina de Turing para calcular la serie de Fibonacci.")
    print("🔢 Puedes ingresar valores de 'n' cuantas veces quieras o salir del programa.\n")

    while True:
        print("📋 Menú Principal:")
        print("1️⃣ Calcular un valor de Fibonacci")
        print("2️⃣ Salir\n")

        opcion = input("👉 Elige una opción (1 o 2): ")

        if opcion == '1':
            calcular_fibonacci()
        elif opcion == '2':
            print("\n👋 Gracias por usar el simulador. ¡Hasta pronto! 🚀")
            break
        else:
            print("⚠️ Opción no válida. Por favor, elige 1 o 2.\n")

if __name__ == "__main__":
    main()
