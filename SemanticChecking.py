import HULK_LANGUAGE_DEFINITION as hulk
from EnumsTokensDefinition import Type,TokenType
from TokensDefinition import OperatorToken,SimbolToken,KeywordToken,VariableToken,LiteralToken
from DerivationTree import DerivationTree,ASTNode,NodeType
from EnumErrorTypes import ErrorType
from ErrorsDefinition import SemanticError

ARITMETIC_OPERATORS = [
    '+',
    '-',
    '*',
    '/',
    '^',
    '%',
    '>',
    '<',
    '<=',
    '>='
]

BOOLEAN_OPERATORS = [
    '&',
    '|',
    '!'
]

ASIGMENT_OPERATORS = [
    '++',
    '--',
    '-=',
    '*=',
    '/=',
    '%=',
    '+=',
    '^='
    '=',
    ':=',
    '|=',
    '&='
]

###################### SEMANTIC CHECKERS ########################

def AsigmentChecker(operator,childs,context):
    """
    checkea la semantica de una asignacion
    """
    
    if not len(childs) == 2: return False,None
    
    if not childs[0].ASTType == NodeType.Variable: return False, SemanticError(f'{childs[0].Value} no es una variable',None,None)

    if context['variables'].count(childs[0].Value) == 0: return False, SemanticError(f'la variable {childs[0].Value} no existe en este contexto',None,None)
    
    if context['types'][childs[0].Value] == int or context['types'][childs[0].Value] == float:
        if not childs[1].Type == int and not childs[1].Type == float:
            return False, SemanticError(f'no se puede asignar un valor de tipo {childs[1].Type} al tipo numerico', None,None)
        return True,None
    
    if not context['types'][childs[0].Value] == childs[1].Type:
        return False, SemanticError(f'no se puede asignar el tipo {childs[1].Type} al tipo {childs[0].Type}',None,None)

    return True,None

def AritmeticChecker(operator,childs,context):
    """
    checkea la semantica de un operador aritmetico
    """
    
    if len(childs) == 1:
        if childs[0].ASTType == NodeType.Variable:
            if context['variables'].count(childs[0].Value) == 0:
                return False,SemanticError(f'la variable {childs[0].Value} no existe en este contexto',None,None)
            if not context['types'][childs[0].Value] == int and not context['types'][childs[0].Value] == float:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable numerica',None,None)
            return True,None
        if not childs[0].Type == int and not childs[0].Type == float:
            return False,SemanticError(f'el operador {operator} solo se puede aplicar a valores numericos',None,None)
        return True,None
    
    if not len(childs) == 2:
        return False,SemanticError(f'el operador {operator} se aplica entre dos operandos',None,None)
    
    if childs[0].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[0].Value) == 0:
            return False, SemanticError(f'la variable {childs[0].Value} no existe en el contexto actual',None,None)
        
        if not context['types'][childs[0].Value] == int and not context['types'][childs[0].Value] == float:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable numerica',None,None)
        
        if childs[1].ASTType == NodeType.Variable:
            if context['variables'].count(childs[1].Value) == 0:
                return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
            
            if not context['types'][childs[1].Value] == int and not context['types'][childs[1].Value] == float:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable numerica',None,None)    

            return True,None
        
        if not childs[1].Type == int and not childs[1].Type == float:
            return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor numerico',None,None)    
            
        return True,None
    
    if not childs[0].Type == int and not childs[0].Type == float:
        return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor numerico',None,None)    
        
    if childs[1].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[1].Value) == 0:
            return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
        
        if not context['types'][childs[1].Value] == int and not context['types'][childs[1].Value] == float:
            return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable numerica',None,None)    
        
        return True,None
    
    if not childs[1].Type == int and not childs[1].Type == float:
        return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor numerico',None,None)

    return True,None

