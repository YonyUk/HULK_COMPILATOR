from Lexer import Lexer
from Parser import NumberExpression,NumberLiteral,NumberVariable,BooleanExpression,BooleanLiteral,BooleanVariable,StringExpression,StringVariable,StringLiteral
from TokensDefinition import OperatorToken
from EnumsTokensDefinition import Simbol,TokenType

def Filter(token):
    if token.Type == TokenType.Simbol:
        return not token.Simbol == Simbol.WhiteSpace
    return True

lexer = Lexer()

reader = open('TestCode.hk','r')
code  = reader.read()
lexer.LoadCode(code)

for state in lexer.LexicalAnalisysFiltered(lexer.Tokenize(),Filter):

    if not state.Error == None:
        print(state)
        break

    secuence = ''
    for token in state.TokensSequence:
        secuence += 'token:' + str(token[0]) + ' : ' + str(token[0].Type) + ' (' + str(token[1]) + ' ' + str(token[2]) + ') '
        pass

    print(secuence)
    print()
    pass