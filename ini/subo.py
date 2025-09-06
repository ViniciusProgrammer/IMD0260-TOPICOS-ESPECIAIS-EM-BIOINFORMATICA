from Bio import SeqIO


def hamming(s1, s2):
    dist = 0
    for x, y in zip(s1, s2):
        if x != y:
            dist += 1
    return dist


def solve_subo(s, t):
    max_occurrences = 0
    best_pattern = ""

    candidate_counts = {}

    for j in range(32, 41):
        for i in range(len(s) - j + 1):
            s_substring = s[i:i + j]

            s_count = 0
            for i2 in range(len(s) - j + 1):
                if hamming(s_substring, s[i2:i2 + j]) <= 3:
                    s_count += 1

            # Conta as ocorrências de s_substring em t
            t_count = 0
            for k in range(len(t) - j + 1):
                if hamming(s_substring, t[k:k + j]) <= 3:
                    t_count += 1

            total_count = s_count + t_count
            if total_count > max_occurrences:
                max_occurrences = total_count
                best_pattern = s_substring

    best_s_count = 0
    for i in range(len(s) - len(best_pattern) + 1):
        if hamming(best_pattern, s[i:i + len(best_pattern)]) <= 3:
            best_s_count += 1

    best_t_count = 0
    for k in range(len(t) - len(best_pattern) + 1):
        if hamming(best_pattern, t[k:k + len(best_pattern)]) <= 3:
            best_t_count += 1

    return best_s_count, best_t_count

try:
    print("Lendo o arquivo rosalind_subo.txt...")
    sequences = [str(record.seq) for record in SeqIO.parse("rosalind_subo.txt", "fasta")]

    if len(sequences) < 2:
        print("Erro: O arquivo deve conter pelo menos duas sequências.")
    else:
        s = sequences[0]
        t = sequences[1]

        print("Processando... Isso pode levar alguns minutos.")
        result_s, result_t = solve_subo(s, t)

        print(f"\nResultado final: {result_s} {result_t}")

except FileNotFoundError:
    print("Erro: O arquivo 'rosalind_subo.txt' não foi encontrado na pasta.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")