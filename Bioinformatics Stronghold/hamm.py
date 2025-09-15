import sys
import rosalind_utility

if __name__ == "__main__":

    input_lines = sys.stdin.read().splitlines()
    s1 = input_lines[0]
    s2 = input_lines[1]
    print(hamming_dist(s1, s2))