import itertools
def generate_combinations(d):
    lists = d.values()
    combinations = itertools.product(*lists)
    return [ ''.join(combination) for combination in combinations ]
d = {1: ['a', 'b'], 2: ['c', 'd']}
print(','.join(generate_combinations(d)))
