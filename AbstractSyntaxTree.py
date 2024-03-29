from EnumsTokensDefinition import Operator,Type,Simbol,TokenType,Keyword
from EnumIntermediateCodeDefinitions import IntermediateCodeType

NumericOperators = [
    Operator.Plus,
    Operator.PPlus,
    Operator.Minus,
    Operator.MMinus,
    Operator.Mul,
    Operator.Div,
    Operator.Rest,
    Operator.Exp
]

StringOperators = [
    Operator.Concat
]

BooleanOperators = [
    Operator.LessEqThan,
    Operator.LessThan,
    Operator.GreatherEqThan,
    Operator.GreatherThan,
    Operator.DoubleEq,
    Operator.Distint,
    Operator.Is
]

class Node:
    
    def __init__(self,token,childs=None):
        self._token = token
        self._childs = childs
        pass
    
    @property
    def Token(self):
        return self._token
    
    @property
    def Childs(self):
        return self.Childs
    
    @property
    def AbstractSyntaxTree(self):
        """
        devuelve el AST asociado a este nodo
        """
        
        raise NotImplementedError()
    
    @property
    def Type(self):
        """
        retorna el tipo que devuelve el token asociado a este nodo
        """
        
        raise NotImplementedError()
    
    @property
    def CILType(self):
        """
        retorna el tipo de seccion de codigo CIL que le corresponde
        """
        
        raise NotImplementedError()
    
    @property
    def NodeType(self):
        """
        devuelve el tipo del nodo
        """
        
        raise NotImplementedError()
    
    pass

class LiteralNode(Node):
    
    def __init__(self,token):
        super().__init__(token)
        pass
    
    @property
    def AbstractSyntaxTree(self):
        return self
    
    @property
    def Type(self):
        return self._token.SelfType
    
    @property
    def NodeType(self):
        return self._token.Type
    
    @property
    def CILType(self):
        return IntermediateCodeType.Data
    
    pass

class VariableNode(Node):
    
    def __init__(self,token):
        super().__init__(token)
        pass
    
    @property
    def Type(self):
        return Type.NONE
    
    @property
    def NodeType(self):
        return self._token.Type
    
    @property
    def CILType(self):
        return IntermediateCodeType.Definition
    
    pass

class OperatorNode(Node):
    
    def __init__(self,token,childs):
        super().__init__(token,childs)
        pass
    
    @property
    def NodeType(self):
        return self._token.Type
    
    @property
    def Type(self):
        if NumericOperators.count(self._token) > 0:
            return Type.Number
        if StringOperators.count(self._token) > 0:
            return Type.String
        if BooleanOperators.count(self._token) > 0:
            return Type.Boolean
        return Type.NONE
    
    @property
    def CILType(self):
        return IntermediateCodeType.Operator
    
    pass

class BinaryOperator(OperatorNode):
    
    def __init__(self,token,left,right):
        super().__init__(token,[left,right])
        pass
    
    @property
    def Left(self):
        return self._childs[0]
    
    @property
    def Right(self):
        return self._childs[1]
    
    @property
    def AbstractSyntaxTree(self):
        self._childs[0] = self.Left.AbstractSyntaxTree
        self._childs[1] = self.Right.AbstractSyntaxTree
        return self
    
    pass

class UnaryOperator(OperatorNode):
    
    def __init__(self,token,value):
        super().__init__(token,[value])
        pass
    
    @property
    def AbstractSyntaxTree(self):
        self._childs[0] = self._childs[0].AbstractSyntaxTree
        return self
    
    pass

class TernaryOperator(OperatorNode):
    
    def __init__(self,token,condition,result1,result2):
        super().__init__(token,[condition,result1,result2])
        pass
    
    @property
    def Condition(self):
        return self._childs[0]
    
    @property
    def AfirmativeResult(self):
        return self._childs[1]
    
    @property
    def NegativeResult(self):
        return self._childs[2]
    
    @property
    def AbstractSyntaxTree(self):
        self._childs[0] = self.Condition.AbstractSyntaxTree
        self._childs[1] = self.AfirmativeResult.AbstractSyntaxTree
        self._childs[2] = self.NegativeResult.AbstractSyntaxTree
        pass
    
    pass

class SimbolNode(Node):
    
    def __init__(self,token):
        super().__init__(token)
        pass
    
    @property
    def NodeType(self):
        return self._token.Type
    
    @property
    def Type(self):
        return Type.NONE
    
    @property
    def AbstractSyntaxTree(self):
        return None
    
    @property
    def CILType(self):
        return None
    
    pass

class LabelNode(Node):
    
    def __init__(self,token,childs):
        super().__init__(token,childs)
        pass
    
    @property
    def NodeType(self):
        return 'LABEL'
    
    @property
    def Type(self):
        return 'UNDEFINED'
    
    @property
    def AbstractSyntaxTree(self):
        
        if len(self._childs) == 1:
            return self._childs[0].AbstractSyntaxTree
        
        index = 0
        while index < len(self._childs):
            
            if self._childs[index].Type == TokenType.Simbol:
                self._childs.pop(index)
                continue
            
            self._childs[index] = self._childs[index].AbstractSyntaxTree
            
            if self._childs[index] == None:
                self._childs.pop(index)
                continue
            
            index += 1
            
            pass
        
        index = 0
        while index < len(self._childs):
            if self._childs[index].Type == TokenType.Operator:
                break
            pass
        
        node = self._childs[index]
        self._childs.pop(index)
        node = self._childs
        
        return node
    
    @property
    def CILType(self):
        return None
        
    pass

class DefinitionNode(Node):
    
    def __init__(self,token,block):
        super().__init__(token,[block])
        pass
    
    @property
    def Block(self):
        return self._childs[0]
    
    @property
    def AbstractSyntaxTree(self):
        self._childs[0] = self.Block.AbstractSyntaxTree
        return self
    
    @property
    def Type(self):
        return Type.NONE
    
    @property
    def CILType(self):
        return IntermediateCodeType.Definition
    
    pass

class TypeDefinitionNode(DefinitionNode):
    
    @property
    def CILType(self):
        return IntermediateCodeType.TypeDefinition
    
    pass

class FunctionDefinitionNode(DefinitionNode):
    
    @property
    def CILType(self):
        return IntermediateCodeType.FunctionDefinition
    
    pass