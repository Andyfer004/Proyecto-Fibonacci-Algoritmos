import json

class MultiTapeTuringMachine:
    """
    Simula una máquina de Turing multi-cinta para Fibonacci.
    - Cinta1: counter (n-2)
    - Cinta2: F(n-2)
    - Cinta3: F(n-1)
    - Cinta4: área de trabajo (suma)
    """

    def __init__(self, config_file, n):
        # Carga la config de un JSON
        with open(config_file, "r") as f:
            config = json.load(f)

        self.estados = config["estados"]
        self.estado_inicial = config["estado_inicial"]
        self.estados_finales = config["estados_finales"]
        self.transiciones = config["transiciones"]

        # Inicializamos las cintas (valores enteros)
        self.n = n
        if n <= 2:
            self.counter = 0
        else:
            self.counter = n - 2  # Cinta1

        self.tape2 = 1  # F(1)
        self.tape3 = 1  # F(2)
        self.tape4 = 0  # Área de trabajo

        self.estado_actual = self.estado_inicial
        self.traza = []  # Guarda la configuración tras cada transición

    def get_configuracion(self):
        """
        Retorna un dict con la configuración actual:
        - estado
        - counter, tape2, tape3, tape4
        """
        return {
            "estado": self.estado_actual,
            "cinta1_counter": self.counter,
            "cinta2_f_k_minus_2": self.tape2,
            "cinta3_f_k_minus_1": self.tape3,
            "cinta4_work": self.tape4
        }

    def paso(self):
        """
        Ejecuta una transición según el estado_actual y las condiciones/acciones
        definidas en self.transiciones.
        """
        if self.estado_actual not in self.transiciones:
            # No hay transición -> se detiene
            return

        info_estado = self.transiciones[self.estado_actual]

        # Verificamos si hay una 'condicion' que determina bifurcación
        if "condicion" in info_estado:
            condicion = info_estado["condicion"]

            if condicion == "IF_N_LE_2":
                # Si n <= 2 -> si_cumple, si no -> si_no_cumple
                if self.n <= 2:
                    self.estado_actual = info_estado["si_cumple"]
                else:
                    self.estado_actual = info_estado["si_no_cumple"]

            elif condicion == "IF_COUNTER_GT_0":
                if self.counter > 0:
                    self.estado_actual = info_estado["si_cumple"]
                else:
                    self.estado_actual = info_estado["si_no_cumple"]

        # Verificamos si hay una 'accion' que realizar
        if "accion" in info_estado:
            accion = info_estado["accion"]

            if accion == "SUM_TAPE2_TAPE3_TO_TAPE4":
                self.tape4 = self.tape2 + self.tape3

            elif accion == "TAPE2_EQUALS_TAPE3_AND_TAPE3_EQUALS_TAPE4":
                self.tape2 = self.tape3
                self.tape3 = self.tape4
                self.tape4 = 0  # limpiar la cinta4

            elif accion == "COUNTER_MINUS_1":
                self.counter -= 1

            elif accion == "STOP":
                # Estamos en un estado final, no hacemos nada especial
                pass

        # Verificamos si hay un 'siguiente' estado (lineal, sin bifurcación)
        if "siguiente" in info_estado:
            self.estado_actual = info_estado["siguiente"]

    def run(self):
        """
        Ejecuta hasta que se alcance un estado final o no exista transición.
        Retorna (fibonacci, traza).
        """
        # Guardamos la config inicial
        self.traza.append(self.get_configuracion())

        while (self.estado_actual not in self.estados_finales and 
               self.estado_actual in self.transiciones):
            self.paso()
            self.traza.append(self.get_configuracion())

        # Al final, F(n) está en tape3
        return self.tape3, self.traza
