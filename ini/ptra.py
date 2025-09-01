# Protein Translation
# Requer a biblioteca Biopython. Se não tiver, instale com: pip install biopython

from Bio.Seq import Seq


def solve_protein_translation(file_path):
    """
    Lê um arquivo de dados do Rosalind e encontra o índice da tabela
    de código genético usada para traduzir o DNA na proteína fornecida.

    Args:
        file_path (str): O caminho para o arquivo de dados.
    """
    try:
        with open(file_path) as f:
            dna, prot = f.read().splitlines()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return

    # Lista dos índices das tabelas de código genético a serem testadas.
    # Esta lista é fornecida na descrição do problema do Rosalind.
    code_tables = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

    for table_index in code_tables:
        # Traduz a sequência de DNA usando a tabela atual.
        # to_stop=True ignora o restante da sequência após um códon de parada.
        translated_protein = str(Seq(dna).translate(table=table_index, to_stop=True))

        # Compara a proteína traduzida com a proteína esperada.
        if prot == translated_protein:
            print(table_index)
            # Uma vez que a solução é encontrada, o programa termina.
            return


# Para executar o script a partir da linha de comando
if __name__ == "__main__":
    import sys

    # Verifica se o nome do arquivo de dados foi fornecido.
    if len(sys.argv) > 1:
        solve_protein_translation(sys.argv[1])
    else:
        print("Uso: python nome_do_seu_arquivo.py rosalind_ptra.txt")