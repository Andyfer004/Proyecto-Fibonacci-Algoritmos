import json

class SingleTapeTuringMachine:
    """
    Simula una Máquina de Turing de UNA SOLA CINTA para calcular Fibonacci.
    La cinta almacena: n F(n-2) F(n-1) F(n) _ _ _ _
    """

    def __init__(self, config_file, n):
        with open(config_file, "r") as f:
            config = json.load(f)

        self.estados = config["estados"]
        self.estado_inicial = config["estado_inicial"]
        self.estados_finales = config["estados_finales"]
        self.transiciones = config["transiciones"]

        self.estado_actual = self.estado_inicial

        # Inicializamos la cinta con el formato: n F(n-2) F(n-1) _
        self.cinta = ["_"] * 10  # Espacios vacíos para cálculos
        self.cinta[0] = str(n)  # n
        self.cinta[1] = "1"  # F(n-2) = 1
        self.cinta[2] = "1"  # F(n-1) = 1
        self.head = 3  # Apunta donde se calculará F(n)

        self.traza = []  # Guardar la configuración tras cada transición

    def get_configuracion(self):
        """
        Retorna el estado y la cinta en su estado actual.
        """
        return {
            "estado": self.estado_actual,
            "cinta": " ".join(self.cinta),
            "cabezal": self.head
        }

    def paso(self):
        """
        Ejecuta una transición según el estado actual y la cinta.
        """
        if self.estado_actual not in self.transiciones:
            return

        info_estado = self.transiciones[self.estado_actual]

        # Leer valores de la cinta
        n = int(self.cinta[0]) if self.cinta[0] != "_" else 0
        f_k_minus_2 = int(self.cinta[1]) if self.cinta[1] != "_" else 0
        f_k_minus_1 = int(self.cinta[2]) if self.cinta[2] != "_" else 0

        # Condiciones de bifurcación
        if "condicion" in info_estado:
            condicion = info_estado["condicion"]
            if condicion == "IF_N_LE_2":
                self.estado_actual = info_estado["si_cumple"] if n <= 2 else info_estado["si_no_cumple"]
            elif condicion == "IF_COUNTER_GT_0":
                self.estado_actual = info_estado["si_cumple"] if n > 2 else info_estado["si_no_cumple"]

        # Acciones de la máquina
        if "accion" in info_estado:
            accion = info_estado["accion"]

            if accion == "SUM_TAPE2_TAPE3_TO_TAPE4":
                suma = f_k_minus_2 + f_k_minus_1
                self.cinta[self.head] = str(suma)  # Escribimos en la cinta

            elif accion == "TAPE2_EQUALS_TAPE3_AND_TAPE3_EQUALS_TAPE4":
                self.cinta[1] = self.cinta[2]  # F(n-2) ← F(n-1)
                self.cinta[2] = self.cinta[self.head]  # F(n-1) ← F(n)
                self.cinta[self.head] = "_"  # Limpiar espacio de trabajo

            elif accion == "COUNTER_MINUS_1":
                self.cinta[0] = str(n - 1)  # Decrementamos n

            elif accion == "STOP":
                pass  # No hace nada, termina

        # Estado siguiente lineal
        if "siguiente" in info_estado:
            self.estado_actual = info_estado["siguiente"]

    def run(self):
        """
        Ejecuta la máquina hasta alcanzar un estado final.
        """
        self.traza.append(self.get_configuracion())

        while self.estado_actual not in self.estados_finales:
            self.paso()
            self.traza.append(self.get_configuracion())

        return self.cinta[2], self.traza  # F(n) está en la posición 2


# Ejemplo de uso
config_file = "machine_config.json"
n = 6  # Calculamos F(6)
machine = SingleTapeTuringMachine(config_file, n)
resultado, traza = machine.run()


