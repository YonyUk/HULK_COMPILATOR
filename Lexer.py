from RegExDefinitions import TokenFinitRegEx,TokenConstrainedRegEx,IRegEx,State
from TokensDefinition import KeywordToken,OperatorToken,SimbolToken,VariableToken,LiteralToken,EndToken
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,OPERATOR_VALUES,SIMBOL_VALUES
from EnumsTokensDefinition import Type
from Rules import LiteralBooleanRule,LiteralNumericRule,LiteralStringRule,NameVariableRule
from copy import copy

class Lexer(IRegEx):
    """
    automata que reconoce todas las cadenas que pertenecen al lenguaje definido
    """
    
    def __init__(self):
        # creamos cada uno de los automatas correspondientes a los diferentes tipos de token
        self._keyword_token_recognizer = TokenFinitRegEx(KEYWORD_VALUES,KeywordToken)
        self._simbol_token_recognizer = TokenFinitRegEx(SIMBOL_VALUES,SimbolToken)
        self._operator_token_recognizer = TokenFinitRegEx(OPERATOR_VALUES,OperatorToken)
        self._variable_token_recognizer = TokenConstrainedRegEx([NameVariableRule()],VariableToken)
        self._boolean_literal_token_recognizer = TokenConstrainedRegEx([LiteralBooleanRule()],LiteralToken,Type.Boolean)
        self._numeric_literal_token_recognizer = TokenConstrainedRegEx([LiteralNumericRule()],LiteralToken,Type.Number)
        self._string_literal_token_recognizer = TokenConstrainedRegEx([LiteralStringRule()],LiteralToken,Type.String)
        # los guardamos en una lista
        self._recognizers = [
            self._keyword_token_recognizer,
            self._simbol_token_recognizer,
            self._operator_token_recognizer,
            self._variable_token_recognizer,
            self._boolean_literal_token_recognizer,
            self._numeric_literal_token_recognizer,
            self._string_literal_token_recognizer   
        ]
        # establecemos las variables de control
        self._text_readed = ''
        self._match = False
        self._state = State.START
        self._last_state = State.START
        self._reading_string = False
        self.Code = ''
        self._error = None
        pass

    @property
    def Error(self):
        return self._error
    
    @property
    def Expression(self):
        return self._text_readed
    
    @property
    def Match(self):
        return self._match
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
        return self._last_state
    
    @property
    def Token(self): 
        
        if self._operator_token_recognizer.LastState == State.FINAL:
            return self._operator_token_recognizer.Token
        if self._simbol_token_recognizer.LastState == State.FINAL:
            return self._simbol_token_recognizer.Token
        if self._keyword_token_recognizer.LastState == State.FINAL:
            return self._keyword_token_recognizer.Token
        if self._variable_token_recognizer.LastState == State.FINAL:
            return self._variable_token_recognizer.Token
        if self._boolean_literal_token_recognizer.LastState == State.FINAL:
            return self._boolean_literal_token_recognizer.Token
        if self._numeric_literal_token_recognizer.LastState == State.FINAL:
            return self._numeric_literal_token_recognizer.Token
        return self._string_literal_token_recognizer.Token
    
    def LoadCode(self,code):
        self.Code = code
        pass
    
    def Restart(self):
        self._text_readed = ''
        self._match = False
        self._state = State.START
        self._last_state = State.START
        for recognizer in self._recognizers:
            recognizer.Restart()
            pass
        pass
    
    def Forward(self,character):
        self._last_state = copy(self.State)
            
        # intentamos reconocer la cadena de alguna forma
        forward = False
        
        for recognizer in self._recognizers:
            
            if not self._reading_string and recognizer == self._string_literal_token_recognizer:
                continue
        
            forward = recognizer.Forward(character) or forward
        
            if recognizer.State == State.FINAL:
                self._state = State.FINAL
                self._match = True
                pass
        
            pass
        
        if not forward:
            self._state = State.FAULT
            self._error = self._recognizers[len(self._recognizers) - 2].Error
            pass
        else:
            self._text_readed += character
            self._match = False
            if not self._state == State.FINAL:
                self._state = State.ONWORK
                pass
            pass
        
        return forward
    
    def Tokenize(self):
        # mientras que haya codigo que leer
        while len(self.Code) > 0:
            position = 0
            # mientras que alguno de los automatas haya tenido transicion
            while self.Forward(self.Code[position]):
                # quitamos el caracter leido
                position += 1
                pass
                
            # si estamos en un estado final
            if self.LastState == State.FINAL:
                # retornamos el token encontrado
                
                yield self.Token
                # comprabmos si estamos leyendo un string
                if self._text_readed == '"' and not self._reading_string:
                    self._reading_string = True
                    pass
                elif self._text_readed == '"':
                    self._reading_string = False
                    pass
                
                self.Restart()
                self.Code = self.Code[position:]
                
                pass

            if len(self.Code) - 1 < position:
                self._text_readed = self.Code
                self.Code = ''
                yield SimbolToken(self._text_readed)
                break
            
            pass
        
        pass
    
    pass