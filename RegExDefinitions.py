from RegExInterface import State,IRegEx
from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,KEYWORD_VALUES

class TokenRegEx(IRegEx):

    def __init__(self,valid_values,token_creator):
        """
        values -> list(str)
        valores admisibles
        token_creator -> Constructor de la clase que instanciara los tokens
        """
        self._match = False
        self._text_readed = ''
        self._state = State.START
        self._values = valid_values
        self._creator = token_creator
        pass
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._text_readed
    
    @property
    def State(self):
        return self._state
    
    @property
    def Token(self):
        return self._creator(self._text_readed)
    
    def Forward(self,character):
        
        if len(character) == 0:
            return True
        
        for value in self._values:
            if value.startswith(self._text_readed + character):
                self._text_readed += character
                if len(value) == len(self._text_readed):
                    self._state = State.FINAL
                    self._match = True
                    pass
                else:
                    self._state = State.ONWORK
                    self._match = False
                    pass
                return True
            pass
        self._match = False
        self._state = State.FAULT
        return False
    
    pass