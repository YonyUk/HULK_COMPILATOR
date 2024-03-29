from enum import Enum

class IntermediateCodeType(Enum):
    
    Data = 0
    Expression = 1
    Body = 2
    Function = 3
    Type = 4
    FunctionInvocation = 5
    
    pass