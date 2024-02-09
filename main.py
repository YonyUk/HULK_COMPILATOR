from Lexer import Lexer

lexer = Lexer()

# Ciclo principal del compilador


while True:
    # leemos la instruccion
    instruction = input('>>> ')
    lexer.LoadCode(instruction)
    # imprimimos todos los tokens
    for token in lexer.Tokenize():
        print(f'{token} ----> {token.Type}')
        pass
    pass


