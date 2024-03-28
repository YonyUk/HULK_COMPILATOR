from GrammarInterface import ProductionType,Grammar
from ExpressionDefinitions import NumberExpression
from VariableDefinitions import NumberVariable
from LiteralDefinitions import NumberLiteral
from EnumsTokensDefinition import TokenType,Operator,Simbol,SimbolType,OperatorType,Type

"""
Las definiciones de las gramaticas
"""

# falta diferenciar entre las prioridades de la potencia y modulacion; y la multiplicacion y division

ArithmeticTerminals = [
    'n',
    'a',
    'p',
    '',
    '+',
    '-',
    '*',
    '/',
    '^',
    '%',
    '(',
    ')',
    '$'
]

ArithmeticNonTerminals = [
    'E',
    'T',
    'F',
    'P',
    'Q'
]

<<<<<<< HEAD
Priorities = {
    '(' : -1,
    ')' : 0,
    '+' : 0,
    '-' : 0,
    '%' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

ArithmeticProductions = {
    'E' : ['E+T','E-T','T'],
    'T' : ['T%F','F'],
    'F' : ['F*P','F/P','P'],
    'P' : ['P^Q','Q'],
=======
ArithmeticProductions = {
    'E' : ['E+T','E-T','T','a','(Ep'],
    'T' : ['E*F','E/F','E*T','E/T','F'],
    'F' : ['E^P','E^F','P'],
    'P' : ['E%Q','E%P','Q'],
>>>>>>> 849d64d (translator moved from GrammarParser)
    'Q' : ['(E)','n']
}

ArithmeticTranslator = {
    TokenType.Literal : 'n',
    Operator.Plus : '+',
    Operator.Minus : '-',
    Operator.Div : '/',
    Operator.Mul : '*',
    Operator.Exp : '^',
    Operator.Rest : '%',
    Simbol.LeftP : '(',
    Simbol.RightP : ')',
    TokenType.Variable : 'n'
}

<<<<<<< HEAD
ArithMeticGrammar = Grammar(
    ArithmeticNonTerminals,
    ArithmeticTerminals,
    ArithmeticProductions,
    'E',
    Priorities
)
=======
ArithMeticGrammar = Grammar(ArithmeticNonTerminals,ArithmeticTerminals,ArithmeticProductions,'E')
>>>>>>> 849d64d (translator moved from GrammarParser)
