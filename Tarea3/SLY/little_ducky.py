# littleducky.py by Paulina Cámara (2021)
# Lexer and Parser program using ply

from sly import Lexer, Parser

# ***** LEXER *****

class CalcLexer(Lexer):
# Tokens
    tokens = [
        'INT',
        'FLOAT',
        'STRING',
        'PROGRAM',
        'ID',
        'COMMA',
        'COLON',
        'SEMICOLON',
        'LEFT_PAR',
        'RIGHT_PAR',
        'LEFT_CURVBR',
        'RIGHT_CURVBR',
        'LESS',
        'GREATER',
        'DIFFERENT',
        'EQUAL',
        'PLUS',
        'MINUS',
        'MULTIPLY',
        'DIVIDE',
        'IF',
        'ELSE',
        'VAR',
        'PRINT'
    ]

# Token definitions
    PROGRAM = r'program'
    ID = r'[a-z][a-zA-Z0-9]*'
    STRING = r'"[a-zA-Z0-9!@#$%^&*()]*"'
    COMMA = r'\,'
    COLON = r'\:'
    SEMICOLON = r'\;'
    LEFT_PAR= r'\('
    RIGHT_PAR = r'\)'
    LEFT_CURVBR = r'\{'
    RIGHT_CURVBR = r'\}'
    LESS = r'\<'
    GREATER = r'\>'
    DIFFERENT = r'\<>'
    EQUAL = r'\='
    PLUS = r'\+'
    MINUS = r'\-'
    MULTIPLY = r'\*'
    DIVIDE = r'\/'
    IF = r'if'
    ELSE = r'else'
    PRINT = r'print'
    VAR = r'[a-z][a-zA-Z_0-9]*'
    ignore = r' \t'

# Functions revisaaar

 @_(r'\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def t_error(self, t):
        print('Line: %d: Not valid character: %r' % (self.lineno, t.value[0]))
        self.index += 1

# Test Lexer function
"""if __name__ == '__main__':
    data = '''
if else print + - * / gabo_125 Gabo 123 12.356
@
'''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)"""

# ***** PARSER *****

class CalcParser(Parser):
    tokens = CalcLexer.tokens
    def __init__(self):
        self.names = { }
    
    # graficaaaaas
    @_('PROGRAM ID SEMICOLON programT')
    def program(self, p):
        return p

    @_('vars programF',
       'programF')
    def programT(self, p):
        return p

     @_(' ')
    def empty(self, p):
        return p

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('>> ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))


