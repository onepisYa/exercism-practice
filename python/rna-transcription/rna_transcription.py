# 1
TRANS=dict(G="C",C="G",T="A",A="U")
def to_rna(dna_strand):
    return "".join(TRANS.get(i) for i in dna_strand)

# 2 
trans = str.maketrans("GCTA", "CGAU")
def to_rna(dna_strand):
    return dna_string.translate(trans)
