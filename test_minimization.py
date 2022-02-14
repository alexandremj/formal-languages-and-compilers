from fa import FA

# 04-Minimizacao p.7
min04_p7 = FA({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}, {'0', '1'},
        {('A', '0'): 'G', ('A', '1'): 'B',
        ('B', '0'): 'F', ('B', '1'): 'E',
        ('C', '0'): 'C', ('C', '1'): 'G',
        ('D', '0'): 'A', ('D', '1'): 'H',
        ('E', '0'): 'E', ('E', '1'): 'A',
        ('F', '0'): 'B', ('F', '1'): 'C',
        ('G', '0'): 'G', ('G', '1'): 'F',
        ('H', '0'): 'H', ('H', '1'): 'D'}, 'A', {'A', 'D', 'G'}
    )
print(min04_p7)
min04_p7.minimize()

ver0506_2 = FA({'S', 'A', 'B', 'C', 'M'}, {'a', 'b', 'c'}, 
        {('S','a'): 'A', ('S','b'): 'B', ('S','c'): 'C',
        ('A','a'): 'M', ('A','b'): 'B', ('A','c'): 'C',
        ('B','a'): 'A', ('B','b'): 'M', ('B','c'): 'C',
        ('C','a'): 'M', ('C','b'): 'M', ('C','c'): 'C',
        ('M','a'): 'M', ('M','b'): 'M', ('M','c'): 'M'},
        'S', {'S', 'A', 'B', 'C'},
        'w nao possui as sequencias aa e bb')
# print(ver0506_2)
ver0506_2.compute('abbababa') # rejeita
ver0506_2.compute('abababab') # aceita
ver0506_2.minimize()
ver0506_2.compute('abbababa') # rejeita
ver0506_2.compute('abababab') # aceita

ver04_1 = FA({'p', 'q', 'r', 's'}, {'0', '1'}, 
        {('p', '0'): ('q', 's'), ('p', '1'): ('q'),
        ('q', '0'): ('r'), ('q', '1'): ('q','r'),
        ('r', '0'): ('s'), ('r', '1'): ('p'),
        ('s', '0'): ('-'), ('s', '1'): ('p')}, 'p', {'q', 's'})
ver04_1.compute('1110010010') # aceita

# add test to &-transitions