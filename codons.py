def create_codon_dict(file_path):
codon_to_amino= {}
for row in rows:
  clean=row.strip().split('\t')
  codon=rows[0]
  amino_acid_abbreviation=[2]
  codon_to_amino={codon:amino_acid_abbreviation}

