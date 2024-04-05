from CIL import CilTree
from DerivationTree import *
from IntermediateCodeGeneratorDefinitions import *

def CilBuilder(node):
    pass

def CILFunctionCallBuilder(node):
    return CilTree(FunctionInvocationNode(node.name),[])

def CILParamBuilder(node):
    cils = []
    for param in node.param:
        cils.append(ParamNode(param))
        pass
    return CilTree(ParamsNode(cils),[])

def CilBinaryExpression(node):
    return CilTree(BinaryExpressionNode(CilBuilder(node.left).Value,CilBuilder(node.right).Value,node.id),[])

