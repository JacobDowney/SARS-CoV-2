import requests
from bs4 import BeautifulSoup

locus_ = "MT461661"

def get_genbank_fasta_url(locus):
    return("https://www.ncbi.nlm.nih.gov/nuccore/" + locus + "?report=fasta")

def get_soup(locus):
    url = get_genbank_fasta_url(locus)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("pre").find(text=True)

maincontent = get_soup(locus_)
print(maincontent)
