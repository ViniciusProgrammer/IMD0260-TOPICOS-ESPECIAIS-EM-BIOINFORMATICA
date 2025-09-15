import sys
from rosalind_utility import parse_fasta

def calculate_gc_content(string):

    count_gc = string.count("G") + string.count("C")
    gc_content = count_gc / len(string)
    return gc_content

if __name__ == "__main__":

    input_lines = sys.stdin.read().splitlines()
    DNA_strs = parse_fasta(input_lines)
    max_GC_content = -1
    max_name = ''
    for name, seq in DNA_strs.items():
        GC_content = calculate_gc_content(seq)
        if GC_content > max_GC_content:
            max_name = name
            max_GC_content = GC_content
    print(max_name)
    print(max_GC_content * 100)