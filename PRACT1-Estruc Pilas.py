class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0

    def insertar(self, item):
        if self.tope >= self.capacidad:
            print(f"Error: Desbordamiento (Overflow) al intentar insertar '{item}'")
            return
        self.elementos.append(item)
        self.tope += 1
        print(f"Insertar({item}) -> TOPE = {self.tope}, Pila: {self.elementos}")

    def eliminar(self):
        if self.tope == 0:
            print("Error: Subdesbordamiento (Underflow). La pila está vacía.")
            return None
        item = self.elementos.pop()
        self.tope -= 1
        print(f"Eliminar() -> TOPE = {self.tope}, Pila: {self.elementos}")
        return item

# --- Simulación de las operaciones solicitadas ---
if __name__ == "__main__":
    mi_pila = Pila(capacidad=8)
    
    print("--- Secuencia de operaciones ---")
    mi_pila.insertar("X")  # a
    mi_pila.insertar("Y")  # b
    mi_pila.eliminar()     # c (Z)
    mi_pila.eliminar()     # d (T)
    mi_pila.eliminar()     # e (U) -> Genera subdesbordamiento
    mi_pila.insertar("V")  # f
    mi_pila.insertar("W")  # g
    mi_pila.eliminar()     # h (p)
    mi_pila.insertar("R")  # i

    print(f"\nResultado final: La pila quedó con {mi_pila.tope} elementos.")