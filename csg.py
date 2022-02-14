from grammar import Grammar

""" Desnecessario para o trabalho, implementado para adicionar as restricoes
    a serem herdadas pelas Livres de Contexto e Regulares """
class ContextSensitiveGrammar(Grammar):
    """ Alem das restricoes gerais, Gramaticas Sensiveis ao Contexto tem a
        restricao de producoes terem corpo de tamanho maior ou igual do que a
        cabeca. Caso & pertenca a linguagem precisamos garantir que apenas o
        simbolo inicial derive em & diretamente e nenhuma outra producao
        derive no simbolo inicial"""
    def is_consistent(self):
        # verificacoes padrao para gramaticas
        if not super().is_consistent():
            return super().is_consistent()

        # cada producao deve ter cabeca menor ou igual ao corpo
        for head in self.productions.keys():
            for body in self.productions[head]:
                if len(head) > len(body):
                    return False
        
        # Caso & pertenca a linguagem precisamos garantir que apenas o
        # simbolo inicial derive em & diretamente e nenhuma outra producao
        # derive no simbolo inicial
        has_epsilon = False

        for head in self.productions.keys():
            if not head == self.start_symbol:
                for production in self.productions[head]:
                    if '&' in production:
                        return False
            else:
                for production in self.productions[head]:
                    if '&' in production:
                        has_epsilon = True

            # caso haja epsilon em alguma producao do simbolo inicial, 
            # precisamos garantir que nenhuma outra producao derive no simbolo
            # inicial
            if has_epsilon:
                for production in self.productions.values():
                    for body in production:
                        if self.start_symbol in body:
                            return False
            
            return True