from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
from ParserInterface import IShiftReduceParser
<<<<<<< HEAD
<<<<<<< HEAD
from copy import copy
<<<<<<< HEAD
from os import system

class GrammarParser(IRegEx,IShiftReduceParser):
    
    Tokens = []
    
    def __init__(self,automatons,grammar):
        self._automatons = automatons
        self._error = None
        self._expression = ''
        self._match = False
        self._state = State.START
        self._lastState = State.START
        self._shift = False
        self._reduce = False
        self._grammar = grammar
        self._stack = []
        self._maxPrefixLength = 0
        
        for production in self._grammar._Productions.keys():
            for p in self._grammar._Productions[production]:
                if len(p) > self._maxPrefixLength:
                    self._maxPrefixLength = len(p)
                    pass
                pass
            pass
        
        pass
        
=======
=======
>>>>>>> 6da4297 (translator moved from GrammarParser)
=======
import GRAMATIC_DEFINITION as GD
>>>>>>> 49a3f4f (grammar modified extensifly)

class GrammarParser(IRegEx,IShiftReduceParser):
    """
    clase encargada de parsear una gramatica
    
    """
    operator_procedence =[
        
        ['('],
        ['^','%'],
        ['*','/'],
        ['+','-'],
        ['>','<','>=','<=','==', '~' ,'is'],
        ['['],
        ['&','|','!'],
        ['.'],
        ['=','+=','-=','/=','*=','--',':='],
        ['if',"for",'while'],
        ['elif'],
        ['else'],
        ["P ''"],
        ["X '"],
        ['@','@@'],
        ['as'],
        ['let'],
        [','],
        ['type' , 'new' , 'function', 'in' , 'protocol' , "{"  ],
        [":"],
        [';',"}" , ']',')'],
        ['||'],
        ['$1'],
        ['$2'],
    ]
    
    def __init__(self,grammar,code):

        self._grammar = grammar
        self._error = None
        self._match = False
        self._stack = []
        
        self.gradient_parser(grammar,self._stack,code)
        
        pass
    
>>>>>>> 849d64d (translator moved from GrammarParser)
    @property
    def Error(self):
        return self._error
    
    @property
    def Match(self):
        return self._match
    
    @property
    def Expression(self):
        return self._expression
    
    @property
    def State(self):
        return self._state
    
    @property
    def LastState(self):
<<<<<<< HEAD
        return self._lastState
    
    def Reduce(self):
        
        init = len(self._stack) - self._maxPrefixLength
        for i in range(max(0,init),len(self._stack)):
            
            p = ''
            for j in range(i,len(self._stack)):
                p += self._stack[j]
            
                for production in self._grammar._Productions.keys():
                    if self._grammar._Productions[production].count(p) > 0:
                        return production,p
                    pass
            
                pass
            pass
        
        return None,None
    
    def Shift(self):
        pass
    
    def Forward(self,token):
        
        self._lastState = copy(self._state)
        if self.LastState == State.FINAL:
            self._reduce = True
            pass
        else:
            self._reduce = False
            pass
        
        forward = False
        
        for automaton in self._automatons.keys():
            forward = self._automatons[automaton].Forward(token) or forward
            if self._automatons[automaton].State == State.ONWORK:
                self._state = State.ONWORK
                self._expression = self._automatons[automaton].Expression
                self._shift = True
                
                for value in self._automatons[automaton]._values:
                    if (self._expression + '.') == value:
                        self._state = State.FINAL
                        break
                    pass
                
                pass
            
            pass
        
        if not self._reduce:
            self._shift = True
            pass
                    
        return forward
    

=======
        return self._laststate
    
    def Restart(self):        
        pass
    
<<<<<<< HEAD
>>>>>>> 849d64d (translator moved from GrammarParser)
    def Restart(self):
        for automaton in self._automatons.keys():
            self._automatons[automaton].Restart()
            pass
<<<<<<< HEAD
        self._shift = False
        self._reduce = False
        self._state = State.START
        self._lastState = State.START
        pass
    
    def LoadTokens(self,tokens):
        
        for token in tokens:
            self.Tokens.append(token)
            pass
        
        pass
    
    def Parse(self):
        
        position = 0
        
        
        while len(self.Tokens) > 1:
                        
            while position < len(self.Tokens) and self.Forward(self.Tokens[position]):
                self._stack.append(self.Tokens[position])
                system('clear')
                print(self._stack)
                position += 1
                pass
            
            if self._reduce:
                self._expression = ''
                reduction,production = self.Reduce()
                
                tokens = self.Tokens[position:]

                for i in range(len(production)):
                    self._stack.pop()
                    system('clear')
                    print(self._stack)
                    pass
                                
                self.Tokens = [reduction].__add__(tokens)
                self.Restart()
                position = 0
                pass
            
            if self._shift:
                self.Restart()
                pass
            
            pass
        
        pass

    pass
