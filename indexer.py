from modules import *

# Constructing Positional Indexing

def get_pos_index(d):    # used Positional Indexing for Indexing part

    posiIndex = {}
    rows = d["source_tokenized"]
    for idx, row in enumerate(rows):
        for pos, term in enumerate(row.split()):
            if term in posiIndex:
                posiIndex[term][0] = posiIndex[term][0]+1
                if idx in posiIndex[term][1]:
                    posiIndex[term][1][idx].append(pos)
                else:
                    posiIndex[term][1][idx] = [pos]
            else:
                posiIndex[term] = []
                posiIndex[term].append(1)
                posiIndex[term].append({})
                posiIndex[term][1][idx] = [pos]
    return d
