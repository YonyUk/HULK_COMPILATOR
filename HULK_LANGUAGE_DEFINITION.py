from EnumsTokensDefinition import TokenType,Simbol,Operator,Keyword

KEYWORD_VALUES = [
    'new',
    'print',
    'function',
    'let',
    'in',
    'protocol',
    'type',
    'while',
    'for',
    'if',
    'else',
    'elif',
    'cos',
    'sin',
    'tan',
    'log',
    'E',
    'PI',
    'exp',
    'sqrt',
    'rand',
    'range',
    'inherits'
]

KEYWORD_DICT = {
    'new' : Keyword.New,
    'print' : Keyword.Print,
    'function' : Keyword.Function,
    'let' : Keyword.Let,
    'in' : Keyword.In,
    'protocol' : Keyword.Protocol,
    'type' : Keyword.Type,
    'while' : Keyword.While,
    'for' : Keyword.For,
    'if' : Keyword.If,
    'else' : Keyword.Else,
    'elif' : Keyword.Elif,
    'cos' : Keyword.Cos,
    'sin' : Keyword.Sin,
    'tan' : Keyword.Tan,
    'log' : Keyword.Log,
    'E' : Keyword.Euler,
    'PI' : Keyword.PI,
    'exp' : Keyword.Exp,
    'sqrt' : Keyword.Sqrt,
    'rand' : Keyword.Rand,
    'range' : Keyword.Range,
    'inherits' : Keyword.Inherits
}

KEYWORD_FUNCTIONS = [
    'cos',
    'sin',
    'tan',
    'print',
    'exp',
    'sqrt',
    'rand',
    'range',
    'log'
]

KEYWORD_DECLARATORS = [
    'let',
    'in',
    'protocol',
    'type',
    'new'
]

KEYWORD_CONDITIONALS = [
    'if',
    'else',
    'elif'
]

KEYWORD_LOOPS = [
    'while',
    'for'
]

OPERATOR_VALUES = [
    '+',
    '-',
    '*',
    '/',
    '^',
    '%',
    '<',
    '>',
    '<=',
    '>=',
    '=',
    '==',
    '@',
    '++',
    '--',
    ':=',
    '!',
    '?',
    '&',
    '|',
    '~',
    'is',
    'as'
]

OPERATOR_DICT = {
    '+' : Operator.Plus,
    '-' : Operator.Minus,
    '*' : Operator.Mul,
    '/' : Operator.Div,
    '^' : Operator.Exp,
    '%' : Operator.Rest,
    '<' : Operator.LessThan,
    '>' : Operator.GreatherThan,
    '<=' : Operator.LessEqThan,
    '>=' : Operator.GreatherEqThan,
    '=' : Operator.Eq,
    '==' : Operator.DoubleEq,
    '@': Operator.Concat,
    '++' : Operator.PPlus,
    '--' : Operator.MMinus,
    ':=' : Operator.DoublePointEq,
    '!' : Operator.Distint,
    '?' : Operator.Ask,
    '&' : Operator.And,
    '|' : Operator.Or,
    '~' : Operator.Not,
    'is' : Operator.Is,
    'as' : Operator.As
}

OPERATOR_TEXTUALS = [
    'is',
    'as'
]

SIMBOL_VALUES = [
    "(",
    ")", 
    "{",
    "}",
    ".",
    "=>",
    "\"",
    " ",
    ";",
    ",",
    "\n",
    "self",
    ":"
]

SIMBOL_DICT = {
    "(" : Simbol.LeftP,
    ")" : Simbol.RightP, 
    "{" : Simbol.LeftB,
    "}" : Simbol.RightB,
    "." : Simbol.Point,
    "=>" : Simbol.RightArrow,
    "\"" : Simbol.DoubleCom,
    " " : Simbol.WhiteSpace,
    ";" : Simbol.PointCom,
    "," : Simbol.Com,
    "\n" : Simbol.JumpLine,
    "self" : Simbol.Self,
    ":" : Simbol.DoublePoint
}

SIMBOL_TEXTUALS = [
    'self'
]

TYPES_DEFINED = [
    'object',
    'number',
    'boolean',
    'string'
]