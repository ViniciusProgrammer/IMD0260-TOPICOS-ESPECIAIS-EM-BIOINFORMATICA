from Bio import SeqIO


def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)

    return dp[m][n]


def solve_the_odd_one_out(file_path):
    try:
        sequences = []
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append((record.id, str(record.seq)))

        if not sequences:
            print("Erro: Nenhum registro de sequência encontrado no arquivo.")
            return

        num_sequences = len(sequences)
        total_distances = {}
        for seq_id, _ in sequences:
            total_distances[seq_id] = 0

        for i in range(num_sequences):
            for j in range(i + 1, num_sequences):
                id1, seq1 = sequences[i]
                id2, seq2 = sequences[j]

                dist = levenshtein_distance(seq1, seq2)

                total_distances[id1] += dist
                total_distances[id2] += dist

        most_different_id = max(total_distances, key=total_distances.get)

        print(most_different_id)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

solve_the_odd_one_out("rosalind_clus.txt")