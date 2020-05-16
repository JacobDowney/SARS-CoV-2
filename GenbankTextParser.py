
def read_txt(filename):
    genbank = {}
    with open(filename, 'r') as file:

        # Locus
        info = file.readline().strip().split()
        genbank['locus'] = info[1]

        # Definition
        defs = file.readline().strip().split('  ')[1]
        info = file.readline()
        while info[0] == ' ':
            defs += info.strip()
            info = file.readline()
        genbank['definition'] = defs

        # Feature
        info = file.readline()
        while info[0:8] != 'FEATURES':
            info = file.readline()

        # start_stop
        start_stop = file.readline().split()[1].split('..')
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
        from io import StringIO
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
