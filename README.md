This project I am going to try to use the skills I've learned in Jin Xiong's
book Essential Bioinformatics.

One of the goals I am going to try to focus on is the mutations over time and
where those mutations were happening and on what date. Something like that is
currently being done on https://nextstrain.org/ncov/global but I want to do that
and relate it to the proportions of deaths and cases in each of the different
countries where there are different mutations.

Some Steps I probably have to take
- Learn about the actual genome and what proteins it is composed of.
- Be able to break down the genome into its proteins and have definitions for
    each of the proteins so that you can see what part is responsible for what
- These different proteins and responsibilities will then be compared to other
    proteins from different locations and times to see how they mutated
- Probably set up a SQL database for storing the different locations and dates
    added for each of the different genome strands. Could be an initial step?

Genbank, https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/ is a great source
for basically sorting the strands based on times and locations to focus on their
changs.


For genbank, this seems to be the format
Locus -
Definition -
Accession -
Version -
DBLink -
Keywords -
Source -
Organism
<a list of> {
  Reference -
  Authors -
  Title -
  Journal -
  Pubmed - <link>
}
Comment -
Features -
  Source - ... collection_date="<some date>"
