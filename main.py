from Lexer import Lexer

lexer = Lexer()

# Ciclo principal del compilador
reader = open('TestCode.hk','r')
code = reader.read()

lexer.LoadCode(code)
state = lexer.LexicalAnalisys(lexer.Tokenize())
print(state)

# while True:
#     # leemos la instruccion
#     instruction = input('>>> ')
#     lexer.LoadCode(instruction)
#     # imprimimos todos los tokens
#     state = lexer.LexicalAnalisys(lexer.Tokenize())
#     print(state)
#     pass


