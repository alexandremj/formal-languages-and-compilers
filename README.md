# formal-languages-and-compilers
Trabalho da Disciplina INE5421 - Linguagens Formais e Compiladores

## Primeira entrega
### Alexandre Müller Júnior - 16102858

Requisitos: Python 3.X

Instalação:
``git clone https://github.com/alexandremj/formal-languages-and-compilers``

Execução (da pasta do projeto):
``python3 <arquivo_de_teste>``, exemplo: ``python3 test_minimization.py``

Também é possível escrever seus próprios arquivos de teste para a classe ``FA.py``, basta apenas manter compatibilidade com os métodos originais

# TL;DR (Too Long, Didn't Run)
### O que funciona?
- Computação determinística e não determinística sem & transições
- Detecção de estados inalcançáveis e estados mortos
- União de autômatos
- Determinização sem & transições

### O que não funciona?
- Determinização com & transições
- Computação com & transições
- Intersecção de autômatos
- Conversão ER → AFD
- Computação não-determinística com & transições
- Construção de classes de equivalência

Para quaisquer dúvidas, não deixe de me contatar em alexandre.muller \[at\] grad.ufsc.br