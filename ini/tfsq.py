from Bio import SeqIO

fastq_file = "rosalind_tfsq.txt"
fasta_file = "answer.txt"

SeqIO.convert(fastq_file, "fastq", fasta_file, "fasta")
