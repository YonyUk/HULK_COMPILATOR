from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,OPERATOR_VALUES
<<<<<<< HEAD
import re
=======
>>>>>>> cbcf627 (first commit)

class Rule:
    """
    clase que define a una regla
    """
    
    def __init__(self,function):
        """
        function() -> bool
        """
        self._function = function
        pass
    
    @property
    def Description(self):
        """
        descripcion de la regla
        """
        
        raise NotImplementedError()
    
    def Try(self,value):
<<<<<<< HEAD
        """
        retorna True si cumple parcialmente la regla
        """
        
        return self._function(value)
    
    def Final(self,value):
        """
        retorna True si es cumple completamente la regla
        """
        
        raise NotImplementedError()
=======
        return self._function(value)
>>>>>>> cbcf627 (first commit)
        
    pass

def BooleanRule(value):
<<<<<<< HEAD
    return 'true'.startswith(value) or 'false'.startswith(value) or value == 'true' or value == 'false'
=======
    return value == 'true' or value == 'false'
>>>>>>> cbcf627 (first commit)

def VariableRule(name):
    
    if name[0].isnumeric():
        return False
    
    if not name.isalnum():
        for simbol in SIMBOL_VALUES:
            if len(simbol) == 1 and name.count(simbol) > 0:
                return False
            pass
        for operator in OPERATOR_VALUES:
            if len(operator) == 1 and name.count(operator) > 0:
                return False
            pass
        return True
    
    return True

def NumericRule(number):
<<<<<<< HEAD
    
    if len(number) == 0:
        return False
    
    if number.count('-') > 1 or number.count('+') > 1: return False
    
    if number.startswith('+') or number.startswith('-'): return False
    
    if number.count('+') == 1 or number.count('-') == 1: return number.count('e') == 1
    
    if number.count('.') > 1: return False
    
    if number.count('e') > 1: return False
    
    ignore = ['e','+','-','.']
    n = ''
    
    for char in number:
        if ignore.count(char) == 0:
            n += char
            pass
        pass
    
    if not n.isnumeric(): return False
    
    return True
=======
    if len(number) == 0:
        return False

    if number[0] == '-' or number[0] == '+':
        return NumericRule(number[1:])
    
    if number[0] == '0':
        if len(number) == 1:
            return True
        return len(number) > 2 and number[1] == '.' and number[2:].isnumeric()
    
    if number.count('.') > 0:
        
        parts = number.split('.')
        
        if len(parts) > 2:
            return False
        return parts[0].isnumeric() and parts[1].isnumeric() 
    
    if number.count('e') == 1:
        
        parts = number.split('e')
        
        if len(parts) > 2:
            return False
        if parts[1].startswith('+') or parts[1].startswith('-'):
            return parts[1][1:].isnumeric() and parts[0].isnumeric()
        return False
    
    return number.isnumeric()
>>>>>>> cbcf627 (first commit)

def StringRule(string):
    return string.count('"') == 0

class LiteralStringRule(Rule):
    
    def __init__(self):
        super().__init__(StringRule)
        pass
    
    @property
    def Description(self):
        return 'Las cadenas de texto no pueden contener el caracter \'"\''
    
<<<<<<< HEAD
    def Final(self,value):
        return True
    
=======
>>>>>>> cbcf627 (first commit)
    pass

class LiteralBooleanRule(Rule):
    
    def __init__(self):
        super().__init__(BooleanRule)
        pass
    
    @property
    def Description(self):
        return 'Los valores solo pueden ser \'true\' o \'false\''
    
<<<<<<< HEAD
    def Final(self,value):
        return value == 'false' or value == 'true'
    
=======
>>>>>>> cbcf627 (first commit)
    pass

class NameVariableRule(Rule):
    
    def __init__(self):
        super().__init__(VariableRule)
        pass
    
    @property
    def Description(self):
        return 'Los nombres de variables deben comenzar con una letra y no pueden contener operadores o simbolos reservados por el lenguaje'
    
<<<<<<< HEAD
    def Final(self,value):
        return True
    
=======
>>>>>>> cbcf627 (first commit)
    pass

class LiteralNumericRule(Rule):
    
    def __init__(self):
        super().__init__(NumericRule)
<<<<<<< HEAD
        
        self._ex1 = '[1-9_][0-9_]*'
        self._ex2 = '[0-9_]*[.][0-9_]*[1-9_]'
        self._ex3 = '[1-9_][0-9_]*e[+,-][1-9_][0-9_]*'
        
=======
>>>>>>> cbcf627 (first commit)
        pass
    
    @property
    def Description(self):
        return 'Los numeros solo deben seguir estas reglas: [1-9][0-9]...[1-9].[0-9]...[0-9] ; 0.[0-9]...[0-9] o [1-9][0-9]...[1-9]e< + o - >[1-9][0-9]...[1-9]'
    
<<<<<<< HEAD
    
    def Final(self,value):
        
        if len(value) == 1 and value.isnumeric():
            return True
        
        t1 = re.findall(self._ex1,value)
        if not len(t1) == 1:
            
            t1 = re.findall(self._ex2,value)
            
            if not len(t1) == 1:
                
                return len(re.findall(self._ex3,value)) == 1
        
            return True
        
        return True
    
=======
>>>>>>> cbcf627 (first commit)
    pass