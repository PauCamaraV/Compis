# littleducky.py by Paulina Cámara (2021)
# Lexer and Parser program using ply

import ply.lex as lex
import ply.yacc as yacc
import sys

# ***** LEXER *****

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

t_COMMA = r'\,'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_LEFT_PAR= r'\('
t_RIGHT_PAR = r'\)'
t_LEFT_CURVBR = r'\{'
t_RIGHT_CURVBR = r'\}'
t_LESS = r'\<'
t_GREATER = r'\>'
t_DIFFERENT = r'\<>'
t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_ignore = r' \t'


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9!@#$%^&*()]*"'
    t.type = 'STRING'
    return t

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    t.type = 'ID'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t 

def t_VAR(t):
    r'[a-z][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t

def t_PRINT(t):
    r'print'
    t.type = 'PRINT'
    return t 

# Error variable 
def t_error(t):
    print('Unvalid character!!: %s' % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test Lexer function

def testLex():
    lexer.input("if ( Pau = pau) { print ( Patrol ) , aLi_12 } else c4M4r4 ")

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# ***** PARSER *****

def p_program(p):
    '''

    program :  PROGRAM ID SEMICOLON programA

    programA : vars bloque empty
            | bloque empty
    '''
    p[0] = None

def p_vars(p):
    '''

    vars : VAR varsA 

    varsA : ID COMMA varsA 
        | ID COLON tipo SEMICOLON empty
        | ID COLON tipo SEMICOLON varsA empty
    '''
    p[0] = None

def p_tipo(p):
    '''

    tipo : INT empty
        | FLOAT empty
    '''
    p[0] = None

def p_bloque(p):
    '''

    bloque : LEFT_CURVBR bloqueA
          | LEFT_CURVBR RIGHT_CURVBR empty

    bloqueA : estatuto RIGHT_CURVBR empty
            | estatuto bloqueA
    '''
    p[0] = None

def p_estatuto(p):
    '''

    estatuto : asignacion empty
            | condicion empty
            | escritura empty
    '''
    p[0] = None

def p_asignacion(p):
    '''

    asignacion : ID EQUAL expresion SEMICOLON empty
    '''
    p[0] = None

def p_condicion(p):
    '''

    condicion : IF LEFT_PAR expresion RIGHT_PAR bloque condicionA

    condicionA : ELSE bloque SEMICOLON empty
            | SEMICOLON empty
    '''
    p[0] = None

def p_escritura(p):
    '''

    escritura : PRINT LEFT_PAR escrituraA
    
    escrituraA : expresion escrituraB
               | STRING escrituraB

    escrituraB : COMMA  escrituraA
               | RIGHT_PAR SEMICOLON empty
    '''
    p[0] = None

def p_expresion(p):
    '''
    expresion : exp expresionA

    expresionA : LESS exp empty
            | GREATER exp empty
            | DIFFERENT exp empty
            | empty
    '''
    p[0] = None

def p_exp(p):
    '''

    exp : termino expA 

    expA : PLUS exp
        | MINUS exp
        | empty
    '''
    p[0] = None

def p_termino(p):
    '''

    termino : factor terminoA

    terminoA : MULTIPLY termino
            | DIVIDE termino
            | empty
    '''
    p[0] = None

def p_factor(p):
    '''

    factor : LEFT_PAR expresion RIGHT_PAR empty
            | factorA
    factorA : PLUS varcte empty
            | MINUS varcte empty
            | varcte empty
    '''
    p[0] = None

def p_varcte(p):
    '''

    varcte : ID empty
           | INT empty
           | FLOAT empty
    '''
    p[0] = None

def p_empty(p):
    '''

    empty : 
    '''
    p[0] = None

def p_error(p):
    print("Syntax Error!!")

parser = yacc.yacc()

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)






