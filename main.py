from Lexer import Lexer

lexer = Lexer()

lexer.LoadCode('a = 123;')

for token in lexer.Tokenize():
    print(token)
    pass