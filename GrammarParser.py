from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State,IRegEx
from GrammarInterface import Grammar
from ParserInterface import IShiftReduceParser
from copy import copy

class GrammarParser(IRegEx,IShiftReduceParser):
    """
    clase encargada de parsear una gramatica
    """
    _automatons = {}
    _items = {}
    
    def __init__(self,grammar,translator):
        self._translator = translator
        self._grammar = grammar
        self._createAutomatons()
        self._error = None
        self._expression = None
        self._match = False
        self._state = State.START
        self._laststate = State.START
        self._stack = []
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
        return self._laststate
    
    def _createAutomatons(self):
        
        for production in self._grammar._Productions.keys():
            
            items = []
            for derivation in self._grammar._Productions[production]:
                for i in range(len(derivation) + 1):
                    items.append(f'{derivation[:i]}.{derivation[i:]}')
                    pass
                pass
            
            automaton = TokenFinitRegEx(items,lambda token: token)
            self._automatons[production] = automaton
            self._items[production] = items
            pass
            
        pass
    
    def Restart(self):
        for automaton in self._automatons.keys():
            self._automatons[automaton].Restart()
            pass
        self._laststate = State.START
        self._state = State.START
        pass
    
    @property
    def _shift(self):
        for i in range(len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            state = None
            for production in self._items.keys():
                for s in self._items[production]:
                    if s.startswith(token):
                        state = s
                        follow = state.split('.')[1]
                        if len(follow) > 0: return True
                        pass
                    pass
                pass
            
            return False
    
    def Shift(self):
        pass
    
    @property
    def _reduce(self):
        # revisar este metodo
        for i in range(len(self._stack)):
            token = ''
            for j in range(i,len(self._stack)):
                token += self._stack[j]
                pass
            
            state = None
            for production in self._items.keys():
                found = False
                for s in self._items[production]:
                    if s.startswith(token):
                        state = s
                        found = True
                        break
                    pass
                if found: break
                pass
            
            follow = state.split('.')[1]
            
            if len(follow) == 0: return True
            pass
        
        return False
    
    def Reduce(self):
        
        while self._reduce:
            
            reduced = False
            for i in range(len(self._stack)):
                token = ''
                for j in range(i,len(self._stack)):
                    token += self._stack[j]
                    pass
                
                while len(self._stack) > len(token) - 1:
                    self._stack.pop()
                    pass
                
                for production in self._items.keys():
                    if self._items[production].count(token + '.') > 0:
                        token = production
                        self._stack.append(token)
                        reduced = True
                        break
                    pass
                
                if reduced: break
                
                pass
            
            pass
        pass
    
    def Forward(self,token):
        
        self._laststate = copy(self._state)
  
        for i in range(len(self._stack) + 1):
            t = ''
            for j in range(i,len(self._stack)):
                t += self._stack[j]
                pass
            t += token
            
            for production in self._items.keys():
                for state in self._items[production]:
                    if state.startswith(t + '.'):
                        self._state = State.FINAL
                        self._stack.append(token)
                        return True
                    pass
                pass
        
        self._state = State.FAULT
        
        return False
    
    def Parse(self,tokens):
        
        position = 0
        
        while self.Forward(tokens[position]):
            
            if self._reduce and self._shift:
                raise Exception('Esta gramatica no es LR(0)')
            
            if self._reduce:
                self.Reduce()
                pass
            else:
                self.Shift()
                pass
            self.Restart()
            position += 1
            pass
        pass
    
    pass