=======
        self._laststate = State.START
        self._state = State.START
        pass
    
    @property
    def _shift(self):
        for i in range(max(0,len(self._stack) - self._maxPrefixLength),len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            for production in self._items.keys():
                for s in self._items[production]:
                    if s.startswith(token):
                        state = s
                        follow = state.split('.')[1]
                        if len(follow) > 0 and self._position < len(self._expression): return True
                        pass
                    pass
                pass
            pass
        return False
    
    def Shift(self):
        pass
    
    @property
    def _reduce(self):
        # revisar este metodo
        for i in range(max(0,len(self._stack) - self._maxPrefixLength),len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            for production in self._items.keys():
                for s in self._items[production]:
                    if s.startswith(token):
                        follow = s.split('.')[1]
                        if len(follow) > 0: return False
                    pass
                pass
            pass
=======
    def compare_procedence(self , operator1 , operator2):
>>>>>>> 6da4297 (translator moved from GrammarParser)
        
        '''
        campare operator1 precedence to operator2 procedence
        
        return values: 
        
        0: equal procedence
        1: grater procedence
        -1: lower procedence
        
        '''
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(operator1) and list(operators).__contains__(operator2):
                return 0
            
            if list(operators).__contains__(operator1) and not list(operators).__contains__(operator2):
                return 1
            
            if not list(operators).__contains__(operator1) and list(operators).__contains__(operator2):
                return -1
            
    def is_operator(self,item):
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(item): return True
        
        return False
    
    def Tostring( self , prefix ):
        
        s=""
        for item in prefix:
            s += item
        
        return s
    
    # the pointer has the structure ( "index" in code , operator "item" )
    pointer=[( 0 ,"$1")]
    
    def match(self , target , derivation ):
        
        if len(target) < len(derivation):
            return False
        
        index = 0
        while index < len(target) :
            
            if target[index] != derivation[index]: return False
        
        return True
    
    def _shift_reduce(self , pivot , index_pointer ):
    
        '''
        return True if shift
        return False if reduce
        return shift if not an operator (True)
        
        '''    
        if len(self.pointer) == 0:
            return True
        
        if self.is_operator(pivot):
            
            result = self.compare_procedence( pivot , self.pointer[-1][1] )

            if result == 0 or result == 1 :
                self.pointer.append((index_pointer,pivot))
                return True
            
            else:
                return False
        
        return True

    def reduce_stack(self , stack:list , gramar ):
            
        sub_stack = stack[ self.pointer[-1][0] : len(stack) ]
        
        target = self.Tostring(sub_stack)
        
        index = 0
        while index < len(target):
        
            for productions in gramar:
                
                for sub_production in productions:
                    
                    for derivation in sub_production[1]: # walk for each derivation and try to reduce
                    
                        target1 = target[ : index + 1 ]
                        
                        if self.match(target1,derivation):
                            
                            new_stack = stack[ : self.pointer[-1][0]]                

                            

                            stack.append(sub_production[0])
                            
                            stack.append("$")
                            
                            return stack
            
            index += 1
        
        return stack
                    
    def gradient_parser(self,gramar,stack:list , code ):
        
        '''
        make a production posible
        
        '''
        index_pointer = 1
        
        shift = True
        
        while index_pointer <  len(code)  :
                
            shift = self._shift_reduce( pivot= code[index_pointer] ,index_pointer=index_pointer )
            
            stack.append( code[index_pointer] )
            
            while not shift:
                
                stack = self.reduce_stack(stack ,gramar )
                
                self.pointer.pop()
                
                shift = self._shift_reduce( pivot= code[index_pointer] ,index_pointer=index_pointer )
            
            pass
<<<<<<< HEAD
        
        pass
    
<<<<<<< HEAD
    pass
>>>>>>> 849d64d (translator moved from GrammarParser)
=======
    def posible_reduction(self,stack):
        
        reductions = []
        for syntaxis in self._grammar:
=======
>>>>>>> 6f9c51e (gramar modified)
            
            index_pointer += 1
    
        if len(stack) == 3 and (stack[1] == 'E' or stack[1] == 'M') :
            
            # self.State = True
            
            print("parsed")
            
            return
        
        print("not parsed")
        
        return
    
    
    
    def Reduce_AST(self):
        
        
        pass
>>>>>>> 6da4297 (translator moved from GrammarParser)
