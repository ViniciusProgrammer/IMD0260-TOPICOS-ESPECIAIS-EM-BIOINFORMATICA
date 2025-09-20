import sys

def extract_meme_regex(filepath):
    """
    Analisa um arquivo de saída do MEME e extrai a primeira expressão regular.
    :param filepath: Caminho para o arquivo meme.txt.
    :return: A string da expressão regular, ou None se não for encontrada.
    """
    try:
        with open(filepath, 'r') as f:
            # Procura pela seção do primeiro motif
            in_motif_1_section = False
            for line in f:
                if 'MOTIF ELTTYAEQEGDGTYTSLTMESYDMCYFMVFMQFLVNK MEME-1' in line:
                    in_motif_1_section = True

                # Uma vez na seção correta, procura pela linha da expressão regular
                if in_motif_1_section and 'regular expression' in line:
                    next(f)  # Pula a linha de hífens '-----------------'

                    # A próxima linha é a resposta
                    regex = f.readline().strip()
                    return regex

    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return None

    return None # Retorna None se a seção ou a linha não forem encontradas

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python extract_meme.py <caminho_para_o_arquivo_meme.txt>")
        sys.exit(1)

    meme_output_file = sys.argv[1]

    regular_expression = extract_meme_regex(meme_output_file)

    if regular_expression:
        print("Expressão Regular Encontrada:")
        print(regular_expression)
    else:
        print("Nenhuma expressão regular foi encontrada para o Motif 1 no arquivo.")