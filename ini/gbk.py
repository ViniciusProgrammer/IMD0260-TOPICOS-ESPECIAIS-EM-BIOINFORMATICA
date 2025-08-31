from Bio import Entrez

def get_Nucleotide_GenBank_entries(genus_name, date1, date2):
    Entrez.email = "seu.email@exemplo.com"
    term = f'"{genus_name}"[Organism] AND ("{date1}"[Publication Date] : "{date2}"[Publication Date])'
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    handle.close()

    return record["Count"]

if __name__ == "__main__":
    try:
        with open("rosalind_gbk.txt", "r") as f:
            genus_name = f.readline().strip()
            date1 = f.readline().strip()
            date2 = f.readline().strip()
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Verifique o caminho.")
        genus_name = "Anthoxanthum"
        date1 = "2003/07/25"
        date2 = "2005/12/27"

    count = get_Nucleotide_GenBank_entries(genus_name, date1, date2)
    print(count)