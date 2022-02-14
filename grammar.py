
""" 
    Uma classe que representa o conceito matematico de uma gramatica:
    G = (N, T, P, S) onde
    N: simbolos nao-terminais
    T: simbolos terminais
    P: regras de producao
    S: simbolo inicial
"""
class Grammar:

    """
        Constroi uma gramatica de acordo com a explicacao acima. O parametro
        opcional language_description serve para anotar a linguagem descrita
        pela gramatica para facilitar no debugging
    """
    def __init__(self, nonterminals, terminals, productions, start_symbol, 
                language_description=''):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.language_description = language_description

    def __str__(self):
        # monta a string de representacao 
        s = ''

        if self.language_description:
            s += f'Linguagem: {self.language_description}\n'

        s += f'(N)ao-terminais: {self.nonterminals}\n'
        s += f'(T)erminais: {self.terminals} \n'
        s += f'(P)roducoes: {self.productions} \n'
        s += f'(S)imbolo inicial: {self.start_symbol} \n'

        return s
    
    # valida se a gramatica esta consistente. subclasses devem extender a 
    # checagem para suas proprias restricoes. Retorna True caso esteja em um
    # estado consistente, do contrario False
    def is_consistent(self):
        # nao existem producoes com simbolos nao contidos nos atributos da
        # classe
        for key in set(self.productions.keys()):
            if key not in self.nonterminals:
                return False

        # percorre as producoes e retorna um conjunto dos terminais que
        # aparecem em pelo menos uma delas
        produced_terminals = set()

        for body in self.productions.values():
            for symbol in body:
                produced_terminals |= set(symbol)
        
        for terminal in produced_terminals:
            if (terminal not in self.terminals and 
                terminal not in self.nonterminals):
                print(f'{terminal}')
                return False
        
        # o simbolo inicial deriva em alguma coisa
        if self.start_symbol not in set(self.productions.keys()):
            return False

        return True
    