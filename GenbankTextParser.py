from io import StringIO

def read_txt(filename):
    genbank = {}
    with open(filename, 'r') as file:

        # Locus
        genbank['locus'] = file.readline().strip().split()[1]

        # Definition
        definition = StringIO()
        definition.write(file.readline().strip().split('  ')[1])
        info = file.readline()
        while info[0] == ' ':
            definition.write(info.strip())
            info = file.readline()
        genbank['definition'] = definition.getvalue()

        # Feature
        info = file.readline()
        str_ = 'FEATURES'
        while info[0:len(str_)] != str_:
            info = file.readline()

        # start_stop
        info = file.readline().split()
        while info[0] != 'source':
            info = file.readline().split()
        start_stop = info[1].split('..')
        genbank['start_stop'] = (int(start_stop[0]) - 1, int(start_stop[1]))

        # country
        info = file.readline().strip()
        str_ = "/country="
        while info[0:len(str_)] != str_:
            info = file.readline().strip()
        genbank['country'] = info[len(str_)+1:-1]

        # collection_date
        info = file.readline().strip()
        str_ = "/collection_date="
        while info[0:len(str_)] != str_:
            info = file.readline().strip()
        genbank['collection_date'] = info[len(str_)+1:-1]


        # gene and cds analyzer


        # origin
        info = file.readline().strip()
        str_ = "ORIGIN"
        while info[0:len(str_)] != str_:
            info = file.readline().strip()
        sequence = StringIO()
        info = file.readline()
        while len(info) > 0:
            sequence.write(info[10:].strip().replace(' ', ''))
            info = file.readline()
        genbank['sequence'] = sequence.getvalue()

    return genbank


if __name__ == '__main__':
    txt_file = 'FastaFiles/MT291830.txt'
    gb = read_txt(txt_file)
    print(gb)
