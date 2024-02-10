from Lexer import Lexer
from Parser import NumberExpression,NumberLiteral,NumberVariable,BooleanExpression,BooleanLiteral,BooleanVariable,StringExpression,StringVariable,StringLiteral
from TokensDefinition import OperatorToken

a = StringLiteral('')
b = StringVariable('yony','h')
c = StringExpression([a,a,b],[OperatorToken('@'),OperatorToken('@')])
print(c)