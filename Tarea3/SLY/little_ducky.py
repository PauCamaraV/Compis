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
    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    @_(r'\d+\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Unvalid character %r at line: %d:' % (self.lineno, t.value[0]))
        self.index += 1
   
# ***** PARSER *****

class CalcParser(Parser):
    tokens = CalcLexer.tokens
    index = 1

    def __init__(self):
        self.names = { }
    
 # Program   
    @_('PROGRAM ID SEMICOLON programA')
    def program(self, p):
        self.index += 1

    @_('vars bloque empty',
       'bloque empty')
    def programA(self, p):
        return p

# Vars
    @_('VAR varsA')
    def vars(self, p):
        return p

    @_('ID COMMA varsA',
       'ID COLON tipo SEMICOLON empty',
       'ID COLON tipo SEMICOLON varsA empty')
    def varsA(self, p):
        return p

# Tipo
    @_('INT empty',
       'FLOAT empty')
    def tipo(self, p):
        return p

# Bloque
    @_('LEFT_CURVBR bloqueA',
       'LEFT_CURVBR RIGHT_CURVBR empty')
    def bloque(self, p):
        return p

    @_('estatuto RIGHT_CURVBR empty',
       'estatuto bloqueA')
    def bloqueA(self, p):
        return p

# Estatuto
    @_('asignacion empty',
       'condicion empty',
       'escritura empty')
    def estatuto(self, p):
        return p

# asignacion
    @_('ID EQUAL expresion SEMICOLON empty')
    def asignacion(self, p):
        return p

# Condicion
    @_('IF LEFT_PAR expresion RIGHT_PAR bloque condicionA')
    def condicion(self, p):
        return p

    @_('ELSE bloque SEMICOLON empty',
       'SEMICOLON empty')
    def condicionA(self, p):
        return p

# Escritura
    @_('PRINT LEFT_PAR escrituraA')
    def escritura(self, p):
        return p

    @_('expresion escrituraB',
       'STRING escrituraB')
    def escrituraA(self, p):
        return p
    
    @_('COMMA  escrituraA',
       'RIGHT_PAR SEMICOLON empty')
    def escrituraB(self, p):
        return p

# Expresion
    @_('exp expresionA')
    def expresion(self, p):
        return p

    @_('LESS exp empty',
       'GREATER exp empty',
       'DIFFERENT exp empty',
       'empty')
    def expresionA(self, p):
        return p

# Exp
    @_('termino expA')
    def exp(self, p):
        return p

    @_('PLUS exp empty',
       'MINUS exp empty',
       'empty')
    def expA(self, p):
        return p

# Termino
    @_('factor terminoA')
    def termino(self, p):
        return p

    @_('MULTIPLY exp empty',
       'DIVIDE exp empty',
       'empty')
    def terminoA(self, p):
        return p

# Factor
    @_('LEFT_PAR expresion RIGHT_PAR empty',
       'factorA')
    def factor(self, p):
        return p

    @_('PLUS varcte empty',
       'MINUS varcte empty',
       'varcte empty')
    def factorA(self, p):
        return p

# Varcte
    @_('ID empty',
       'INT empty',
       'FLOAT empty')
    def varcte(self, p):
        return p

# Empty
    @_(' ')
    def empty(self, p):
        return p

    def error(self, p):
        #if p:
        print("Syntax Error!! Line: %d" % (self.index))
        self.index += 1
        self.tokens
      #  else:
       #     print("Syntax Error!! EOF")


if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('Insert test doc (.txt): ')
            f = open(text, "r")
            for s in f:
                parser.parse(lexer.tokenize(s))    
        except EOFError:
            print('Error!!')


