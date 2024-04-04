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
<<<<<<< HEAD
>>>>>>> 49a3f4f (grammar modified extensifly)
=======
import DerivationTree
>>>>>>> ae2415e (assembling ast structure to parser)

class GrammarParser(IRegEx,IShiftReduceParser):
    """
    GRAMMATIC PARSING

    """
    operator_procedence =[
        
        ['[','(','{'],
        [']',')'],
        ["c"],
        ['}'],
        ['as'],
        ['^','%','**'],
        ['*','/'],
        ['+','-'],
        ['>','<','>=','<=','==', '~' ,'is'],
        ['&','|','!'],
        ['.'],
        ['=','+=','-=','/=','*=','--',':=','++','--'],
        ["let"],
        ['if'],
        ['elif'],
        ['else'],
        ['@','@@'],
        [','],
        ['=>'],
        ['in' ],
        ['||'],
        [";"],
        ["$2"],
        ["$1","$3"],
    ]
    
    def __init__(self,grammar,code ):

        self._grammar = grammar
        self._error = None
        self._match = False
        self._stack = []
        self.derivation_Tree: DerivationTree.DerivationTree = None
        
        parsed_code = self.gradient_parser(grammar,self._stack,code)
        
        if not parsed_code:
            self.Error = True
        
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
<<<<<<< HEAD
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
=======
=======
    @property
    def check_point(self,last_reduction):
        self.last_reduction = last_reduction
        
        return self.last_reduction
    
>>>>>>> ae2415e (assembling ast structure to parser)
    def compare_procedence(self , pivote , pointer):
