def hanoi(n, col_origem, col_destino, col_aux, passo=[0]):
    if n == 1:
        passo[0] += 1
        print(f"Mover disco 1 de {col_origem} para {col_destino} passo {passo}")
        return
    hanoi(n - 1, col_origem, col_aux, col_destino)
    passo[0] += 1
    print(f"Mover disco {n} de {col_origem} para {col_destino} passo {passo}")
    hanoi(n - 1, col_aux, col_destino, col_origem)

# Executando com 3 discos
hanoi(8, 'col_origem', 'col_destino', 'col_aux')