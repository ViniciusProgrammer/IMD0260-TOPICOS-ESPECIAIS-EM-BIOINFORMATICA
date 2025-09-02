from Bio.Seq import translate
from Bio.Data import CodonTable

def genetic_code(dna, protein):
    dna = dna.upper().strip()
    protein = protein.strip()
    res = []
    for t in CodonTable.ambiguous_generic_by_id:
        translation = str(translate(dna, table=t, to_stop=False))
        translation = translation.replace("*", "")  # alguns códigos ainda podem ter STOPs
        if translation == protein:
            res.append(t)
    return res

if __name__ == "__main__":
    with open("rosalind_ptra.txt", "r") as f:
        dna = f.readline().strip()
        protein = f.readline().strip()
    res = genetic_code(dna, protein)
    if res:
        print(res[0])   # imprime o primeiro índice válido
    else:
        print("Nenhuma tabela bateu!")
