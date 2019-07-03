import ply.lex as lex

tokens = (
    'FLOAT',
    'INT',
    'STRING',
    'BOOL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'VAR',
    'EOS',
)

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_EQUALS(t):
    r'\='
    return t

def t_EOS(t):
    r'\;'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = str(t.value)[1:-1] # removes first and last speech marks
    return t

def t_BOOL(t):
    r'true|false|nil'
    if t.value == "true":
        value = True
    elif t.value == "false":
        value = False
    else:
        value = None
    t.value = value
    return t

def t_VAR(t):
    r'([a-zA-Z_][a-zA-Z0-9_]*)'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def group(expressions):
    out = []
    temp = []
    for expr in expressions:
        if expr.type != "EOS":
            temp.append(expr)
        else:
            out.append(temp)
            temp = []

    out.append(temp)

    return out

def lexify(string):
    lexer.input(string)
    expressions = list(iter(lexer.token, None))
    return group(expressions)

lexer = lex.lex()