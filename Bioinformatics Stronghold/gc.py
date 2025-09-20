import sys

def parse_fasta(lines):
    """
    Analisa linhas em formato FASTA e retorna um dicionário.
    :param lines: Uma lista de strings (linhas do arquivo).
    :return: Um dicionário com {ID: sequencia}.
    """
    dna_strings = {}
    current_id = ""
    for line in lines:
        if line.startswith('>'):
            # Remove o '>' para obter o ID limpo
            current_id = line[1:]
            dna_strings[current_id] = ""
        else:
            # Concatena as partes da sequência
            dna_strings[current_id] += line
    return dna_strings


def calculate_gc_content(string):
    """
    Calcula o GC content de uma string de DNA.
    :param string: string para calcular o GC content.
    :return: GC content como uma fração (float).
    """
    if len(string) == 0:
        return 0.0
    count_gc = string.count("G") + string.count("C")
    gc_content = count_gc / len(string)
    return gc_content


if __name__ == "__main__":
    # Pega o nome do arquivo passado como argumento na linha de comando
    # Este método é mais robusto e evita erros de terminal.
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Erro: Por favor, forneça o nome do arquivo.")
        print("Uso: python gc.py <nome_do_arquivo.txt>")
        sys.exit(1)  # Sai do programa se nenhum arquivo for fornecido

    # Abre e lê o arquivo
    with open(filename, 'r') as file:
        input_lines = file.read().splitlines()

    # Analisa as linhas para criar um dicionário de sequências de DNA
    dna_strs = parse_fasta(input_lines)

    max_gc_content = -1.0
    max_name = ''

    # Itera sobre o dicionário para encontrar a sequência com o maior GC content
    for name, seq in dna_strs.items():
        gc_content = calculate_gc_content(seq)
        if gc_content > max_gc_content:
            max_name = name
            max_gc_content = gc_content

    # Imprime o resultado no formato exigido
    if max_name:
        print(max_name)
        print(f"{(max_gc_content * 100):.6f}")