# phre.py
# ^_^ coding: utf-8 ^_^
import sys

def count_below_threshold(lines):
    # remove linhas vazias e final \n
    lines = [ln.rstrip("\n") for ln in lines if ln.strip() != ""]
    threshold = int(lines[0].strip())

    count = 0
    # os FASTQ vêm em blocos de 4 linhas a partir da linha 1
    for i in range(1, len(lines), 4):
        # header = lines[i]
        # seq    = lines[i+1]
        # plus   = lines[i+2]
        qual = lines[i+3]

        phreds = [ord(c) - 33 for c in qual]
        avg = sum(phreds) / len(phreds)
        if avg < threshold:
            count += 1
    return count

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()

    print(count_below_threshold(lines))

if __name__ == "__main__":
    main()
