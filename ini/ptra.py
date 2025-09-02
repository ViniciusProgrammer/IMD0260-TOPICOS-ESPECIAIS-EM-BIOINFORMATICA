from Bio.Seq import translate

def genetic_code(dna, protein):
    res = []
    table_ids = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
    for t in table_ids:
        translation = translate(dna, table=t, to_stop=False)
        # compara ignorando STOP (*) no final
        if translation.startswith(protein):
            res.append(t)
    return res

if __name__ == "__main__":
    with open("rosalind_ptra.txt", "r") as f:
        dna = f.readline().strip()
        protein = f.readline().strip()
    res = genetic_code(dna, protein)
    if res:
        print(res[0])
    else:
        print("Nenhuma tabela bateu!")
