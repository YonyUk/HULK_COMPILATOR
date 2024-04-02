from EnumsTokensDefinition import TokenType,Type
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES,SIMBOL_VALUES,OPERATOR_VALUES
from enum import Enum
from TokensDefinition import SimbolToken,OperatorToken,LiteralToken

class NodeType(Enum):

    Variable = 0
    Number = 1
    String = 2
    Boolean = 3
    Function = 4
    Type = 5
    Undefined = 6

    pass

class DerivationTree:
    """
        Clase que define al arbol de derivacion de una gramatica
        token: Token
        childs: list(DerivationTree)
        builder: constructor de la clase de nodo AST que devolvera
    """
    
    def __init__(self,token,childs,builder):

        self._token = token
        self._childs = childs
        self._builder = builder
        pass
    
    @property
    def IsLeaf(self):
        return len(self._childs) == 0
    
    @property
    def Childs(self):
        return [child for child in self._childs if not child.Type == TokenType.Simbol and not len(child.Text) == 0]
    
    @property
    def IsRelevant(self):
        return KEYWORD_VALUES.count(self.Text) > 0 or SIMBOL_VALUES.count(self.Text) > 0 or OPERATOR_VALUES.count(self.Text) > 0
    
    @property
    def Type(self):
        try:
            return self._token.Type
        except Exception:
            return Type.NONE
        pass
    
    @property
    def Text(self):
        try:
            return self._token.Text
        except Exception:
            return self._token
    
    @property
    def Token(self):
        return self._token
    
    @property
    def ASTNode(self):
        return self._builder(self._token)
    
    @property
    def AST(self):
        """
        retorna el AST asociado
        """
        # Si es el caracter vacio
        if len(self.Text) == 0:
            return None
        # Si es un nodo hoja
        if self.IsLeaf:
            return self.ASTNode
        # Si solamente tiene un hijo
        if len(self.Childs) == 1:
            return self.Childs[0].AST
        # Si es un operador
        if self.Type == TokenType.Operator:
            # computamos los ast de cada hijo
            ASTChilds = [child.AST for child in self.Childs]
            # creamos el astnode correspondiente a este nodo
            node = self.ASTNode
            # le ponemos los ast hijos de este nodo
            node.Childs = ASTChilds
            return node
        # si el nodo no ofrece ninguna informacion
        if not self.Type == TokenType.Operator and not self.Type == TokenType.Keyword and not self.Type == TokenType.Variable:
            # buscamos por algun hijo que si nos ofrezca informacion
            childs = self.Childs
            position = 0
            for i in range(len(childs)):
                # encontramos el nodo deseado, un operador, una variable, un literal o una palabra clave
                if childs[i].Type == TokenType.Operator or childs[i].Type == TokenType.Keyword or childs[i].Type == TokenType.Variable or childs[i].Type == TokenType.Literal:
                    position = i
                    break
                pass
            #  extraemos el nodo encontrado
            node = childs.pop(position)
            #  computamos sus hijos y los agregamos a los hijos que tenemos hasta ahora
            childs = childs.__add__(node.Childs)
            # eliminamos la referencia a sus hijos
            node._childs = None
            # computamos el astnode correspondiente al nodo encontrado
            ASTNode = node.ASTNode
            # computamos los ast de cada hijo existente
            ASTChilds = []
            for child in childs:
                ASTChilds.append(child.AST)
                pass
            # le pasamos la referencia de ellos al astnode actual
            ASTNode.Childs = ASTChilds
            # retornamos el AST construido
            return ASTNode
        # extraemos el ASTNode correspondiente al nodo actual
        ASTNode = self.ASTNode
        # computamos los AST hijos
        ASTChilds = [child.AST for child in self.Childs]
        # agregamos la referencia y retornamos
        ASTNode.Childs = ASTChilds
        return ASTNode
    
    pass

