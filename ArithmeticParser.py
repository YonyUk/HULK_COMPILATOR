from ParserInterface import IExpressionParser
from GrammarDefinition import ArithMeticGrammar,ArithmeticTranslator,ArithmeticNonTerminals,ArithmeticTerminals,ArithmeticProductions
from RegExInterface import IRegEx,State
from GrammarParser import GrammarParser
from GrammarInterface import Grammar
from RegExDefinitions import TokenFinitRegEx

AG = ArithMeticGrammar

def createItemsLR0(production):
    states = []
    for p in production:
        for i in range(len(p) + 1):
            s = p[:i]
            t = p[i:]
            states.append(s + '.' + t)
            pass
        pass
    return states

a0 = TokenFinitRegEx(createItemsLR0(AG._Productions['Q']),lambda token: token)
a1 = TokenFinitRegEx(createItemsLR0(AG._Productions['F']),lambda token: token)
a2 = TokenFinitRegEx(createItemsLR0(AG._Productions['T']),lambda token: token)
a3 = TokenFinitRegEx(createItemsLR0(AG._Productions['P']),lambda token: token)
a4 = TokenFinitRegEx(createItemsLR0(AG._Productions['E']),lambda token: token)

automatons = {
    0 : a0,
    1 : a1,
    2 : a2,
    3 : a3,
    4 : a4
}

parser = GrammarParser(automatons,AG)

chain = 'n+(n-n^n)/(n-n/n)'
index = 0

parser.LoadTokens(chain)
parser.Parse()