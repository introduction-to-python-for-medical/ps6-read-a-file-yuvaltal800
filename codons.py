!mkdir data # Create a folder for the data in the colab
!wget https://raw.githubusercontent.com/yotam-biu/ps6/main/data/codons.txt -O /content/data/codons.txt

def create_codon_dict(file_path):
  path="data/codons.txt"
  file = open(path)
  rows = file.readlines()
  file.close()

  codon_to_amino= {}
    for row in rows:
    clean=row.strip().split('\t')
    codon=clean[0]
    amino_acid_abbreviation=clean[2]
    codon_to_amino[codon] = amino_acid_abbreviation

   codon_to_amino= {file(path)}
