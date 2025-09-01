from Bio import Entrez, SeqIO
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
Entrez.email = "seu_email@exemplo.com"

ids = ["JX205496.1", "JX469991.1"]
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()

with open("rosalind_pairwise.fasta", "w") as f:
    SeqIO.write(records, f, "fasta")

print("Arquivo FASTA criado: 'rosalind_pairwise.fasta'")
