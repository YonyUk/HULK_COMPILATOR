from GrammarInterface import ProductionType,Grammar
from ExpressionDefinitions import NumberExpression
from VariableDefinitions import NumberVariable
from LiteralDefinitions import NumberLiteral
from EnumsTokensDefinition import TokenType,Operator,Simbol,SimbolType,OperatorType,Type

"""
Las definiciones de las gramaticas
"""

ArithmeticTerminals = [
    'n',
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

ArithmeticProductions = {
    'E' : ['E+T','E-T','T'],
    'T' : ['E*F','E/F','F'],
    'F' : ['E^P','P'],
    'P' : ['E%P','Q'],
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

ArithMeticGrammar = Grammar(ArithmeticNonTerminals,ArithmeticTerminals,ArithmeticProductions,'E')