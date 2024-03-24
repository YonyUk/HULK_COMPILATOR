from RegExDefinitions import TokenFinitRegEx
from RegExInterface import State
from GrammarInterface import Grammar

class GrammarParser(TokenFinitRegEx):
    
    _states = {}
    
    def __init__(self,grammar):
        self._grammar = grammar
        self._createLR0Items()
        pass
    
    def _createLR0Items(self):
        """
        crea los items LR(0) dado la gramatica del parser
        """
        
        for token in self._grammar._Productions.keys():
            
            items = []
            
            for production in self._grammar._Productions[token]:
                
                for i in range(len(production) + 1):
                    if items.count(production[:i]) == 0:
                        items.append(production[:i])
                        pass
                    pass
                pass
        
            self._states[token] = items
            
            pass
        
        pass
    
    pass
