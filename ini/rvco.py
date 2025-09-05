# ^_^ coding:utf-8 ^_^

"""
Complementing a Strand of DNA
url: http://rosalind.info/problems/rvco/

Given: A collection of n (n≤10) DNA strings.
Return: The number of given strings that match their reverse complements.
"""

from Bio import SeqIO
from Bio.Seq import Seq


def match_reverse(seqs):
    """
    Calcula o número de sequências de DNA que são iguais aos seus complementos reversos.
    """
    count = 0
    for seq in seqs:
        # Cria um objeto Seq do Biopython. A partir de versões recentes,
        # o alfabeto não precisa ser especificado.
        my_seq = Seq(seq)

        # Obtém o complemento reverso da sequência.
        reverse_seq = my_seq.reverse_complement()

        # Compara a sequência original com seu complemento reverso.
        if my_seq == reverse_seq:
            count += 1

    return count


if __name__ == "__main__":
    # Abre o arquivo de dados fornecido pelo Rosalind.
    # Certifique-se de que o arquivo "rosalind_rvco.txt"
    # está na mesma pasta que este script.
    with open("rosalind_rvco.txt", "r") as f:
        # Lê todas as sequências do arquivo FASTA e as armazena em uma lista.
        seqs = [str(record.seq) for record in SeqIO.parse(f, "fasta")]

    # Chama a função para contar as sequências que se correspondem.
    count = match_reverse(seqs)

    # Imprime o resultado final.
    print(count)