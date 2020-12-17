
import math
import pickle
import SequenceAlignment as sq
import Translate as translate

def get_score(seq_1, seq_2):
    return (sq.global_sequence_alignment(seq_1, seq_2) / len(seq_1)) ** 2

def read_sequence(seq_name, type='translations'):
    with open(f'FastaFiles/{type}/{seq_name}', 'r') as seq_file:
        return seq_file.read().replace('\n', '')
    return -1

def get_sorted_keys(sequences):
    keys = [key for key in sequences]
    sort_date = sorted(keys, key = lambda x : sequences[x]['collection_date'])
    return sorted(sort_date, key = lambda x : sequences[x]['location'])

def compare_sequences(seq_1, seq_2, seq_len=500):
    min_len = min(len(seq_1), len(seq_2))
    max_len = max(len(seq_1), len(seq_2))
    incr = int(seq_len / 2)
    scores = [0] * math.ceil(min_len / incr)
    for i in range(len(scores)-1):
        start = i * incr
        scores[i] = get_score(seq_1[start:start+incr], seq_2[start:start+incr])
    start = (len(scores) - 1) * incr
    scores[-1] = get_score(seq_1[start:min_len], seq_2[start:min_len])

    accuracy = sum(scores) / len(scores)
    return accuracy

def pickle_sequences():
    sequences = {}
    with open('FastaFiles/contents', 'r') as content_file:
        for content in content_file.read().split('\n\n'):
            info = content.split('\n')
            name = info[0]
            sequences[name] = {}
            sequences[name]['link'] = info[1]
            sequences[name]['description'] = info[2]
            sequences[name]['location'] = info[3]
            sequences[name]['collection_date'] = info[4]
            with open(f'FastaFiles/sequences/{name}', 'r') as seq_file:
                seq = seq_file.read().replace('\n', '')
                for c in seq:
                    if c != 'A' and c != 'C' and c != 'T' and c != 'G':
                        print("ERROR IN: ", name, c)
                sequences[name]['sequence'] = seq
                sequences[name]['my_translation'] = ''.join(translate.translate(seq))
            with open(f'FastaFiles/translations/{name}', 'r') as trans_file:
                sequences[name]['translation'] = trans_file.read().replace('\n', '')
    with open('sequences.pkl', 'wb') as f:
        pickle.dump(sequences, f)

def depickle_sequences():
    with open('sequences.pkl', 'rb') as f:
        return pickle.load(f)

def pickle_comparisons(sequences, type='translation'):
    keys = get_sorted_keys(sequences)
    sequence_comparisons = {}
    for key in keys:
        sequence_comparisons[key] = {}
    for i in range(1, len(keys)):
        seq_1 = keys[i]
        type_1 = sequences[seq_1][type]
        print(f'{i} / 20')
        for j in range(i):
            seq_2 = keys[j]
            type_2 = sequences[seq_2][type]
            score = round(compare_sequences(type_1, type_2), 4)
            sequence_comparisons[seq_1][seq_2] = score
            sequence_comparisons[seq_2][seq_1] = score

    file_name = f'{type}_comparisons.pkl'
    with open(file_name, 'wb') as f:
        pickle.dump(sequence_comparisons, f)

def depickle_comparisons(type='sequence'):
    file_name = f'{type}_comparisons.pkl'
    with open(file_name, 'rb') as f:
        return pickle.load(f)



# trans = depickle_comparisons('translation')
# seqs = depickle_comparisons('sequence')
# for key1 in seqs:
#     for key2 in seqs[key1]:
#         print(key1, key2, round(trans[key1][key2], 4),  seqs[key1][key2])

def print_by_location():
    sequences = depickle_sequences()
    seqs = depickle_comparisons('sequence')
    trans = depickle_comparisons('my_translation')
    my_trans = depickle_comparisons('translation')

    by_location = {}
    for sequence in sequences:
        location = sequences[sequence]['location']
        if location in by_location:
            by_location[location].append(sequence)
        else:
            by_location[location] = [sequence]

    for location in by_location:
        print(location)

        keys = by_location[location]
        key_list = []
        for key in keys:
            key_list.append(key)

        table = [[0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6, [0] * 6]

        for i in range(6):
            for j in range(6):
                if i == j:
                    table[i][j] = '0.0000'
                    continue # cancels out crosses
                if i == 0:
                    table[i][j] = sequences[key_list[j-1]]['collection_date']
                    continue
                elif j == 0:
                    table[i][j] = sequences[key_list[i-1]]['collection_date']
                    continue
                else:
                    table[i][j] = ' ' + str(seqs[key_list[i-1]][key_list[j-1]]) + ' '
                    continue
        for tab in table:
            print(tab)

def main():
    sequences = depickle_sequences()
    seqs = depickle_comparisons('sequence')
    trans = depickle_comparisons('my_translation')
    my_trans = depickle_comparisons('translation')

    ts = trans['MT396241']
    t = 0
    c = 0
    for key in ts:
        c += ts[key]
        t += 1
    print (c / t)




if __name__ == '__main__':
    main()
else:
    print("not supported")
