def create_codon_dict(file_path):
!mkdir data # Create a folder for the data in the colab
!wget https://raw.githubusercontent.com/yotam-biu/ps6/main/data/codons.txt -O /content/data/codons.txt

path="data/codons.txt"
file = open(path)
rows = file.readlines()
file.close()

codon_to_amino= {}
for row in rows:
  clean=row.strip().split('\t')
  codon=rows[0]
  amino_acid_abbreviation=[2]
  codon_to_amino={codon:amino_acid_abbreviation}

ef create_codon_dict(file_path):
   codon_to_amino= {file(path)}
