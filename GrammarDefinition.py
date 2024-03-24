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
    'X',
    'F',
    'Y',
    'P',
    'Z',
    'Q',
    'W'
]

ArithmeticProductions = {
    'E' : ['TX'],
    'X' : ['+TX','-TX',''],
    'T' : ['FY'],
    'Y' : ['*FY','/FY',''],
    'F' : ['PZ'],
    'Z' : ['^PZ',''],
    'P' : ['QW'],
    'W' : ['%QW',''],
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