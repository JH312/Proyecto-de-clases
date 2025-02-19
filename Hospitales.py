import numpy as np

def m_hospitales(m, n, num_Hospi):
    matriz = np.zeros((m, n), dtype=int)

    p= [(i, j) for i in range(m) for j in range(n)]

    np.random.shuffle(p)

    for i in range(min(num_Hospi, len(p))):
        x, y = p[i]
        matriz[x, y] = 1

    return matriz

def main():
    num_Hospi = int(input("Cuantos hospitales deseas ordenar?"))
    m = int(input("Digite el numero de filas:"))
    n = int(input("Digite el numero de columnas:"))

    matriz_hospi = m_hospitales(m, n, num_Hospi)

    print("Matriz para hospitales aleatorios")
    print(matriz_hospi)
if __name__ == '__main__':
    main()