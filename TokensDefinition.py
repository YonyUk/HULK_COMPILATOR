from Token import Token
from Utils import isNumeric
from TokenInterfaces import IKeywordToken,ILiteralToken,ISimbolToken,IOperatorToken,IVariableToken
from EnumsTokensDefinition import Keyword,KeywordType,Type,Operator,OperatorType,TokenType,Simbol,SimbolType
from HULK_LANGUAGE_DEFINITION import KEYWORD_CONDITIONALS,KEYWORD_DECLARATORS,KEYWORD_FUNCTIONS,KEYWORD_LOOPS,KEYWORD_VALUES

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
        
        if self.Text == 'print':
            return Keyword.Print
        if self.Text == 'function':
            return Keyword.Function
        if self.Text == 'let':
            return Keyword.Let
        if self.Text == 'in':
            return Keyword.In
        if self.Text == 'protocol':
            return Keyword.Protocol
        if self.Text == 'type':
            return Keyword.Type
        if self.Text == 'new':
            return Keyword.New
        if self.Text == 'if':
            return Keyword.If
        if self.Text == 'else':
            return Keyword.Else
        if self.Text == 'if':
            return Keyword.Elif
        if self.Text == 'while':
            return Keyword.While
        if self.Text == 'for':
            return Keyword.For
        if self.Text == 'cos':
            return Keyword.Cos
        if self.Text == 'sin':
            return Keyword.Sin
        if self.Text == 'tan':
            return Keyword.Tan
        if self.Text == 'exp':
            return Keyword.Exp
        if self.Text == 'sqrt':
            return Keyword.Sqrt
        if self.Text == 'rand':
            return Keyword.Rand
        if self.Text == 'range':
            return Keyword.Range
        if self.Text == 'E':
            return Keyword.Euler
        if self.Text == 'PI':
            return Keyword.PI
        if self.Text == 'log':
            return Keyword.Log
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
        
        if self.Text == '+':
            return Operator.Plus
        if self.Text == '++':
            return Operator.PPlus
        if self.Text == '-':
            return Operator.Minus
        if self.Text == '--':
            return Operator.MMinus
        if self.Text == '*':
            return Operator.Mul
        if self.Text == '/':
            return Operator.Div
        if self.Text == '^':
            return Operator.Exp
        if self.Text == '%':
            return Operator.Rest
        if self.Text == '<':
            return Operator.LessThan
        if self.Text == '>':
            return Operator.GreatherThan
        if self.Text == '<=':
            return Operator.LessEqThan
        if self.Text == '>=':
            return Operator.GreatherEqThan
        if self.Text == '=':
            return Operator.Eq
        if self.Text == '==':
            return Operator.DoubleEq
        if self.Text == '!=':
            return Operator.Distint
        if self.Text == ':=':
            return Operator.DoublePointEq
        if self.Text == '&':
            return Operator.And
        if self.Text == '|':
            return Operator.Or
        if self.Text == '!':
            return Operator.Not
        if self.Text == '@':
            return Operator.Concat
        if self.Text == 'is':
            return Operator.Is
        if self.Text == 'as':
            return Operator.As
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
        
        if self.Text == "(":
            return Simbol.LeftP
        if self.Text == ")":
            return Simbol.RightP
        if self.Text == "{":
            return Simbol.LeftB
        if self.Text == "}":
            return Simbol.RightB
        if self.Text == ".":
            return Simbol.Point
        if self.Text == ":":
            return Simbol.DoublePoint
        if self.Text == ",":
            return Simbol.Com
        if self.Text == "":
            return Simbol.PointCom
        if self.Text == "=>":
            return Simbol.RightArrow
        if self.Text == "\"":
            return Simbol.DoubleCom
        if self.Text == " ":
            return Simbol.WhiteSpace
        if self.Text == "\n":
            return Simbol.JumpLine
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
        super.__init__(Text)
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