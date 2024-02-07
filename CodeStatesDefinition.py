class State:
    
    def __init__(self,error):
        self._error = error
        pass
    
    @property
    def Error(self):
        return self._error
    
    def __str__(self):
        if self._error == None:
            return 'OK'
        return str(self._error)
    
    pass

class CompilationStateOK(State):
    
    def __init__(self):
        super().__init__(None)
        pass
    
    pass

class CompilationStateERROR(State):
    
    def __init__(self,error):
        super().__init__(error)
        pass
    
    pass