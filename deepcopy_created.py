def deep_copy(l):
    if type(l[0]) != list:
        return [i for i in l]
    else:
        return [deep_copy(l[i]) for i in range(len(l))]
