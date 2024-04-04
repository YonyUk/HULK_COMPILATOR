from EnumsTokensDefinition import TokenType, Type, Keyword
from HULK_LANGUAGE_DEFINITION import KEYWORD_VALUES, SIMBOL_VALUES, OPERATOR_VALUES
from enum import Enum
from TokensDefinition import SimbolToken, OperatorToken, LiteralToken


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
    This class defines the derivation tree of a grammar

    token: Token
    childs: list(DerivationTree)

    builder: constructor of the AST node class that will return

    """

    def __init__(self, label, childs, builder):

        self._token = label
        self._childs = childs
        self._builder = builder

        pass

    @property
    def IsLeaf(self):

        return len(self._childs) == 0

    @property
    def Childs(self):

        return [
            child
            for child in self._childs
            if not child.Type == TokenType.Simbol and not len(child.Text) == 0
        ]

    @property
    def IsRelevant(self):

        return (
            KEYWORD_VALUES.count(self.Text) > 0
            or SIMBOL_VALUES.count(self.Text) > 0
            or OPERATOR_VALUES.count(self.Text) > 0
        )

    @property
    def Type(self):

        try:
            return self._token.Type

        except Exception:
            return Type.NONE

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
        if (
            not self.Type == TokenType.Operator
            and not self.Type == TokenType.Keyword
            and not self.Type == TokenType.Variable
        ):
            # buscamos por algun hijo que si nos ofrezca informacion
            childs = self.Childs
            position = 0
            for i in range(len(childs)):
                # encontramos el nodo deseado, un operador, una variable, un literal o una palabra clave
                if (
                    childs[i].Type == TokenType.Operator
                    or childs[i].Type == TokenType.Keyword
                    or childs[i].Type == TokenType.Variable
                    or childs[i].Type == TokenType.Literal
                ):
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
    Context = None
    ASTType = NodeType.Undefined

    Context_Builder = None
    
    def __init__(self, label , token_list , **kwargs ):
        
        self.Value = label
        self.toke_list=token_list
        
        if list(kwargs.keys()).count("Type") > 0:
            self.ASTType = kwargs["Type"]
            pass
        if list(kwargs.keys()).count("Checker") > 0:
            self.Checker = kwargs["Checker"]
            pass
        if list(kwargs.keys()).count("Resolver") > 0:
            self.Resolver = kwargs["Resolver"]
            pass
        if list(kwargs.keys()).count("Context") > 0:
            self.Context = kwargs["Context"]
            pass
        
        pass
    
    def get_context(self):
        
        # work with the Contex_Builder to return a context
        
        pass
    
    def context_check(self):
        
        pass

    @property
    def type_checking(self):
        
        """
        checkea la semantica del nodo
        returna true si esta correcta, false,Error en otro caso donde Error es el error lanzado
        si no se paso ningun checker como parametro retornara true siempre
        el checker debe devolver una tupla donde el primer valor es el resultado y el segundo el error en caso de existir

        """

        if self.Checker == None:
            return True, None
        return self.Checker(self.Value, self.Childs, self.Context)

    @property
    def cil_node_code(self):
        """
        return CIL codes

        """

        if self.Resolver == None:
            return self.Value

        return self.Resolver(self.Value, self.Childs, self.Context)

    pass

class builder:

    '''
    ATENCION:

    AST debe poder identificar si , es de tipo "function" ,  de tipo "type" , de tipo "protocolo" o tipo "bloque"
    y dado el tipo de nodo las propiedades de este, ejemplo si es funcion , cuales son sus parametros , su nombre , y su bloque
    
    '''
    

    def __init__(self, label, token_list):
        """Recibimos la lista de tokens"""

        self._token_list = token_list

        pass

    """En esta funcion procesamos la lista de tokens para saber que nodo construir"""

    def Proccess(self):
        if len(self._token_list) == 1:
            builder.ASTLiteral(self._token_list[0])

        if len(
            self._token_list == 3 and self._token_list[1].Type == TokenType.Operator
        ):
            return builder.ASTBinOp.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[0]):
            return builder.ASTNew.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[5]):
            return builder.ASTProtocol.Resolve
        pass

        """Cada uno es un Nodo en el AST"""

    class ASTLiteral:

        def __init__(self, token):
            self._token = token

        def Resolve(self):
            return ASTNode(self._token,[])

    pass

    class ASTNew:

        def __init__(self, label, body):

            self.value = "new"
            self._label = label
            self._body = body
            pass

        def Resolve(self):

            return ASTNode(
                self.value,
                [self._label, self._body],
                Type=self._label
            )
            pass

        pass

    class ASTLabel:
        def __init__(self, label, token):

            self._label = label
            self._token = token
            pass

        def Resolve(self):

            return ASTNode(
                self._token, [], Type=self._label
            )

        pass

    class ASTBinOp:
        def __init__(self, left, operator, rigth):
            self._left = left
            self._operator = operator
            self._rigth = rigth

        def Resolve(self):
            return ASTNode(
                self._operator,
                [self._left, self._rigth],
                Type=TokenType.Operator,
            )

    pass

    class ASTFunction:
        def __init__(self, label, parameters, body):
            self.value = "function"
            self._label = label
            self._parameters = parameters
            self._body = body
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._label, self._parameters, self._body])

        pass

    class ASTProtocol:
        def __init__(self, label, body):
            self.value = "protocol"
            self._label = label
            self._body = body

        def Resolve(self):
            return ASTNode(
                self.value,
                [self._label, self._body],
                Type=self._label
            )

    """
    
    e.j:
    
    a = LiteralToken('5',Type.Number)
    b = LiteralToken('10',Type.Number)
    c = LiteralToken('20',Type.Number)
	
    ast = Minus.AST
    
    """

    pass

