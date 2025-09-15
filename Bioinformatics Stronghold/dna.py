import sys

def count_symbols(string):
    symbols = sorted(set(string))

    counts_list = []
    for sym in symbols:
        counts_list.append(string.count(sym))
    return counts_list


if __name__ == "__main__":
    DNA_string = sys.stdin.read().splitlines()[0]
    print(' '.join(str(c) for c in count_symbols(DNA_string)))