>>>>>>> b8678ef (parser almost finished)
        
        '''
        compare precedence between operator1 and operator2:
        ->  0: equal procedence
        ->  1: grater procedence
        -> -1: lower procedence        
        '''
        
        if pivote == "(" : return 0
        if pivote == "{" : return 0
        if pivote == "[" : return 0
        
        if pointer == "(" and ( pivote == ")" ) : return -1
        
        if pointer == "{" and ( pivote == "}" ): return -1
        
        if pointer == "[" and ( pivote == "]"): return -1
        
        if pointer == "$1": return 0 
        if pointer == "$2" or pivote == "$2" : return -1 
        
        if any( pointer == item for item in [']',')','}'] ) or any( pivote == item for item in [']',')','}'] ) :
            return -1
        
        if any( pointer == item for item in ['[','(','{'] ) or any( pivote == item for item in ['[','(','{'] ) :
            return -1
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(pivote) and list(operators).__contains__(pointer):
                return 0
            
            if list(operators).__contains__(pivote) and not list(operators).__contains__(pointer):
                return 1
            
            if not list(operators).__contains__(pivote) and list(operators).__contains__(pointer):
                return -1
            
    def is_operator(self,item):
        
        for operators in self.operator_procedence:
            
            if list(operators).__contains__(item): return True
        
        return False
    
    # the stack_pointer has the structure ( "index" in code , operator "item" )
    stack_pointer=[( 0 ,"$1")]
    best_match = 0
    
    def match(self , target:list , derivation:list ):
        
        if len(target) != len(derivation):
            return False
        
        index = 0

        while index < len(derivation) :
            
            if target[index][0] != derivation[index]: return False
            
            index += 1
        
        if len(derivation) > self.best_match:
            
            self.best_match = len(derivation)      
            
            return  True
    
        else: return  False
        
    def _shift_reduce(self , pivot , index_pointer ,next_point ):
    
        '''
        return True if shift
        return False if reduce
        return shift if not an operator (True)
        
        '''    
        if len(self.stack_pointer) == 0:
            return True
        
        if self.is_operator(pivot):
            
            result = self.compare_procedence( pivot , self.stack_pointer[next_point][1] )

            if result == 0 or result == 1 :

                self.stack_pointer.append((index_pointer,pivot))

                return True
            
            else:
                return False
        
        return True
    
    def remove_item_stack(self , stack:list ,pop_number):
        
        i=0
        while i < pop_number:
            
            stack.pop()
            
            i +=1
        
        return stack

    def reduce_stack(self , stack:list , gramar , next_point ):
            
        self.best_match =0
        
        sub_stack = stack[ self.stack_pointer[next_point][0] : ]
        
        best_match=[]
        
        index = 0
        
        pop_number = 0
        while index < len(sub_stack):
        
            target = sub_stack[ index: ]
            
            for productions in gramar:
                
                for sub_production in productions:
                    
                    for derivation in sub_production[1]: # walk through each derivation and stay with the longer prefix that matches
                        
                        new_best_match = self.match(target,derivation)
                        
                        if new_best_match :
                            
                            best_match = sub_production[0]
                            
                            pop_number = len(derivation)
            
            index += 1
            
        if len(best_match) > 0:

            token_list = self.match_derivation_token( best_match , stack[ len(stack)- pop_number :] )

            new_derivation_tree = self.derivation_tree( best_match , token_list )
            
            new_stack = self.remove_item_stack(stack=stack , pop_number= pop_number )
            
            new_stack.append(( best_match , new_derivation_tree ))
            
            return new_stack , True
        
        return stack , False
    
    def match_derivation_token(self, label ,reduced_token):
        
        token_list = []
        
        for item in reduced_token:
            
            
            if item[0] == "$1" or item[0] == "$2" or item[0] == "$3":
                continue
    
            token_list.append(item[1])
        
        return ( label, token_list )
    
    def reduce_pointer( self , pointer:list , stack:list ): # pop all pointer which where reduced
        
        pointer.reverse()
        
        new_pointer = []
        for p in pointer:
            
            if p[0] <= len(stack) - 1 and p[1] == stack[p[0] ]:
                new_pointer.append(p)
        
        new_pointer.append(pointer[-1])
        new_pointer.reverse()
        
        return stack,new_pointer
    
    def parsed_code(self,stack):
            
        return len(stack) == 3 and (stack[1][0] == "E" or stack[1][0] == "b" )
    
    def gradient_parser(self,gramar,stack:list , code ):        
        '''
        parse the string using gradient parser
        
        '''
        index_pointer = 1
        
        shift = True
        
        while index_pointer <  len(code) :
            
            next_pointer =- 1
            
            shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer= len(stack) ,next_point= -1 ) # determines action | shift or reduce
                    
            while not shift:
                
                stack , modified = self.reduce_stack(stack ,gramar , next_pointer ) # try to reduce 
        
                if not modified: # verify any change in the stack
                    
                    next_pointer -=1 # check agin for reduction but using another pointer in the stack pointer
                    shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer = len(stack) , next_point= next_pointer ) 
                
                else: 
                    
                    next_pointer =- 1 # if reduction was made , restart pointer in the stack pointer

                    stack,self.stack_pointer = self.reduce_pointer( self.stack_pointer ,stack) # reduce the stack pointer
                    
                    shift = shift = self._shift_reduce( pivot= code[index_pointer][0] ,index_pointer = len(stack) , next_point= next_pointer ) # check again | shift or reduce
                
<<<<<<< HEAD
                else: shift = False
                
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
            
=======
            stack.append( code[index_pointer] )
<<<<<<< HEAD
            print(stack)
>>>>>>> b8678ef (parser almost finished)
=======
            
>>>>>>> 9249b2b (comment added)
            index_pointer += 1
    
        return self.parsed_code(stack)
    
    @property
    def derivation_tree(self, label , token_list):
        
        '''
        pattern to follow -> existing tree is child of the new node
        '''
        
<<<<<<< HEAD
        new_node = DerivationTree()
        
        
        
        pass
>>>>>>> 6da4297 (translator moved from GrammarParser)
=======
        return DerivationTree.builder( label , token_list )
>>>>>>> ba41d7d (hard-coded Parser-AST)
