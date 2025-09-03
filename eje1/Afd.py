class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}
        self.estado_inicial = 'q0'
        self.estados_finales = {'q0', 'q1', 'q2'}
        self.estado_actual = self.estado_inicial
        self.transiciones = {
            'q0': {'a': 'q0', 'b': 'q1', 'c': 'q2'},
            'q1': {'a': 'q3', 'b': 'q1', 'c': 'q2'},
            'q2': {'a': 'q3', 'b': 'q3', 'c': 'q2'},
            'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3'}
        }

    def reiniciar(self):
        self.estado_actual = self.estado_inicial

    def procesar_simbolo(self, simbolo):
        if simbolo in self.transiciones[self.estado_actual]:
            self.estado_actual = self.transiciones[self.estado_actual][simbolo]
        else:
            self.estado_actual = 'q3'

    def es_cadena_valida(self, cadena):
        self.reiniciar()
        for simbolo in cadena:
            self.procesar_simbolo(simbolo)
            print(f"Símbolo: '{simbolo}' -> Estado: {self.estado_actual}")
        return self.estado_actual in self.estados_finales

if __name__ == "__main__":
    afd = AFD()
    cadena = input("Ingrese una cadena conletras a b c: ")
    if afd.es_cadena_valida(cadena):
        print("La cadena es válida ")
    else:
        print("La cadena invalida ")
