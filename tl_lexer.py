import ply.lex as lex

keywords = (
    'Null',
    'function',
    'let',
    'List',
    'for',
    'if',
    'else',
    'while',
    'in',
    'of',
    'Number',
    'return'
)

tokens = keywords + (
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'MOD',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COLON',
    'Q_MARK',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'ASSIGN',
    'GT',
    'LD',
    'GTE',
    'LTE',
    'NEQUAL',
    'LOR',
    'LAND',
    'NOT',
    'RETTYPE',
    'ID',
    'COMMA',
    'NUMBER'
)

# A string containing ignored characters (spaces and tabs)
t_ignore = '\t '

t_EQUAL = r'\=='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_MOD = r'\%'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_Q_MARK = r'\?'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ASSIGN = r'\='
t_GT = r'\>'
t_LD = r'\<'
t_GTE = r'\>='
t_LTE = r'\<='
t_NEQUAL = r'\!='
# t_LOR = r'\||'
t_LAND = r'\&&'
t_NOT = r'\!'
t_RETTYPE = r'\=>'
t_COMMA = r','


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t


def t_NUMBER(t):
    r'\d+'
    # r'[0-9]+'
    t.value = int(t.value)

    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'//[^\n]\n'
    pass


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer1 = lex.lex(debug=0)