class ASTNode:
    """
    Clase que define los nodos del AST
        token: Token
        token -> token correspondiente al nodo
        kwargs -> debe contener las funciones 'Resolver', 'Checker' y Type
        Resolver debe recibir por parametros al valor de este nodo y sus hijos
        Checker debe recibir por parametros al valor de este nodo, sus hijos y
        un diccionario con el contexto hasta el
        Ambos, el Resolver y el Checker deben devolver una tupla donde el primer
        valor es el resultado y el segundo el error en caso de ocurrir
        
    """
    
    Childs = []
    Resolver = None
    Checker = None
    Context = {}
    ASTType = NodeType.Undefined
    
    def __init__(self,token,**kwargs):
        
        self.Value = token
        if list(kwargs.keys()).count('Type') > 0:
            self.ASTType = kwargs['Type']
            pass
        if list(kwargs.keys()).count('Checker') > 0:
            self.Checker = kwargs['Checker']
            pass
        if list(kwargs.keys()).count('Resolver') > 0:
            self.Resolver = kwargs['Resolver']
            pass
        if list(kwargs.keys()).count('Context') > 0:
            self.Context = kwargs['Context']
            pass
        pass
    
    @property
    def Check(self):
        """
        checkea la semantica del nodo
        returna true si esta correcta, false,Error en otro caso donde Error es el error lanzado
        si no se paso ningun checker como parametro retornara true siempre
        el checker debe devolver una tupla donde el primer valor es el resultado y el segundo el error en caso de existir
        
        """
        
        if self.Checker == None:
            return True,None
        return self.Checker(self.Value,self.Childs,self.Context)
    
    @property
    def Result(self):
        """
        ejecuta la orden almacenada en este nodo y devuelve el resultado
        si no se paso ningun "resolver" como parametro , retornara el valor asociado al nodo.
        El resolver debe devolver una tupla donde el primer valor es el resultado, el segundo es el error en caso de existir
        
        """
        
        if self.Resolver == None:
            return self.Value
        return self.Resolver(self.Value,self.Childs,self.Context)
    
    @property
    def Type(self):
        
        if len(self.Childs) == 0:
            return type(self.Value)
        t = type(self.Childs[0])
        for i in range(1,len(self.Childs)):
            if not self.Childs[i].Type == t: return Type.NONE
            pass
        return t
    
    pass

class builder:
    
    '''
    -> This class has to return the AST for each kw ,literal and symbol 
    
    -> This is useful for AST contruction from parser.
    
    -> The "builder feature" is the function that know how to return a feature AST
    
    e.j:
    
    a = LiteralToken('5',Type.Number)
    b = LiteralToken('10',Type.Number)
    c = LiteralToken('20',Type.Number)
    lp = SimbolToken('(')
    rp = SimbolToken(')')

    plus = OperatorToken('+')
    minus = OperatorToken('-')

    A = DerivationTree(a,[],lambda token: ASTNode(int(token.Text)))
    B = DerivationTree(b,[],lambda token: ASTNode(int(token.Text)))
    Plus = DerivationTree(plus,[A,B],lambda token: token)

    LP = DerivationTree(lp,[],lambda token: token)
    RP = DerivationTree(rp,[],lambda token: token)
    E = DerivationTree('e',[LP,Plus,RP],lambda token: token)
    C = DerivationTree(c,[],lambda token: ASTNode(int(token.Text)))
    Minus = DerivationTree(minus,[C,E],lambda token: token)

    ast = Minus.AST

    In this case, this function : "lambda token: ASTNode(int(token.Text))"  
    returns an ASTNode class of a literal, with no "resolver" and no checker , because it is just a literal,
    as you can see it just has value specified in its "args" , and the same happend for the rest of the cases
    
    __YOUR TASK__:
    
    -> For features like blocks you need to implement its "checker" for "type inference", and it resolver in order to
       minimize it nodes to build the final AST of its node.
    
    note: blocks type is infered from it "last operation".
    
    '''
    
    pass