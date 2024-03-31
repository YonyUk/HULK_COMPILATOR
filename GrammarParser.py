from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
from GrammarInterface import Grammar
from ParserInterface import IShiftReduceParser
from copy import copy
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
    

    def Restart(self):
        for automaton in self._automatons.keys():
            self._automatons[automaton].Restart()
            pass
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