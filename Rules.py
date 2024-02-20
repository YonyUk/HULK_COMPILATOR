from HULK_LANGUAGE_DEFINITION import SIMBOL_VALUES,OPERATOR_VALUES

def LiteralBooleanRule(value):
    return value == 'true' or value == 'false'

def NameVariableRule(name):
    
    if name[0].isnumeric:
        return False
    
    if not name.isalnum:
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

def LiteralNumericRule(number):

    if number[0] == '-' or number[0] == '+':
        return LiteralNumericRule(number[1:])
    
    if number[0] == '0':
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