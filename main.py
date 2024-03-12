# Importar o lexer do ply
from lex import lex
from sys import exit

tokens = ('CONSTANTE_INTEIRA', 'OPERADOR_ARITMETICO')

# Regex
t_CONSTANTE_INTEIRA = "\d+"
t_OPERADOR_ARITMETICO = "\+|\-|\*|\/" 
t_ignore = " "

def t_error(t):
    print(t.value, 'Esta zoado')
    exit(0)

expressao = "101 + 2 - 5 / 45 & "

# Criar um novo objeto LEXER
lexer = lex()

# Carregar a fita de entrada do LEXER
lexer.input(expressao)

while True:
    # Ler o proximo token
    t = lexer.token()
    # Leu um token invalido, para
    if not t:
        break

    print('LEXEMA: ',t.value)
    print('TIPO: ',t.type)
    print('LINHA: ',t.lineno)
    print('COLUNA: ',t.lexpos)
    print('')