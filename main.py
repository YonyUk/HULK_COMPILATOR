from Lexer import Lexer
from Parser import NumberExpression,NumberLiteral,NumberVariable,BooleanExpression,BooleanLiteral,BooleanVariable
from TokensDefinition import OperatorToken

a = BooleanLiteral(False)
b = BooleanVariable('yony',True)

c = BooleanExpression([a,b],[OperatorToken('|')])
print(c)