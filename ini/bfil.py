from Bio import SeqIO

def Base_Filtration_Quality(data):
    records = []
    with open(data, "r") as f:
        t = int(f.readline().strip())
        for record in SeqIO.parse(f, "fastq"):
            phred = record.letter_annotations["phred_quality"]
            start, end = 0, len(phred)
            while phred[start] < t:
                start += 1
            while phred[end-1] < t:
                end -= 1
            print(record[start:end].format('fastq'))

if __name__ == "__main__":
    data = "rosalind_bfil.txt"
    Base_Filtration_Quality(data)