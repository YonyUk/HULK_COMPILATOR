class IExpressionParser:
    
    def Parse(self,tokens):
        """
        Parse() -> Expression
        parsea una cadena de tokens
        """
        raise NotImplementedError()
    
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 849d64d (translator moved from GrammarParser)
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
    
<<<<<<< HEAD
=======
>>>>>>> cbcf627 (first commit)
=======
>>>>>>> 849d64d (translator moved from GrammarParser)
    pass