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


def rev_comp(s):
    """Retorna o complemento reverso de uma string de DNA."""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(s))


def reverse_palindromes(string, min_len=4, max_len=12):
    """
    Localiza palíndromos reversos dentro de uma string de DNA.
    :param string: A string de DNA para análise.
    :return: Uma lista de tuplas (posição, comprimento).
    """
    pos_list = []
    # Itera sobre todos os comprimentos de substring possíveis
    for k in range(min_len, max_len + 1):
        # Itera sobre todas as posições de início possíveis
        for i in range(len(string) - k + 1):
            subseq = string[i:i + k]
            # Verifica se a substring é um palíndromo reverso
            if subseq == rev_comp(subseq):
                # Adiciona a posição (baseada em 1) e o comprimento à lista
                pos_list.append((i + 1, k))
    return pos_list


if __name__ == "__main__":
    '''
    Dado: Uma string de DNA em formato FASTA.
    Retorno: A posição e o comprimento de cada palíndromo reverso
             com comprimento entre 4 e 12.
    '''
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Erro: Forneça o nome do arquivo FASTA como argumento.")
        print("Uso: python revp.py <nome_do_arquivo.fasta>")
        sys.exit(1)

    with open(filename, 'r') as file:
        input_lines = file.read().splitlines()

    # Pega a primeira (e única) sequência de DNA do arquivo
    dna_string = list(parse_fasta(input_lines).values())[0]

    positions = reverse_palindromes(dna_string)

    for pos, length in positions:
        print(f"{pos} {length}")