def BooleanChecker(operator,childs,context):
    """
    checkea la semantica de un operador booleano
    """
    
    if len(childs) == 1:
        if childs[0].ASTType == NodeType.Variable:
            if context['variables'].count(childs[0].Value) == 0:
                return False,SemanticError(f'la variable {childs[0].Value} no existe en este contexto',None,None)
            if not context['types'][childs[0].Value] == bool:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable booleana',None,None)
            return True,None
        if not childs[0].Type == bool:
            return False,SemanticError(f'el operador {operator} solo se puede aplicar a valores booleanos',None,None)
        return True,None
    
    if not len(childs) == 2:
        return False,SemanticError(f'el operador {operator} se aplica entre dos operandos',None,None)
    
    if childs[0].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[0].Value) == 0:
            return False, SemanticError(f'la variable {childs[0].Value} no existe en el contexto actual',None,None)
        
        if not context['types'][childs[0].Value] == bool:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable booleana',None,None)
        
        if childs[1].ASTType == NodeType.Variable:
            if context['variables'].count(childs[1].Value) == 0:
                return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
            
            if not context['types'][childs[1].Value] == bool:
                return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable booleana',None,None)    

            return True,None
        
        if not childs[1].Type == bool:
            return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor booleano',None,None)    
            
        return True,None
    
    if not childs[0].Type == bool:
        return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor booleano',None,None)    
        
    if childs[1].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[1].Value) == 0:
            return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
        
        if not context['types'][childs[1].Value] == bool and not context['types'][childs[1].Value] == bool:
            return False, SemanticError(f'el operador {operator} solo se puede aplicar a una variable booleana',None,None)    
        
        return True,None
    
    if not childs[1].Type == bool:
        return False, SemanticError(f'el operador {operator} solo se puede aplicar a una valor booleano',None,None)

    return True,None

def StringChecker(operator,childs,context):
    """
    comprueba la semantica del operador @
    """
    if not len(childs) == 2:
        return False,SemanticError(f'el operador {operator} se aplica entre dos operandos',None,None)
    
    if childs[0].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[0].Value) == 0:
            return False, SemanticError(f'la variable {childs[0].Value} no existe en el contexto actual',None,None)
        
        if childs[1].ASTType == NodeType.Variable:
            if context['variables'].count(childs[1].Value) == 0:
                return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
            
            return True,None
            
        return True,None
    
    if childs[1].ASTType == NodeType.Variable:
        
        if context['variables'].count(childs[1].Value) == 0:
            return False, SemanticError(f'la variable {childs[1].Value} no existe en el contexto actual',None,None)
                
        return True,None

    return True,None

def OperatorChecker(operator,childs,context):
    
    if ASIGMENT_OPERATORS.count(operator) > 0:
        return AsigmentChecker(operator,childs,context)
    if ARITMETIC_OPERATORS.count(operator) > 0:
        return AritmeticChecker(operator,childs,context)
    if BOOLEAN_OPERATORS.count(operator) > 0:
        return BooleanChecker(operator,childs,context)
    return StringChecker(operator,childs,context)    

################### OPERATOR RESOLVERS ##########################

def BinaryResolver(operator,childs,context):
    left = childs[0].Result[0]
    right = childs[1].Result[0]
    
    return hulk.OPERATOR_RESOLVERS[operator](left,right),None

def AsigmentResolver(operator,childs,context):
    left = childs[0]
    
    if len(childs) == 1:
        op1 = operator[1]
        context['values'][left.Value] = hulk.OPERATOR_RESOLVERS[op1](context['values'][left.Value],1)
        return None,None
    
    op = operator[0]
    
    right = childs[1].Result[0]
    
    if op == '=':
        context['values'][left.Value] = right
        pass
    else:
        context['values'][left.Value] = hulk.OPERATOR_RESOLVERS[op](context['values'][left.Value],right)
        pass
    return None,None

context = {
    'variables': [
        'b',
        'a'
    ],
    'types': {
        'b' : int,
        'a' : float
    },
    'values': {
        'a' : 10,
        'b' : 5
    }
}

print()
print()
print()
print()
print()
print()
print()
print()

a = ASTNode('a',Type=NodeType.Variable,Context=context,Resolver=lambda operator,childs,context: (context['values']['a'],None))
b = ASTNode('b',Type=NodeType.Variable,Context=context,Resolver=lambda operator,childs,context: (context['values']['b'],None))
c = ASTNode(5,Resolver=lambda operator,childs,context: (5,None))
operation = ASTNode('++',Checker=OperatorChecker,Context=context,Resolver=AsigmentResolver)
operation.Childs = [b,c]
op1 = ASTNode('-',Resolver=BinaryResolver)
op1.Childs = [a,operation]

result = op1.Result

print(f'{result[0]},{result[1]}')
print(context)