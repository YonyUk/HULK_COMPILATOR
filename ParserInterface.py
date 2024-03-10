class IExpressionParser:
    
    def Parse(self,tokens):
        """
        Parse() -> Expression
        parsea una cadena de tokens
        """
        raise NotImplementedError()
    
<<<<<<< HEAD
    pass

class IShiftReduceParser(IExpressionParser):
    
    def Shift(self):
        """
        se desplaza en la cadena
        """
        raise NotImplementedError()
    
    def Reduce(self):
        """
        reduce el token actual
        """
        raise NotImplementedError()
    
=======
>>>>>>> cbcf627 (first commit)
    pass