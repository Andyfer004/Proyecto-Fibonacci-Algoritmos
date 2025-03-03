import json

class TuringMachine:
    def __init__(self, config_file):
        """Carga la configuración de la máquina desde un archivo JSON."""
        with open(config_file, "r") as f:
            config = json.load(f)

        self.estados = config["estados"]
        self.alfabeto = config["alfabeto"]
        self.cinta = config["cinta"]
        self.estado_actual = config["estado_inicial"]
        self.estado_final = config["estado_final"]
        self.transiciones = config["transiciones"]
        self.head = 0  # Posición inicial del cabezal

    def mover_cabezal(self, direccion):
        """Mueve el cabezal en la dirección dada (R o L)."""
        if direccion == "R":
            self.head += 1
            if self.head >= len(self.cinta):
                self.cinta.append("b")  # Expande la cinta
        elif direccion == "L" and self.head > 0:
            self.head -= 1

    def ejecutar(self):
        """Ejecuta la simulación de la máquina de Turing."""
        while self.estado_actual != self.estado_final:
            simbolo_actual = self.cinta[self.head]
            if simbolo_actual not in self.transiciones[self.estado_actual]:
                break

            nuevo_estado, movimiento = self.transiciones[self.estado_actual][simbolo_actual]
            self.estado_actual = nuevo_estado
            self.mover_cabezal(movimiento)

        return "".join(self.cinta)