from modules import *

# Constructing Positional Indexing

def get_pos_index(data):

    pos_index = {}
    rows = data["source_tokenized"]

    for idx, row in enumerate(rows):
        for pos, term in enumerate(row.split()):
            if term in pos_index:
                pos_index[term][0] = pos_index[term][0]+1
                if idx in pos_index[term][1]:
                    pos_index[term][1][idx].append(pos)
                else:
                    pos_index[term][1][idx] = [pos]
            else:
                pos_index[term] = []
                pos_index[term].append(1)
                pos_index[term].append({})
                pos_index[term][1][idx] = [pos]
    return data
