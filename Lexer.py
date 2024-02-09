from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,SIMBOL_TEXTUALS,OPERATOR_VALUES,OPERATOR_TEXTUALS,KEYWORD_VALUES
from TokensDefinition import OperatorToken,SimbolToken,KeywordToken,LiteralToken,VariableToken,EndToken
from Utils import isNumeric
from EnumsTokensDefinition import TokenType,Simbol
from ErrorsDefinition import LexicalError
from CodeStatesDefinition import CompilationStateERROR,CompilationStateOK
from Token import Token

class Lexer:
    
    def __init__(self):
        self.TextReaded = ''
        self.Code = ''
        self.CurrentPosition = 0
        pass
    
    def LoadCode(self,Code):
        
        self.Code = Code
        self.CurrentPosition = 1
        self.TextReaded = str(Code[0])
        pass
    
    def _IsSimbolSufix(self,text):
        
        for simbol in SIMBOL_VALUES:
            if simbol.endswith(text) and not len(simbol) == len(text):
                return True
            pass
        return False
    
    def _IsSimbolPrefix(self,text):
        
        for simbol in SIMBOL_VALUES:
            if simbol.startswith(text):
                return True
            pass
        return False
    
    def _IsTextualSimbolPrefix(self,text):
        
        for simbol in SIMBOL_TEXTUALS:
            if simbol.startswith(text):
                return True
            pass
        return False
    
    def _IsOperatorSufix(self,text):
        
        for operator in OPERATOR_VALUES:
            if operator.endswith(text) and not len(operator) == len(text):
                return True
            pass
        return False
    
    def _IsOperatorPrefix(self,text):
        
        for operator in OPERATOR_VALUES:
            if operator.startswith(text):
                return True
            pass
        return False
    
    def _IsTextualOperatorPrefix(self,text):
        
        for operator in OPERATOR_TEXTUALS:
            if operator.startswith(text):
                return True
            pass
        return False
    
    def _CreateToken(self,text):
        
        if OPERATOR_VALUES.__contains__(text):
            return OperatorToken(text)
        if SIMBOL_VALUES.__contains__(text):
            return SimbolToken(text)
        if KEYWORD_VALUES.__contains__(text):
            return KeywordToken(text)
        if text == 'true' or text == 'false' or isNumeric(text):
            return LiteralToken(text)
        return VariableToken(text)
    
    def Tokenize(self):
        
        while self.CurrentPosition < len(self.Code):
            
            if self.Code[self.CurrentPosition] == ' ':
                # lo que sea que se haya leido es un token
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                pass
            elif self.Code[self.CurrentPosition] == '.':
                # mismo caso anterios
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                pass
            elif self.TextReaded == " ":
                # estamos en presencia de un token
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                pass
            elif self.TextReaded == "\n":
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                pass
            elif self.Code[self.CurrentPosition] == "\n":
                # lo que sea que se haya leido es un token
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                yield self._CreateToken(self.TextReaded)
                self.TextReaded = str(self.Code[self.CurrentPosition])
                self.CurrentPosition += 1
                pass
            elif self.TextReaded == "\"":
                # nos hemos topado con la declaracion de un string
                # lo que sea que se haya leido es un token
                yield self._CreateToken(self.TextReaded)
                
                length = 0
                if self.Code.count("\"",self.CurrentPosition) > 0:
                    length = self.Code.index("\"",self.CurrentPosition) - self.CurrentPosition
                    pass
                
                if length == 0:
                    # lo que quedaba del codigo forma parte del string detectado
                    self.TextReaded = self.Code[self.CurrentPosition + 1]
                    yield LiteralToken(self.TextReaded)
                    yield EndToken("")
                    break
                
                # terminamos el procesamiento del string
                self.TextReaded = self.Code[self.CurrentPosition:self.CurrentPosition + length]
                yield LiteralToken(self.TextReaded)
                self.CurrentPosition += len(self.TextReaded)
                self.TextReaded = "\""
                yield self._CreateToken(self.TextReaded)
                self.CurrentPosition += 1
                
                if self.CurrentPosition == len(self.Code):
                    yield EndToken("")
                    break
                else:
                    self.TextReaded = str(self.Code[self.CurrentPosition])
                    self.CurrentPosition += 1
                    pass
                
                pass
            elif self._IsOperatorPrefix(self.TextReaded) and not self.TextReaded == 'a' and not self.TextReaded == 'i':
                # detectamos el prefijo de un operador
                
                if not self._IsOperatorSufix(str(self.Code[self.CurrentPosition])) and not self._IsSimbolSufix(str(self.Code[self.CurrentPosition])):
                    # si no es sufijo de ningun operador o simbolo
                    if not self._IsTextualOperatorPrefix(self.TextReaded):
                        # estamos en presencia de un operador
                        yield self._CreateToken(self.TextReaded)
                        self.TextReaded = str(self.Code[self.CurrentPosition])
                        self.CurrentPosition += 1
                        pass
                    else:
                        self.TextReaded += self.Code[self.CurrentPosition]
                        self.CurrentPosition += 1
                        pass
                    pass
                else:
                    self.TextReaded += self.Code[self.CurrentPosition]
                    self.CurrentPosition += 1
                    pass
                pass
            elif self._IsOperatorPrefix(self.Code[self.CurrentPosition]) and not self.Code[self.CurrentPosition] == 'a' and not self.Code[self.CurrentPosition] == 'i':
                
                if not self._IsTextualOperatorPrefix(self.Code[self.CurrentPosition]):
                    # lo que sea que se haya leido es un token
                    yield self._CreateToken(self.TextReaded)
                    self.TextReaded = str(self.Code[self.CurrentPosition])
                    self.CurrentPosition += 1
                    pass
                else:
                    self.TextReaded += self.Code[self.CurrentPosition]
                    self.CurrentPosition += 1
                    pass
                
                pass
            elif self._IsSimbolPrefix(self.TextReaded):
                # si el texto leido es prefijo de algun simbolo
                
                if not self._IsSimbolSufix(self.Code[self.CurrentPosition]):
                    # si el caracter actual no es sufijo de ningun simbolo
                    
                    if not self._IsTextualSimbolPrefix(self.TextReaded):
                        yield self._CreateToken(self.TextReaded)
                        self.TextReaded = str(self.Code[self.CurrentPosition])
                        self.CurrentPosition += 1
                        pass
                    else:
                        self.TextReaded += self.Code[self.CurrentPosition]
                        self.CurrentPosition += 1
                        pass
                    pass
                else:
                    self.TextReaded += self.Code[self.CurrentPosition]
                    self.CurrentPosition += 1
                    pass
                
                pass
            elif self._IsSimbolPrefix(self.Code[self.CurrentPosition]):
                # si es prefijo de algun simbolo
                
                if not self._IsTextualSimbolPrefix(self.Code[self.CurrentPosition]):
                    #  lo que sea que se haya leido es un token
                    
                    yield self._CreateToken(self.TextReaded)
                    self.TextReaded = str(self.Code[self.CurrentPosition])
                    self.CurrentPosition += 1
                    pass
                else:
                    self.TextReaded += self.Code[self.CurrentPosition]
                    self.CurrentPosition += 1
                    pass
                    
                pass
            else:
                self.TextReaded += self.Code[self.CurrentPosition]
                self.CurrentPosition += 1
                pass
            
            pass
        yield self._CreateToken(self.TextReaded)
        yield EndToken("")
        
        pass
    
    def TokenizeFiltered(self,filter):
        for token in self.Tokenize():
            if filter(token):
                yield token
                pass
            pass
        pass

    def LexicalAnalisys(self,tokens_sequence):
        
        column = 0
        line = 0
        
        for token in tokens_sequence:
            if token.Type == TokenType.Variable:
                if not str(str(token)[0]).isalpha():
                    error = LexicalError('El nombre de una variable debe comenzar con una letra',column,line)
                    return CompilationStateERROR(error)
                pass
            elif token.Type == TokenType.Simbol:
                if token.Simbol == Simbol.JumpLine:
                    line += 1
                    column = 0
                    pass
                pass
            column += token.Length
            pass
        
        return CompilationStateOK()
    
    pass
