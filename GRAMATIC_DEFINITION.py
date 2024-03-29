import HULK_LANGUAGE_DEFINITION as HK

gramar =[

# function_caLL
[
    ["c",[ "c(p)" , "cT" ] ],
    ["T", ["c"]]
],

# strings
[
    ["T", ["T@T","T@@T"]]
],

# expression_block
[
    ["b",[ "{\}", "b}"]],
    ["O", ["{E", "{b" ,"{B" ,"{M", "{M", "OE" , "OB", "bl ''M","bl ''M"]],
    ["B" , ["b;"]],
    ["E" , ["T;"]],
    ["T",  ["T.T"]]
],

# literals
[

["T" , [ "letT" ]],
["p" , [ "T,T" , "p,T" ]],
["T" , [ "T:=T" , "T:=T" , "T:=T" ]],
["T" , [ "T=T" ]],
["T" , [ "TasT" ]],
["T" , [ "T:T" ]],
["E", ["T;"]],

],

# booleans
[
    
    ["T" , ["T&T" , "T|T" , "T!=T", "T>T" , "T<T" , "T<=T" , "T>=T" , "T==T" , "TisT" ]]
],

# numbers
[
    
    ["T" , ["T '+T", "T-T", "T*T", "T/T", "T^T", "T%T"]],
    ["T" , [ "T-=T" ,"T+=T" ,"T/=T" ,"T*=T" , "T--" , "T++" , "T" ]]
],

# IN
[
    ["T", ["TinT" , "pinT" , "pinp"]],
    ["E", [ "Tinb" , "TinB"]]
     
],

#  For
[

 ["FOR" , ["forTb" , "forTB", "forTE"]],
 ["for", ["forTT"]],
 ["T" , ["for"]]
 
],

# conditional
[
    
    ["I" , [ "ifTT" , "IelifTb" , "IelifTT" , "ifTb" ] ],
    ["If", ["IelseB" , "Ielseb"  ]],      
    ["E" , ["If"]]
    
],

# While
[
    
    ["W" , ["whileTE" , "whileTB" , "whileTb" ]],
    ["w", ["whileTT" ]],
    ["T", ["w"]],
    ["E" , ["W"]]
    
],

# function
[    
 
    ["M" , [ "functionTB" , "functionT=>E"  
            "functionT=>B"  , "functionTb" , "functionT=>b" ]]
],

# types
[
    
    ["M ", ["typeTb"  , "typeTinheritsTb" ]],
    ["T" , [ "newT" ]]
],

# protocols
[
    ["M" , ["protocolTb" , "protocolTextendsTb" , "protocolTB" , "protocolTextendsTB"]]
],

# vector
[
    
    ["T" , ["[T||T]" , "[p]" ]],
    ["T", ["T[T]"]]
]
]

production_token = [
        "p",
        "c",
        "B",
        "b",
        "T",
        "W",
        "w",
        "E",
        "I",
        "If",
        "for",
        "FOR",
        "O",
        "new",
        "function",
        "let",
        "in",
        "protocol",
        "type",
        "while",
        "for",
        "if",
        "else",
        "elif",
        "e",
        "PI",
        "inherits",
        ",",
        ";",
        "=>",
        ":",
        "(",
        ")",
        "{",
        "}",
        ".",
        "!",
        "++",
        "*=",
        "!=",
        "--",
        "is",
        "as",
        "+",
        "-",
        "*",
        "/",
        "^",
        "%",
        "<",
        ">",
        "<=",
        ">=",
        "=",
        "==",
        "@",
        ":=",
        "!",
        "&",
        "|"
    ]

def traslator(token_list):
    
    print(token_list)
    parse_list=["$"]
    index=0
    while index < len(token_list ):
        
        try:
            
            if token_list[index] == "PI" or token_list[index] == "e"  or float(token_list[index])  :
                parse_list.append("T")
                index += 1
                continue
        
        except:
            pass
        
        if token_list[index] =="'" or token_list[index] == "\"" : 
            
            index1 = index + 1
            while index1 < len(token_list):
                
                if token_list[index1] == "'" or token_list[index1] == "\"" :
                    parse_list.append("T")
                    index = index1
                    index += 1
                    break
                
                index1 +=1
                    
        kw = False                    
        for arg in HK.SYMBOLS_and_OPERATORS_parser:            
            
            if token_list[index] == arg:
            
                parse_list.append(token_list[index])
                kw =True
                break
            
        if not kw:
            if index + 1 < len(token_list) and token_list[index + 1 ] == "(" :
                parse_list.append("name")
            
            else:
                parse_list.append("T")
        index += 1
    
    parse_list.append("$")
    return parse_list
