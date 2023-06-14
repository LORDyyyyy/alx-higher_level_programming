#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary.values())[0]
    score = ""
    for key, value in a_dictionary.items():
        if max < value:
            score = key
    return score
