from Lexer import Lexer
from RegExDefinitions import TokenConstrainedRegEx,TokenFinitRegEx
from TokensDefinition import KeywordToken,SimbolToken,OperatorToken,VariableToken,LiteralToken,Type
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,SIMBOL_VALUES,OPERATOR_VALUES
from Rules import LiteralBooleanRule,LiteralNumericRule,LiteralStringRule,NameVariableRule
from ExpressionDefinitions import NumberExpression,StringExpression,BooleanExpression
from VariableDefinitions import NumberVariable,StringVariable,BooleanVariable
from LiteralDefinitions import NumberLiteral,StringLiteral,BooleanLiteral
import GRAMATIC_DEFINITION
import GrammarParser as GP
from os import system


def FiltToken(token):
    return len(token.Text) > 0 and token.Text != ' '

#_____________________________LEXER___________________________________________________

# build automaton to recognice language

keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)

simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)

operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)

variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule()],VariableToken)

boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule()],LiteralToken,Type.Boolean)

numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule()],LiteralToken,Type.Number)

string_literal_token_recognizer = TokenConstrainedRegEx([LiteralStringRule()],LiteralToken,Type.String)

print('+++++++++++++++++++++ TokeniZING ++++++++++++++++++++++++++++++')

# save to priority dictionary

recognizers = {
    0: keyword_token_recognizer,
    1: simbol_token_recognizer,
    2: operator_token_recognizer,
    3: boolean_literal_token_recognizer,
    4: numeric_literal_token_recognizer,
    5: string_literal_token_recognizer,
    6: variable_token_recognizer
}

# start lexer with defined rules

lexer = Lexer(recognizers)

system("cls")

# load code
reader = open('TestCode.hk','r')
code = reader.read()
lexer.LoadCode(code)

# check for lexical errors
Error = False
my_list =[]
for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
    
    my_list = my_list.__add__(state.TokensSequence)
    
    if state.Error != None:
        
        Error =True
        print(state)
        
        break
    pass

<<<<<<< HEAD
# extraemos los tokens del codigo
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 849d64d (translator moved from GrammarParser)
# for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
#     print(state)
#     pass

<<<<<<< HEAD
for token in lexer.Tokenize():
    print(token,token.Type)
=======
for state in lexer.LexicalAnalisys(lexer.Tokenize(),FiltToken):
    print(state)
>>>>>>> cbcf627 (first commit)
    pass
=======
my_list= [token.Text  for token in lexer.Tokenize() if token.Text != ' ' and token.Text != '\n' and token.Text != ''  ]

print(my_list)
gd_token= GRAMATIC_DEFINITION.traslator(my_list)

print(gd_token)
>>>>>>> 849d64d (translator moved from GrammarParser)
=======
#__________________PARSER__________________________________________
# go to parse
if not Error:
    
    tokens = [str(token) for token in my_list if token.Text != '\n' and token.Text != ' ']
    
    my_list = tokens

    gd_token= GRAMATIC_DEFINITION.traslator(my_list)

<<<<<<< HEAD
    print(gd_token)
>>>>>>> 6f9c51e (gramar modified)

=======
    #print(gd_token)
>>>>>>> 8380a4e (grammar tokenikezed)

    gp = GP.GrammarParser(GRAMATIC_DEFINITION.gramar,gd_token)




#_________________________SEMANTIC CHEKING__________________________________

    # YOUR CODE GOES HERE
#_________________________CODE GENERATION__________________________________

    # YOUR CODE GOES HERE

#________________________END_____________________________________________