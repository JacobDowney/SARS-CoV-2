from io import StringIO

# Gonna work on finding similarities between two different sequences

# Possibly move to C++ for more efficiency if I figure out how to do that

# compare dna seq
# compare amino acid seq

# Global: Needelman-Wunch algorithm
# Local: Smith-Waterman algorithm

"""
Vocabulary from https://www.ncbi.nlm.nih.gov/books/NBK62051/
------------------------------------------------------------
Alignment: The process or result of matching up the nucleotide or amino acid
           residues of two or more biological sequences to achieve maximal
           levels of identity and, in the case of amino acid sequences,
           conservation, for the purpose of assessing the degree of similarity
           and the possobility of homology.
Homology: Similarity attributed to descent from a common ancestor. Homologous
          biological components (genes, proteins, structures) are called
          homologs. See orthologs and paralogs
Orthologs: Homologous biological components (genes, proteins, structures) in
           different species that arose from a single component present in the
           common ancestor of the species; orthologs may or may not have similar
           functions. Often evolves new functions.
Paralogs: Homologous biological components within a single species that arose by
          gene duplication. Often retains the same functions.
- much more
"""

"""
4 ways to get to a piece
1.) Diagonal - match
2.) Diagonal - mismatch
3.) Left - gap in vertical
4.) Up - gap in horizontal

We find the max of those 4 and thats which way you go

Dynamic Programming alignment
"""



"""
(acg, atg, match=1, mismatch=-3, gap=-4)
X   -   A   C   G
-   0   -4  -8  -12
A   -4  1   -3  -7
T   -8  -3  -2  -6
G   -12 -7  -6  -1
"""
def global_sequence_alignment(seq1, seq2, match=1, mismatch=-3, gap=-4):
    h_len = len(seq1) + 1
    v_len = len(seq2) + 1
    matrix = [ [0 for y in range(h_len) ] for x in range(v_len) ]

    # horizontal gaps
    for i in range(1, h_len):
        matrix[0][i] = matrix[0][i-1] + gap

    # vertical gaps
    for i in range(1, v_len):
        matrix[i][0] = matrix[i-1][0] + gap

    # seq1 => hor, seq2 => ver
    for v in range(1, v_len):
        for h in range(1, h_len):
            pos_match = matrix[v-1][h-1]
            pos_match += match if seq1[h-1] == seq2[v-1] else mismatch
            v_h_gap = max(matrix[v-1][h], matrix[v][h-1]) + gap
            matrix[v][h] = max(pos_match, v_h_gap)

    return matrix[-1][-1]

def get_aligned_sequences(seq1, seq2, matrix):
    str1 = StringIO()
    str2 = StringIO()
    h = len(seq1)
    v = len(seq2)
    while h != 0 and v != 0:
        l1 = seq1[h-1]
        l2 = seq2[v-1]
        if matrix[v-1][h-1] >= max(matrix[v-1][h], matrix[v][h-1]):
            v -= 1
            h -= 1
        elif matrix[v-1][h] > matrix[v][h-1]:
            l1 = '-'
            v -= 1
        else:
            l2 = '-'
            h -= 1
        str1.write(l1)
        str2.write(l2)
    while h > 0:
        str1.write(seq1[h])
        str2.write('-')
        h -= 1
    while v > 0:
        str1.write('-')
        str2.write(seq2[v])
        v -= 1
    return(str1.getvalue()[::-1], str2.getvalue()[::-1])


def print_matrix(matrix):
    for line in matrix:
        print(line)

#
