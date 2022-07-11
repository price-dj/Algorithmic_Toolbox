def get_longest_common_subseq(data):
    substr = []
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_subseq_of_any(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_subseq_of_any(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if not is_subseq(find, data[i]):
            return False
    return True

# Will also return True if possible_subseq == seq.
def is_subseq(possible_subseq, seq):
    if len(possible_subseq) > len(seq):
        return False
    def get_length_n_slices(n):
        for i in range(len(seq) + 1 - n):
            yield seq[i:i+n]
    for slyce in get_length_n_slices(len(possible_subseq)):
        if slyce == possible_subseq:
            return True
    return False

print(get_longest_common_subseq([[8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]]))

#print get_longest_common_subseq(['Oh, hello, my friend.',
                                    # 'I prefer Jelly Belly beans.',
                                    # 'When hell freezes over!'])
