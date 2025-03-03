from turing_machine import MultiTapeTuringMachine

def main():
    n = int(input("Ingrese el valor de n para Fibonacci: "))
    
    maquina = MultiTapeTuringMachine("machine_config.json", n)
    resultado, traza = maquina.run()

    # Imprime la traza
    print("\n--- TRAZA DE EJECUCIÓN ---")
    for i, config in enumerate(traza):
        print(f"Paso {i}: "
              f"Estado={config['estado']}, "
              f"Counter={config['cinta1_counter']}, "
              f"F(k-2)={config['cinta2_f_k_minus_2']}, "
              f"F(k-1)={config['cinta3_f_k_minus_1']}, "
              f"Work={config['cinta4_work']}")

    # Imprime resultado
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Fibonacci({n}) = {resultado}")

if __name__ == "__main__":
    main()