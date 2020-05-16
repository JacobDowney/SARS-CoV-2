# Goal of file is translate from dna sequence to amino acid codon sequence

"""
Taken from : http://www.cryst.bbk.ac.uk/education/AminoAcid/the_twenty.html

Amino Acids
    The structural units (monomers) that make up proteins. They join together to
    form short polymer chains called peptides or longer chains called either
    polypeptides or proteins. These polymers are linear and unbranched, with
    each amino acid within the chain attached to two neighboring amino acids.
------------------
Alanine       - ala - A
Arginine      - arg - R
Asparagine    - asn - N
Aspartic Acid - asp - D
Cysteine      - cys - C
Glutamine     - gln - Q
Glutamic Acid - glu - E
Glycine       - gly - G
Histidine     - his - H
Isoleucine    - ile - I
Leucine       - leu - L
Lysine        - lys - K
Methionine    - met - M
Phenylalanine - phe - F
Proline       - pro - P
Serine        - ser - S
Threonine     - thr - T
Tryptophan    - trp - W
Tyrosine      - tyr - Y
Valine        - val - V

Sometimes it's not possibly to differentiate these closely related amino acids
Asparagine / Aspartic Acid  - asx - B
Glutamine / Glutamic Acid   - glx - Z

Groupings
------------------
Aliphatic - Alanine, Glycine, Isoleucine, Leucine, Proline, Valine
Aromatic - Phenylalanine, Tryptophan, Tyrosine
Acidic - Aspartic Acid, Glutamic Acid
Basic - Arginine, Histidine, Lysine
Hydroxylic - Serine, Thereonine
Sulphur-containing - Cysteine, Methionine
Amidic (containing amide) - Asparagine, Glutamine

Codons
    A sequence of 3 nucleotides which together form a unit of genetic code in a
    DNA or RNA molecule.
------------------
UU: UUU - phe - F   UUC - phe - F   UUA - leu - L   UUG - leu - L
UC: UCU - ser - S   UCC - ser - S   UCA - ser - S   UCG - ser - S
UA: UAU - tyr - Y   UAC - tyr - Y   UAA - STOP      UAG - STOP
UG: UGU - cys - C   UGC - cys - C   UGA - STOP      UGG - trp - W

CU: CUU - leu - L   CUC - leu - L   CUA - leu - L   CUG - leu - L
CC: CCU - pro - P   CCC - pro - P   CCA - pro - P   CCG - pro - P
CA: CAU - his - H   CAC - his - H   CAA - gln - Q   CAG - gln - Q
CG: CGU - arg - R   CGC - arg - R   CGA - arg - R   CGG - arg - R

AU: AUU - ile - I   AUC - ile - I   AUA - ile - I   AUG - met - M
AC: ACU - thr - T   ACC - thr - T   ACA - thr - T   ACG - thr - T
AA: AAU - asn - N   AAC - asn - N   AAA - lys - K   AAG - lys - K
AG: AGU - ser - S   AGC - ser - S   AGA - arg - R   AGG - arg - R

GU: GUU - val - V   GUC - val - V   GUA - val - V   GUG - val - V
GC: GCU - ala - A   GCC - ala - A   GCA - ala - A   GCG - ala - A
GA: GAU - asp - D   GAC - asp - D   GAA - glu - E   GAG - glu - E
GG: GGU - gly - G   GGC - gly - G   GGA - gly - G   GGG - gly - G
"""

codon_map = {
    'GCT' : 'A',    'GCC' : 'A',    'GCA' : 'A',    'GCG' : 'A',
    'TGT' : 'C',    'TGC' : 'C',
    'GAT' : 'D',    'GAC' : 'D',
    'GAA' : 'E',    'GAG' : 'E',
    'TTT' : 'F',    'TTC' : 'F',
    'GGT' : 'G',    'GGC' : 'G',    'GGA' : 'G',    'GGG' : 'G',
    'CAT' : 'H',    'CAC' : 'H',
    'ATT' : 'I',    'ATC' : 'I',    'ATA' : 'I',
    'AAA' : 'K',    'AAG' : 'K',
    'TTA' : 'L',    'TTG' : 'L',    'CTT' : 'L',    'CTC' : 'L',    'CTA' : 'L',    'CTG' : 'L',
    'ATG' : 'M',
    'AAT' : 'N',    'AAC' : 'N',
    'CCT' : 'P',    'CCC' : 'P',    'CCA' : 'P',    'CCG' : 'P',
    'CAA' : 'Q',    'CAG' : 'Q',
    'CGT' : 'R',    'CGC' : 'R',    'CGA' : 'R',    'CGG' : 'R',    'AGA' : 'R',    'AGG' : 'R',
    'TCT' : 'S',    'TCC' : 'S',    'TCA' : 'S',    'TCG' : 'S',    'AGT' : 'S',    'AGC' : 'S',
    'ACT' : 'T',    'ACC' : 'T',    'ACA' : 'T',    'ACG' : 'T',
    'GTT' : 'V',    'GTC' : 'V',    'GTA' : 'V',    'GTG' : 'V',
    'TGG' : 'W',
    'TAT' : 'Y',    'TAC' : 'Y',
    'TAA' : 'STOP', 'TAG' : 'STOP', 'TGA' : 'STOP',
}

def translate(sequence):
    from io import StringIO
    translations = []
    current = 0

    while current < len(sequence) - 3:
        translation = StringIO()
        start = sequence.find('ATG', current)
        if start == -1:
            break
        for current in range(start, len(sequence), 3):
            mapping = codon_map[sequence[current:current+3]]
            if mapping == 'STOP':
                break
            translation.write(mapping)
        value = translation.getvalue()
        if value != "":
            translations.append(value)

    return translations
