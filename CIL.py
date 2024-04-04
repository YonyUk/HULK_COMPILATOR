from EnumIntermediateCodeDefinitions import IntermediateCodeType
from IntermediateCodeGeneratorDefinitions import *

class CilTree:
    
    def __init__(self,node,childs):
        self._node = node
        self._childs = childs
        pass
    
    @property
    def Functions(self):
        """
        retorna todos los nodos que son funciones
        """
        functions = []
        for child in self._childs:
            for function in child.Functions:
                if functions.count(function) == 0:
                    functions.append(function)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Function and functions.count(self._node.Name) == 0:
            functions.append(self._node)
            pass
        
        return functions
    
    @property
    def Data(self):
        """
        retorna todos los datos string usados
        """
        
        data = []
        for child in self._childs:
            for d in child.Data:
                if data.count(d) == 0:
                    data.append(d)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Function:
            for d in self._node.Body.Data:
                if type(d) == DataNode and data.count(d) == 0:
                    data.append(d)
                    pass
                pass
            pass
        
        return data
    
    @property
    def Types(self):
        
        types = []
        
        for child in self._childs:
            for t in child.Types:
                if types.count(t) == 0:
                    types.append(t)
                    pass
                pass
            pass
        
        if self._node.Type == IntermediateCodeType.Type and types.count(self._node) == 0:
            types.append(self._node)
            pass
        
        return types
    
    @property
    def DataDefinitions(self):
        definition = '.DATA\n\n'
        for data in self.Data:
            definition += data.Template['DATA'] + '\n'
            pass
        return definition + '\n\n'
    
    @property
    def TypesDefinitions(self):
        definition = '.TYPES\n\n'
        for t in self.Types:
            d = t.Template['TEMPLATE'].split(';')
            definition += d[0] + '\n'
            for i in range(1,len(d) - 1):
                definition += d[i] + ';\n'
                pass
            definition += d[len(d) - 1] + '\n\n'
            pass
        return definition + '\n\n'
    
    @property
    def FunctionsDefinitions(self):
        definition = '.CODE\n\n'
        
        for function in self.Functions:
            d = function.Template['TEMPLATE'].split(';')
            definition += d[0] + ';\n'
            for i in range(1,len(d) - 1):
                if len(d[i]) > 0:
                    definition += d[i] + ';\n'
                    pass
                pass
            definition += d[len(d) - 1] + '\n\n'
            pass
        
        return definition
    
    @property
    def Code(self):
        
        datas = self.DataDefinitions
        types = self.TypesDefinitions
        codes = self.FunctionsDefinitions
        
        return datas + types + codes
    
    pass
# ################################COMPROBANDO############################