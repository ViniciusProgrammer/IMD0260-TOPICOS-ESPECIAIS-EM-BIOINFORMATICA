import sys


def hamming_dist(s1, s2):
    """
    Calcula a distância de Hamming entre duas strings de mesmo comprimento.
    :param s1: A primeira string.
    :param s2: A segunda string.
    :return: A distância de Hamming (int).
    """
    distancia = 0
    # Itera sobre cada posição nas strings
    for i in range(len(s1)):
        # Se os caracteres na mesma posição forem diferentes, aumenta a distância
        if s1[i] != s2[i]:
            distancia += 1
    return distancia

if __name__ == "__main__":
    '''
    Dado: Duas strings de DNA s e t de igual comprimento (não excedendo 1 kbp).
    Retorno: A distância de Hamming dH(s,t).
    '''
    try:
        # Lê as duas linhas da entrada padrão
        input_lines = sys.stdin.read().splitlines()
        s1 = input_lines[0]
        s2 = input_lines[1]

        # Calcula e imprime a distância de Hamming
        print(hamming_dist(s1, s2))

    except IndexError:
        print("Erro: A entrada precisa conter duas linhas de DNA.")