from turing_machine import SingleTapeTuringMachine

def main():
    n = int(input("Ingrese el valor de n para Fibonacci: "))
    
    maquina = SingleTapeTuringMachine("machine_config.json", n)
    resultado, traza = maquina.run()

    # Imprime la traza
    print("\n--- TRAZA DE EJECUCIÓN ---")
    for i, config in enumerate(traza):
        print(f"Paso {i}: Estado={config['estado']}, Cinta={config['cinta']}, Cabezal={config['cabezal']}")

    # Imprime resultado final
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Fibonacci({n}) = {resultado}")

if __name__ == "__main__":
    main()