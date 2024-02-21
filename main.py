from Lexer import Lexer

lexer = Lexer()

reader = open('TestCode.hk','r')
code = reader.read()
lexer.LoadCode(code)

for token in lexer.Tokenize():
    print(token,token.Type)
    pass