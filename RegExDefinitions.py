from RegExInterface import State,IRegEx

class TokenFinitRegEx(IRegEx):
    """
    clase que reconoce tokens que pertenezcan a un conjunto finito
    """

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

class TokenConstrainedRegEx(IRegEx):
    
    def __init__(self,constrains,token_creator,self_type=None):
        """
        constrains -> functions() => bool
        restricciones que debe cumplir el token
        token_creator -> constructor de la clase de token que reconocera
        """
        self._match = False
        self._state = State.START
        self._text_readed = ''
        self._constrains = constrains
        self._creator = token_creator
        self._self_type = self_type
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
        if self._self_type == None:
            return self._creator(self._text_readed)
        return self._creator(self._text_readed,self._self_type)
    
    def Forward(self,character):
        
        if len(character) == 0:
            return True
        
        for constrain in self._constrains:
            if not constrain(self._text_readed + character):
                self._match = False
                self._state = State.FAULT
                return False
            pass
                
        self._text_readed += character
        self._match = True
        self._state = State.FINAL
        return True
    
    pass