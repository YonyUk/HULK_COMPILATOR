from RegExDefinitions import TokenFinitRegEx,TokenConstrainedRegEx,IRegEx
from TokensDefinition import KeywordToken,OperatorToken,SimbolToken,VariableToken,LiteralToken,EndToken
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,OPERATOR_VALUES,SIMBOL_VALUES
from EnumsTokensDefinition import Type
from Rules import *

class Lexer(IRegEx):
    
    def __init__(self):
        self._keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)
        self._simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)
        self._operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)
        self._variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule],VariableToken)
        self._boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule],LiteralToken,Type.Boolean)
        self._numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule],LiteralToken,Type.Number)
        self._string_literal_token_recognizer = TokenConstrainedRegEx([],LiteralToken,Type.String)
        pass
    
    pass