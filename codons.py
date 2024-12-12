def create_codon_dict(file_path):
  file = open(file_path)
  rows = file.readlines()
  file.close()
  codon_to_amino= {}
  for row in rows:
    clean=row.strip().split('\t')
    codon=clean[0]
    amino_acid_abbreviation=clean[2]
    codon_to_amino[codon] = amino_acid_abbreviation
  return codon_to_amino
