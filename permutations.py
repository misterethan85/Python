import itertools

arg = input("")

perm = list("".join(string) for string in itertools.permutations(arg)) #permlist

perm = list(set(perm)) # permuted list without duplicates

print(perm)

