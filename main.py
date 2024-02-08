from Lexer import Lexer

lexer = Lexer()

# Ciclo principal del compilador

lexer.LoadCode('let a = 10 in print(a);')
for token in lexer.Tokenize():
    print(f'{token} ----> {token.Type}')
    pass

# while True:
    #     # leemos la instruccion
#     print('\r')
#     instruction = input('>>> ')
#     lexer.LoadCode(instruction)
#     # imprimimos todos los tokens
#     pass


