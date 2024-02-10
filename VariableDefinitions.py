from ExpressionInterfaces import IExpression,Expression
from ExpressionDefinitions import NumberExpression

class UnassignatedVariableException(Exception):
    
    def __init__(self,message):
        self._message = message
        super().__init__(message)
        pass
    
    pass

class IVariable:
    
    @property
    def Name(self):
        """
        devuelve el nombre de la variable
        """
        raise NotImplementedError()
    
    @property
    def Value(self):
        """
        devuelve el valor de la variable
        """
        raise NotImplementedError()
    
    @property
    def IsAssignated(self):
        """
        devuelve si una variable ya ha sido asignada o no
        """
        raise NotImplementedError()
    
    def setValue(self):
        """
        cambia el valor de la variable
        """
        raise NotImplementedError()
    
    pass

class NumberVariable(IVariable,NumberExpression):
    
    def __init__(self,name,value=None):
        self._name = name
        if value == None:
            self._isassignated = False
            self._value = 0
            pass
        else:
            self._isassignated = True
            self._value = value
            pass
        pass
    
    @property
    def Name(self):
        return self._name
    
    @property
    def Value(self):
        if not self._isassignated:
            raise UnassignatedVariableException('No se ha asignado un valor a esta variable')
        return self._value
    
    def Resolve(self):
        pass
    
    def __str__(self):
        return str(self.Value)
    
    pass