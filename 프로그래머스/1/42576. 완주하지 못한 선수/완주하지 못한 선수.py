def solution(participant, completion):
    dictionary = {}
    for p in participant:
        if p in dictionary:
            dictionary[p] += 1
        else:
            dictionary.update({p : 1})
    for c in completion:
        if c in dictionary:
            dictionary[c] -= 1
        if dictionary[c] == 0:
            dictionary.pop(c)
    result_list = list(dictionary.keys())
    return result_list[0]