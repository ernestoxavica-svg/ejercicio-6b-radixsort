"""
Ordenamiento Radix Sort
Menú que pide la cantidad de números y los números, los ordena con
Radix Sort y repite hasta que el usuario decida salir.
"""


def radix_sort(lista):
    """Ordena enteros (positivos y negativos) con Radix Sort LSD en base 10."""
    negativos = [-x for x in lista if x < 0]
    positivos = [x for x in lista if x >= 0]

    negativos = _radix_positivos(negativos)
    positivos = _radix_positivos(positivos)

    # Los negativos se ordenaron por valor absoluto: se invierten y se regresa el signo
    return [-x for x in reversed(negativos)] + positivos


def _radix_positivos(arr):
    if not arr:
        return []
    arr = arr.copy()
    maximo = max(arr)
    exp = 1                                   # 1 = unidades, 10 = decenas, ...
    while maximo // exp > 0:
        arr = _counting_sort_digito(arr, exp)
        exp *= 10
    return arr


def _counting_sort_digito(arr, exp):
    """Counting sort estable según el dígito indicado por exp."""
    salida = [0] * len(arr)
    conteo = [0] * 10

    for num in arr:
        conteo[(num // exp) % 10] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    for num in reversed(arr):                 # recorrer al revés mantiene la estabilidad
        d = (num // exp) % 10
        conteo[d] -= 1
        salida[conteo[d]] = num
    return salida


def pedir_entero(mensaje, minimo=None):
    """Pide un entero por teclado y repite hasta que sea válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida, escribe un número entero.")


def pedir_numeros():
    """Pide la cantidad de números y luego cada número."""
    cantidad = pedir_entero("¿Cuántos números deseas ordenar? ", minimo=1)
    numeros = []
    for i in range(cantidad):
        numeros.append(pedir_entero(f"  Número {i + 1}: "))
    return numeros


def menu():
    print("\n===== ORDENAMIENTO RADIX SORT =====")
    print("1. Ordenar números")
    print("2. Salir")


def main():
    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            numeros = pedir_numeros()
            print("\nLista original :", numeros)
            print("Lista ordenada :", radix_sort(numeros))
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()