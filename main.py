from Lexer import Lexer

lexer = Lexer()

# Ciclo principal del compilador


while True:
    # leemos la instruccion
    instruction = input('>>> ')
    lexer.LoadCode(instruction)
    # imprimimos todos los tokens
    state = lexer.LexicalAnalisys(lexer.Tokenize())
    print(state)
    pass


