from grammar import Grammar

g = Grammar(('S'), ('a', 'b', 'c'), {'S': ('aSa', 'bSb','c')}, 'S',
            'L = {wcw^r | w \in {a,b}*}')

print(g)
print(g.is_consistent())