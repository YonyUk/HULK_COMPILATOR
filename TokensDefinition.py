from Token import Token
from Utils import isNumeric
from TokenInterfaces import IKeywordToken,ILiteralToken,ISimbolToken,IOperatorToken,IVariableToken
from EnumsTokensDefinition import Operator,Simbol,Keyword,KeywordType,Type,OperatorType,TokenType,SimbolType
from HULK_LANGUAGE_DEFINITION import KEYWORD_CONDITIONALS,KEYWORD_DECLARATORS,KEYWORD_FUNCTIONS,KEYWORD_LOOPS,KEYWORD_VALUES,KEYWORD_DICT,OPERATOR_DICT,SIMBOL_DICT

class KeywordToken(Token,IKeywordToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo de token que representa
        """
        
        return TokenType.Keyword
    
    @property
    def Keyword(self):
        """
        Keyword() -> Keyword
        devuelve la palabra reservada que representa
        """
        
        if KEYWORD_DICT.keys().__contains__(self.Text):
            return KEYWORD_DICT[self.Text]
        return Keyword.NONE
    
    @property
    def KeywordType(self):
        """
        KeywordType() -> KeywordType
        devuelve el tipo de palabra reservada que representa
        """
        
        if KEYWORD_FUNCTIONS.__contains__(self.Text):
            return KeywordType.Function
        if KEYWORD_DECLARATORS.__contains__(self.Text):
            return KeywordType.Declarator
        if KEYWORD_CONDITIONALS.__contains__(self.Text):
            return KeywordType.Conditional
        if KEYWORD_LOOPS.__contains__(self.Text):
            return KeywordType.Loop
        return KeywordType.Const
        
    pass

class LiteralToken(Token,ILiteralToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> Type
        devuelve el tipo de token que representa
        """
        
        return TokenType.Literal
    
    @property
    def SelfType(self):
        """
        SelfType() -> Type
        devuelve el tipo del valor del token que representa
        """
        
        if self.Text == 'true' or self.Text == 'false':
            return Type.Boolean
        if self.Text.isnumeric() or isNumeric(self.Text):
            return Type.Number
        return Type.String
    
    pass

class OperatorToken(Token,IOperatorToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo de token que representa
        """
        
        return TokenType.Operator
    
    @property
    def Operator(self):
        """
        Operator() -> Operator
        devuelve el operador que representa
        """
        
        if OPERATOR_DICT.keys().__contains__(self.Text):
            return OPERATOR_DICT[self.Text]
        return Operator.NONE
    
    @property
    def OperatorType(self):
        """
        OperatorType() -> OperatorType
        devuelve el tipo de operador que representa
        """
        
        if self.Text == '++' or self.Text == '--' or self.Text == '!':
            return OperatorType.Unary
        if self.Text == '?':
            return OperatorType.Ternary
        return OperatorType.Binary
    
    pass

class SimbolToken(Token,ISimbolToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo del token que representa
        """
        
        return TokenType.Simbol
    
    @property
    def Simbol(self):
        """
        Simbol() -> Simbol
        devuelve el simbolo que representa
        """
        
        if SIMBOL_DICT.keys().__contains__(self.Text):
            return SIMBOL_DICT[self.Text]
        return Simbol.NONE
    
    @property
    def SimbolType(self):
        """
        SimbolType() -> SimbolType
        devuelve el tipo de simbolo que representa
        """
        
        if self.Text == "(" or self.Text == ")" or self.Text == "{" or self.Text == "}":
            return SimbolType.Agrupator
        if self.Text == "." or self.Text == "self":
            return SimbolType.Accesor
        if self.Text == "=>" or self.Text == "\"" or self.Text == ":":
            return SimbolType.Declarator
        return SimbolType.Separator
    
    pass

class VariableToken(Token,IVariableToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Type(self):
        """
        Type() -> TokenType
        devuelve el tipo del token que representa
        """
        
        return TokenType.Variable
    
    @property
    def Name(self):
        """
        Name() -> string
        devuelve el nombre de la variable que representa
        """

        return self.Text
    
    pass

class EndToken(SimbolToken):
    
    def __init__(self,Text):
        super().__init__(Text)
        pass
    
    @property
    def Simbol(self):
        return Simbol.End
    
    @property
    def SimbolType(self):
        return SimbolType.Separator
    
    pass