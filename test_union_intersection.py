from fa import FA

dfa_a = FA({'q0','q1'}, 'a',
            {('q0', 'a'): 'q1',
            ('q1', 'a'): 'q1'},
            'q0', 'q1', 'Aceita palavras com comprimento > 1')

dfa_b = FA({'q0','q1', 'q2'}, {'a', 'b'},
            {('q0', 'a'): 'q0', ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q1', ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q2', ('q2', 'b'): 'q2'},
            'q0', 'q2', 'Aceita palavras com 2 bs')

united = dfa_a.union(dfa_b)
print(united.compute('a'))
print(united.compute('abba'))
print(united.compute('b'))