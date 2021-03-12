# littleducky.py by Paulina Cámara (2021)
# Lexer and Parser program using ply
import ply.lex as lex
import ply.yacc as yacc
import sys

# ***** LEXER *****

# Tokens
tokens = [
    'PROGRAM',      #program
    'ID',           #id
    'SEMICOLON',     
    'COMMA',        
    'COLON',        
    'INT',          
    'FLOAT',        
    'STRING',       
    'LEFT_CURVBR',     
    'RIGHT_CURVBR',    
    'EQUAL',          
    'LESS',         
    'GREATER',      
    'DIFFERENT',         
    'LEFT_PAR',       
    'RIGHT_PAR',        
    'IF',           
    'ELSE',         
    'VAR',          
    'PRINT',        
    'PLUS',         
    'MINUS',        
    'MULTIPLY',         
    'DIVIDE'          
]

# Token definitions
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_COLON = r'\:'
t_LEFT_CURVBR = r'\{'
t_RIGHT_CURVBR = r'\}'
t_EQUAL = r'\='
t_DIFFERENT = r'\<\>'
t_LESS = r'\<'
t_GREATER = r'\>'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'

t_ignore = ' \t'

def t_PROGRAM(t):
    r'program'
    t.type = 'PROGRAM'
    return t

def t_IF(t):
    r'if'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'else'
    t.type = 'ELSE'
    return t 

def t_PRINT(t):
    r'print'
    t.type = 'PRINT'
    return t 

def t_VAR(t):
    r'[a-z][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t

def t_ID(t):
    r'[A-Z][a-zA-Z0-9]*'
    t.type = 'ID'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[a-zA-Z0-9!@#$%^&*()]*"'
    t.type = 'STRING'
    return t

# count lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Errores de lexer
def t_error(t):
    print('Line: %d, Not valid character: %r' % (t.lexer.lineno, t.value[0]))
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
    program  : PROGRAM ID SEMICOLON programA
    
    programA : vars programB
             | programB
    
    programB : bloque empty
    '''
    p[0] = None

def p_vars(p):
    '''
    vars  : VAR varsA
    
    varsA : ID COMMA varsA
          | ID COLON tipo SEMICOLON varsB
    
    varsB : varsA
          | empty
    '''
    p[0] = None

def p_tipo(p):
    '''
    tipo  : INT empty
          | FLOAT empty
    '''
    p[0] = None

def p_bloque(p):
    '''
    bloque  : LEFT_CURVBR bloqueA
    bloqueA : estatuto bloqueA
            | RIGHT_CURVBR empty
    '''
    p[0] = None

def p_estatuto(p):
    '''
    estatuto  : asignacion empty
              | condicion empty
              | escritura empty
    '''
    p[0] = None

def p_asignacion(p):
    '''
    asignacion  : ID EQUAL expresion SEMICOLON empty
    '''
    p[0] = None
    
def p_escritura(p):
    '''
    escritura  : PRINT LEFT_PAR escrituraA
    escrituraA : expresion escrituraB
               | STRING escrituraB
    escrituraB : COMMA  escrituraA
               | RIGHT_PAR SEMICOLON empty
    '''
    p[0] = None

def p_expresion(p):
    '''
    expresion  : exp expresionA
    expresionA : LESS exp empty
               | GREATER exp empty
               | DIFFERENT exp empty
               | empty
    '''
    p[0] = None

def p_condicion(p):
    '''
    condicion  : IF LEFT_PAR expresion RIGHT_PAR bloque condicionA
    condicionA : ELSE bloque empty
               | empty
    '''
    p[0] = None

def p_exp(p):
    '''
    exp  : termino expA
    expA : PLUS exp
         | MINUS exp
         | empty
    '''
    p[0] = None

def p_termino(p):
    '''
    termino  : factor terminoA
    terminoA : MULTIPLY termino
         | DIVIDE termino
         | empty
    '''
    p[0] = None

def p_factor(p):
    '''
    factor  : LEFT_PAR expresion RIGHT_PAR empty
            | factorA
    factorA : PLUS factorB
            | MINUS factorB
            | factorB
    factorB : varcte empty
    '''
    p[0] = None

def p_varcte(p):
    '''
    varcte  : ID empty
            | INT empty
            | FLOAT empty
    '''
    p[0] = None
#Funcion de manejo de errores
def p_error(p):
    print("Syntax error found at line %d." % (lexer.lineno))

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None

parser = yacc.yacc()

while True:
    try:
        text = input('Insert test doc (.txt): ')
        f = open(text, "r")
        lexer.lineno = 1
        for s in f:
            parser.parse(s)
    except EOFError:
        print('Error')






