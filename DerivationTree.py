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

    def __init__(self, token, childs, builder):

        self._token = token
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

    def __init__(self, token, token_list, **kwargs):

        self.Value = token
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
        if list(kwargs.keys()).count("Context_Builder") > 0:
            self.Context = kwargs["Context_Builder"]
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

    @property
    def Type(self):  # tries to infer types

        if len(self.Childs) == 0:  # if no node , return value type
            return type(self.Value)

        t = type(
            self.Childs[0]
        )  # if at least one node, return the type of the first node

        for i in range(
            1, len(self.Childs)
        ):  # check for the rest of the childs of this node if they are of the same type

            if not self.Childs[i].Type == t:
                return Type.NONE

            pass

        return t

    pass


class context:

    def __init__(self, derivation_tree):
        pass

    # return derivation_tree_with_context


class builder:

    # '4' '+' '(' '5' '+' '6' ')' ';'

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
        if len(self._token_list == 2 and self._token_list[0] == KEYWORD_VALUES[1]):
            return builder.ASTPrint.Resolve
        if len(self._token_list == 4 and self._token_list[0] == KEYWORD_VALUES[2]):
            return builder.ASTFunction.Resolve
        if len(self._token_list == 2 and self._token_list[0] == KEYWORD_VALUES[3]):
            return builder.ASTLet.Resolve
        if len(self._token_list == 3 and self._token_list[1] == KEYWORD_VALUES[4]):
            return builder.ASTIn.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[5]):
            return builder.ASTProtocol.Resolve
        if len(
            self._token_list == 4
            and self._token_list[0] == KEYWORD_VALUES[5]
            and self._token_list[2] == "extends"
        ):
            return builder.ASTProtocolExtend.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[6]):
            return builder.ASTType.Resolve
        if len(
            self._token_list == 3
            and self._token_list[0] == KEYWORD_VALUES[6]
            and self._token_list[2] == "inherits"
        ):
            return builder.ASTType.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[7]):
            return builder.ASTWhile.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[8]):
            return builder.ASTFor.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[9]):
            return builder.ASTIf.Resolve
        if len(self._token_list == 2 and self._token_list[0] == KEYWORD_VALUES[10]):
            return builder.ASTElse.Resolve
        if len(self._token_list == 3 and self._token_list[0] == KEYWORD_VALUES[11]):
            return builder.ASTElif.Resolve
        pass

        """Cada uno es un Nodo en el AST"""

    class ASTLiteral:

        def __init__(self, token):
            self._token = token

        def Resolve(self):
            return ASTNode(self._token)

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
            )
            pass

        pass

    class ASTLabel:
        def __init__(self, label, token):

            self._label = label
            self._token = token
            pass

        def Resolve(self):

            return ASTNode(self._token, [])

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
            )

    pass

    class ASTUnaryOp:
        def __init__(self, left, operator):
            self._left = left
            self._operator = operator

        def Resolve(self):
            return ASTNode(
                self._operator,
                [self._left],
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

        pass

    class ASTProtocol:
        def __init__(self, label, body):
            self.value = "protocol"
            self._label = label
            self._body = body

        def Resolve(self):
            return ASTNode(self.value, [self._label, self._body])

        pass

    pass

    class ASTProtocolExtend:
        def __init__(self, label1, label2, body):
            self.value = "protocol"
            self._label1 = label1
            self._label2 = label2
            self._body = body
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._label1, self._label2, self._body])
            pass

        pass

    class ASTType:
        def __init__(self, label, body):
            self.value = "type"
            self._label = label
            self._body = body

        def Resolve(self):
            return ASTNode(
                self.value,
                [self._label, self._body],
                {"Resolve": self.Resolve(), "Type": self._label},
            )

        pass

    pass

    class ASTTypeInherit:
        def __init__(self, label1, label2, body):
            self.value = "type"
            self._label1 = label1
            self._label2 = label2
            self._body = body
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._label1, self._label2, self._body])
            pass

        pass

    class ASTIn:
        def __init__(self, left, rigth):
            self.value = "In"
            self._left = left
            self._rigth = rigth
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._left, self._rigth])
            pass

        pass

    class ASTLet:
        def __init__(self, t):
            self._t = t
            self.value = "let"
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._t])
            pass

        pass

    class ASTFor:
        def __init__(self, T, E):
            self.value = "for"
            self._T = T
            self._E = E
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._T, self._E])
            pass

        pass

    class ASTWhile:
        def __init__(self, T, E):
            self.value = "while"
            self._T = T
            self._E = E
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._T, self._E])
            pass

        pass

    class ASTIf:
        def __init__(self, T, E):
            self.value = "if"
            self._T = T
            self._E = E

            pass

        def Resolve(self):
            return ASTNode(self.value, [self._T, self._E])
            pass

        pass

    class ASTElIf:
        def __init__(self, T, E):
            self.value = "elif"
            self._T = T
            self._E = E

            pass

        def Resolve(self):
            return ASTNode(self.value, [self._T, self._E])
            pass

        pass

    class ASTElse:
        def __init__(self, T):
            self.value = "else"
            self._T = T

            pass

        def Resolve(self):
            return ASTNode(self.value, [self._T])
            pass

        pass

    class ASTPrint:
        def __init__(self, body):
            self.value = "print"
            self._body = body
            pass

        def Resolve(self):
            return ASTNode(self.value, [self._body])
            pass

        pass

    pass
