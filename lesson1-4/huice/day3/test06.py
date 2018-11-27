from functools import reduce


a = ['adam', 'LISA', 'barT']
print([x.capitalize() for x in a])
print([x[:1].upper()+x[1:].lower() for x in a])

b = [1, 2, 3, 4, 5]


def sum(x):
    return reduce(lambda i, j: i*j, x)

print(sum(b))

