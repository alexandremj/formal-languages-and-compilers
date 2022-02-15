from itertools import chain, combinations

import copy



# receita pronta disponibilizada pelo itertools
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



def subsearch(l, c):
    i = 0

    while i < len(l):
        for char in l[i]:
            if char == c:
                return i
        i += 1
    
    return len(l)



""" Uma classe que representa automatos finitos:
    M = (Q, \Sigma, \delta, q_0, F) onde
    Q       : conjunto de estados
    \Sigma  : alfabeto
    \delta  : funcao de transicao
    q_0     : estado inicial
    F       : estados de aceitacao

"""
class FA:
    """
        Constroi um automato de acordo com a explicacao acima. O parametro
        opcional language_description serve para anotar a linguagem descrita
        pelo automato para facilitar no debugging
    """
    def __init__(self, states=set(), alphabet=set(), transition_function=dict(),
                start_state='q0', accept_states=set(),  language_description=''):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.language_description = language_description



    def __str__(self):
        # monta a string de representacao 
        s = ''

        if self.language_description:
            s += f'Linguagem: {self.language_description}\n'

        s += f'Estados: {self.states}\n'
        s += f'Alfabeto: {self.alphabet} \n'
        s += f'Funcao de transicao: {self.transition_function} \n'
        s += f'Estado inicial: {self.start_state} \n'
        s += f'Estados de aceitacao: {self.accept_states} \n'
        s += '-' * 73

        return s
    


    """ Item A: Conversao de AFND (com e sem \epsilon para AFD)"""
    def determinization(self):
        print('\n\n' + '=' * 28 + ' Determinizacao ' + '=' * 28)

        det = FA(language_description=self.language_description)
        det.states = set(powerset(self.states))
        det.alphabet = self.alphabet
        det.start_state = self.start_state

        for s in det.states:
            if s == set():
                continue
            else:
                for elem in s:
                    if elem in self.accept_states:
                        det.accept_states.add(s)
                        break
        
        keys = self.transition_function.keys()

        # cria um conjunto de estados que contem epsilon transicoes para
        # facilitar a computacao mais para frente
        contains_epsilon_transition = set()
        for key in keys:
            key = tuple(key)
            if len(key):
                if key[-1] == '&':
                    contains_epsilon_transition.add(key[0:-1])


        # TODO: add epsilon
        for state in det.states:
            if state != set():
                t_state = tuple(sorted(state))
                for symbol in self.alphabet:
                    result = tuple()

                    for elem in t_state:
                        if (elem, symbol) in keys:
                            r = self.transition_function[elem, symbol]
                            result = result + tuple(r)

                    det.transition_function[t_state, symbol] = result

        if len(contains_epsilon_transition):
            pass
            # epsilon_transitions = state in contains_epsilon_transition
            # current = state
            # epsilon_closure = set()
            # while epsilon_transitions:
            #     next = self.transition_function[(current, '&')]
            #     epsilon_closure = epsilon_closure.union({next})
            #     if next in contains_epsilon_transition:
            #         current = next
            #     else:
            #         epsilon_transitions = False

            # # limpa caso um mesmo estado tenha sido adicionado mais
            # # de uma vez e ordena
            # print(f'&-fecho({tuple(sorted(t_state))}): {epsilon_closure}')
            # result = tuple(sorted(set(result).union(epsilon_closure)))
        return det


    

    """ Item B: Reconhecimento de sentencas em AF """
    def compute(self, sentence):
        print('\n\n' + '=' * 30 + ' Computacao ' + '=' * 31)
        print(f'Computando a palavra {sentence}')

        current_states = {self.start_state}

        for c in sentence:
            next_states = set()

            print(f'Computing {c} in states {current_states}')

            for state in current_states:
                print(f'state: {state}')
                # try:
                next_state = self.transition_function[(state, c)]

                if next_state != '-':
                    for s in next_state:
                        next_states = next_states.union({s})

                
                # except KeyError:
                #     continue

            current_states = next_states
            print(f'{next_states}')
        
        accepted = False

        for state in current_states:
            if state in self.accept_states:
                accepted = True

        if accepted:
            print(f'Palavra {sentence} pertence a {self.language_description}')
        else:
            print(f'Palavra {sentence} rejeitada')
        
        return accepted
    


    """ Item C: Minimizacao de AF
    
        Necessario determinizar antes!
    """
    def minimize(self):
        print('\n\n' + '=' * 30 + ' Minimizacao ' + '=' * 30)
        dummy = copy.deepcopy(self)

        # remove inalcancaveis
        reachable = set([dummy.start_state])
        new_states = set([dummy.start_state])

        while len(new_states):
            temp = set()

            for state in new_states:
                for symbol in dummy.alphabet:
                    next_state = dummy.transition_function[state, symbol]
                    if not next_state in reachable:
                        temp.add(next_state)

            reachable = reachable.union(temp)
            new_states = temp
            
        
        unreachable = dummy.states - reachable

        dummy.states = reachable
        dummy.accept_states = {s for s in reachable if s in dummy.accept_states}
        print(f'Estados inalcancaveis: {unreachable}')

        # remove mortos
        alive = dummy.accept_states
        new_states = dummy.accept_states

        while len(new_states):
            temp = set()

            for key in dummy.transition_function:
                if dummy.transition_function[key] in alive:
                    if key[0] not in alive:
                        temp.add(key[0])
            
            alive = alive.union(temp)
            new_states = temp

        dead = dummy.states - alive
        print(f'Estados mortos: {dead}')

        dummy.states = alive        
        
        # classes de equivalencia
        # comecamos com F e K-F
        old_classes = [dummy.accept_states,
                        dummy.states.difference(dummy.accept_states)]

        for class_ in old_classes:
            new_classes = []

            if len(class_) < 2:
                new_classes.append(class_)
                continue

            print(f'old: {old_classes}')
            pairs = list(combinations(class_, 2))

            print(pairs)

            for pair in pairs:
                same_class = True
                for symbol in self.alphabet:
                    a, b = pair
                    if (subsearch(old_classes, self.transition_function[a, symbol])
                        != subsearch(old_classes, self.transition_function[b, symbol])):
                        new_classes.append(set(a))
                        new_classes.append(set(b))
                        same_class = False
                
                inserted = False
                if same_class:
                    for _ in new_classes:
                        if a in _:
                            _ = _.union(set(b))
                            inserted = True
                        elif b in _:
                            _ = _.union(set(a))
                            inserted = True
                
                if not inserted:
                    new_classes.append({a, b})                    

        print(f'Classes de Equivalencia: {new_classes}')
        print('-' * 73)



    """ Item D: Uniao e intersecao de AFD """
    def union(self, other):
        print('\n\n' + '=' * 28 + ' Uniao ' + '=' * 27)
        A_states = {'A_' + state for state in self.states}
        B_states = {'B_' + state for state in other.states}

        new_states = A_states.union(B_states)

        A_alphabet = {'A_' + symbol for symbol in self.alphabet}
        B_alphabet = {'B_' + symbol for symbol in self.alphabet}

        new_alphabet = A_alphabet.union(B_alphabet)

        new_transition_function = dict()

        for key in self.transition_function:
            new_key = tuple('A_' + elem for elem in key)
            new_transition_function[new_key] = self.transition_function[key]

        for key in other.transition_function:
            new_key = tuple('B_' + elem for elem in key)
            new_transition_function[new_key] = other.transition_function[key]

        new_start_state = 'S'
        new_transition_function[(new_start_state, '&')] = ('A_' + self.start_state,
                                                        'B_' + self.start_state)
        
        A_accept_states = {'A_' + ''.join(sorted(self.accept_states, reverse=True))}
        B_accept_states = {'B_' + ''.join(sorted(self.accept_states, reverse=True))}

        new_accept_states = A_accept_states.union(B_accept_states)

        new = FA(new_states, new_alphabet, new_transition_function,
                new_start_state, new_accept_states)
        print(new)
        return new
    


    def intersection(self, other):
        print('\n\n' + '=' * 30 + ' Intersecao ' + '=' * 30)

    

    """ Item E: Conversao de ER para AFD (usando o algoritmo baseado em arvore
        sintatica - Livro Aho - secao 3.9)

        Constroi um AFD com base na regex passada    
    
    """
    def from_regex(regex):
        print('\n\n' + '=' * 26 + ' Conversao ER -> AFD ' + '=' * 25)
