import sys


def parse_fasta(lines):
    """Analisa linhas em formato FASTA e retorna um dicionário."""
    dna_strings = {}
    current_id = ""
    for line in lines:
        if line.startswith('>'):
            current_id = line[1:]
            dna_strings[current_id] = ""
        else:
            dna_strings[current_id] += line
    return dna_strings


def consensus_and_profile(strings):
    """
    Cria uma string de consenso e uma matriz de perfil a partir de uma lista de DNAs.
    :param strings: Lista de strings de DNA de mesmo comprimento.
    :return: Uma tupla contendo (consensus_string, profile_matrix).
    """
    if not strings:
        return "", {}

    str_len = len(strings[0])
    # Inicializa a matriz de perfil com zeros
    profile = {
        'A': [0] * str_len,
        'C': [0] * str_len,
        'G': [0] * str_len,
        'T': [0] * str_len
    }

    # Preenche a matriz de perfil
    for seq in strings:
        for i, base in enumerate(seq):
            profile[base][i] += 1

    # Cria a string de consenso
    consensus_string = ""
    for i in range(str_len):
        max_count = -1
        consensus_base = ''
        for base in ['A', 'C', 'G', 'T']:
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                consensus_base = base
        consensus_string += consensus_base

    return consensus_string, profile


if __name__ == "__main__":
    '''
    Dado: Uma coleção de no máximo 10 strings de DNA de igual comprimento em formato FASTA.
    Retorno: Uma string de consenso e a matriz de perfil.
    '''
    # Use o método de ler o nome do arquivo, que é mais robusto
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Erro: Forneça o nome do arquivo FASTA como argumento.")
        print("Uso: python seu_script.py <nome_do_arquivo.fasta>")
        sys.exit(1)

    with open(filename, 'r') as file:
        input_lines = file.read().splitlines()

    dna_dict = parse_fasta(input_lines)
    dna_list = list(dna_dict.values())

    cons_string, profile_mat = consensus_and_profile(dna_list)

    # Imprime os resultados
    print(cons_string)
    for symbol, counts in profile_mat.items():
        # Converte a lista de contagens em uma string de números separados por espaço
        counts_str = ' '.join(map(str, counts))
        print(f"{symbol}: {counts_str}")