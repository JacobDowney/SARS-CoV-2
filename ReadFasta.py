
def read_from_file(filename):
    fasta = {}
    genome = ''
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == '>':
                fasta['name'] = line[1:].rstrip()
            else:
                genome += line.rstrip()
    fasta['genome'] = genome
    return fasta

# This is assuming the format I made
def make_genome_from_txt(filename):
    genome = {}
    with open(filename, 'r') as file:
        genome['locus'] = file.readline().rstrip()
        genome['description'] = file.readline().rstrip()
        genome['location'] = file.readline().rstrip()
        genome['data_collected'] = file.readline().rstrip()
        sequence = ""
        for line in file:
            sequence += line.rstrip()
        genome['sequence'] = sequence
    return genome



def read_files():
    files = [
        "MT019529.txt"
    ]
    for file in files:
        fasta_file = "FastaFiles/" + file
        fasta = make_genome_from_txt(fasta_file)
        #print(fasta)


# https://www2.le.ac.uk/projects/vgec/highereducation/topics/geneexpression-regulation
# Gene expression: the process by which the genetic code - the nucleotide
#                  sequence - of a gene is used to direct protein synthesis and
#                  produce the structures of the cell. Genes that code for amino
#                  acid sequences are known as 'structural genes'
#                  transcription then translation
# Transcription: the production of messenger RNA (mRNA) by the enzyme RNA
#                polymerase, and the processing of the resulting mRNA module.
# Translation: the use of mRNA to direct protein synthesis, and the subsequent
#              post-translational processing of the protein molecule.
#               amino acid translation???

def single_file():
    file = "FastaFiles/MT019529.txt"
    genome = make_genome_from_txt(file)

    sequence = genome['sequence']               #29899

    # https://www.ncbi.nlm.nih.gov/nuccore/MT019529


    # 5'UTR
    # https://www.ncbi.nlm.nih.gov/nuccore/MT019529.1?from=1&to=265
    # 1..265
    #
    _5UTR = sequence[:265]


    # Its link is: the same + ".1?location=266:13468,13468:21555"



    # Basically encach section has a "gene" and a "CDS" section
    # gene: gives us the overall start finish and gene name
    #       LINK: source, gene, translation, and genome
    # CDS: this gives us all the real information that we need. it is basically
    #      the gene section but with more info. This does have a protein id link
    #      in it that you can use.
    #      LINK: source, gene, translation, genome
    #      PROTEINIDLINK: source, gene, translation
    #
    # KEY TAKEAWAY
    # the links themselves aren't that helpful bc everything in the links are
    # already shown in the main link's info
    # We get: start, stop, gene name, product name, translation, protein id, etc



    # join(266..13468,13468..21555)
    # gene = orf1ab
    # ribosomal_slippage                                    What does this mean
    # note= pp1ab; translated by -1 ribosomal frameshift      Correlation?
    # product = orf1ab polyprotein                          look what that is
    # protein id = https://www.ncbi.nlm.nih.gov/protein/1805293612
    # translation = ...
    orf1ab = sequence[265:21555] # -> gets translated to the translation
    # TODO: probably gonna wanna get the translation at some point

    # GAP OF STUFF FROM 21555 -> 21563 (13)

    # 21563..25384
    # gene = s
    # note = structural protein
    # product = surface glycoprotein                        wtf is that
    # protein id = https://www.ncbi.nlm.nih.gov/protein/1805293613
    # translation = ...
    s = sequence[21562:25384]

    # GAP 25384 -> 25393 (7)

    # 25393..26220
    # gene = orf3a

    print(s)



if __name__ == '__main__':
    single_file()
