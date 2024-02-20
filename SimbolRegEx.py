from RegExInterface import State,IRegEx
from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES

class RegEx(IRegEx):
    
    @property
    def Token(self):
        """
        devuelve el token asociado a la cadena consumida
        """
        
        raise NotImplementedError()
    
    pass

class SimbolRegEx(IRegEx):
    
    def __init__(self):
        self._state = State.START
        self._match = False
        self._text_readed = ''
        pass
    
    def Forward(self,character):
        
        self._text_readed += character
        for simbol in SIMBOL_VALUES:
            if simbol.startswith(self._text_readed):
                self._match = True
                if len(simbol) == self._text_readed:
                    self._state = State.FINAL
                    pass
                else:
                    self._state = State.ONWORK
                    pass
                return True
            pass
        self._match = False
        self._state = State.FAULT
        return False    
    
    pass