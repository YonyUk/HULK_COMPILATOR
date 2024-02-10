from ExpressionDefinitions import NumberExpression

class ILiteral:
    
    @property
    def Value(self):
        """
        devuelve el valor del literal que representa
        """
        raise NotImplementedError()
    
    pass

class NumberLiteral(ILiteral,NumberExpression):
    
    def __init__(self,value):
        self._value = value
        pass
    
    @property
    def Value(self):
        return self._value
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self._value)
    
    pass