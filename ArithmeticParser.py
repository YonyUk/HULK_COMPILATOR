from ParserInterface import IExpressionParser
from GrammarDefinition import ArithMeticGrammar,ArithmeticTranslator,ArithmeticNonTerminals,ArithmeticTerminals,ArithmeticProductions
from RegExInterface import IRegEx,State
from GrammarParser import GrammarParser
from GrammarInterface import Grammar

class ArithmeticParser(IExpressionParser):
    
    def __init__(self):
        self._grammar = ArithMeticGrammar
        self._translator = ArithmeticTranslator
        pass
        
    pass

AG = ArithMeticGrammar
parser = GrammarParser(AG)
print(parser._states)