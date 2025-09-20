import sys


def parse_fasta(lines):
    """Parses lines in FASTA format and returns a dictionary."""
    dna_strings = {}
    current_id = ""
    for line in lines:
        if line.startswith('>'):
            current_id = line[1:]
            dna_strings[current_id] = ""
        else:
            dna_strings[current_id] += line
    return dna_strings


def lcsm(strings_list):
    """
    Finds the longest common substring among a list of DNA strings.
    :param strings_list: list of DNA strings.
    :return: the longest common substring.
    """
    if not strings_list:
        return ""

    # Find the shortest string to use as a reference
    min_len_string = min(strings_list, key=len)
    other_strings = [s for s in strings_list if s != min_len_string]

    # Iterate from the longest possible substring length down to 1
    for k in range(len(min_len_string), 0, -1):
        for i in range(len(min_len_string) - k + 1):
            substring = min_len_string[i:i + k]
            # Use all() for a cleaner check to see if the substring is in all other strings
            if all(substring in other for other in other_strings):
                return substring

    return ""  # Should not be reached if there are common bases


if __name__ == "__main__":
    '''
    Given: A collection of k DNA strings of length at most 1 kbp each in FASTA format.
    Return: A longest common substring of the collection.
    '''
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Error: Please provide the FASTA file name as an argument.")
        print("Usage: python lcsm.py <your_file.txt>")
        sys.exit(1)

    with open(filename, 'r') as file:
        input_lines = file.read().splitlines()

    strings_dict = parse_fasta(input_lines)
    DNA_strings = list(strings_dict.values())

    print(lcsm(DNA_strings))