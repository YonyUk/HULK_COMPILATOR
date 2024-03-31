import HULK_LANGUAGE_DEFINITION as HK

gramar =[


# function_caLL
[
    ["F",[ ["c","P"] , ["c","N" ] , ["c","T"] ] ],
    ["P",[["(","p",")"]]],
    ["T",[["F"]],],
    ["N",[["(",")"]]],
],

# strings
[
    ["T", [ ["T","@","T"]  , ["T","@@","T"] ] ],
    ["E", [["T","@","E"] ,["T","@@","E"] ] ]
],

# expression_block
[
    ["b",[ ["{","}"], [ "b","}" ] , ["O","}"] ] ],
    ["O", [["T",";","E"], ["b"] , ["{","M"], ["{","M"], ["O","E"] , ["O","B"], ["O","M"]]],
    ["B" , [["b",";"]]],
    ["E" , [["T",";"]]],
    ["T",  [["T" ,".","E"], ["T" ,".","T"] ]],
    ["E",  [["T" ,".","E"] ]]
],

# literals
[

["T" , [ ["let","T"] ]],
["p" , [ ["T", "," ,"T" ] , ["p",",","T"] ]],
["T" , [ ["T",":=","T"]  , ["T",":=","T"] , ["T",":=","T"] ]],
["E" , [ ["T",":=","E"] , ["T",":=","E"] ,  ["T",":=","E"] ]],
["T" , [ ["T","=","T"]  ]],
["E" , [  ["T","=","E"] ]],
["T" , [ ["T","as","T"] , ["T","as","E"] ]],
["E" , [ ["T","as","E"] ]],
["T" , [ ["T",":","T"]  ]],
["E" , [ ["T",":","E"] ]],
["E", [["T",";"]]],
["T", [["(","T",")"]]],

],

# booleans
[
    
    ["T" , [["T","&","T"]  , ["T","|","T"]  , ["T","!=","T"] ,
            ["T",">","T"]  , ["T","<","T"]  , ["T","<=","T"] ,
            ["T",">=","T"] , ["T","==","T"] , 
            ["T","is","T"] ]],
    
    ["E" , [["T","&","E"]  , ["T","|","E"]  , ["T","!=","E"] ,
            ["T",">","E"]  , ["T","<","E"]  , ["T","<=","E"] ,
            ["T",">=","E"] , ["T","==","E"] , 
            ["T","is","E"] ]],
],

# numbers
[
    
    ["T" , [["T","+","T"], ["T","-","T"],[ "T","*","T"], ["T","/","T"], ["T","^","T"], ["T","%","T"]]],
    ["E" , [["T","+","E"], ["T","-","E"],[ "T","*","E"], ["T","/","E"], ["T","^","E"], ["T","%","E"]]],
    
    ["T" , [ ["T","-=","T"] ,["T","+=","T"] ,["T","/=","T"] ,["T","*=","T"] , ["T","--"] , ["T","++"] ]],
    ["E" , [ ["T","-=","E"] ,["T","+=","E"] ,["T","/=","E"] ,["T","*=","E"] , ["E","--"] , ["E","++"] ]]
],

# IN
[
    ["T", [["T","in","T"] , ["p","in","T"] , ["p","in","p"]]],
    ["E", [["T","in","E"] , ["p","in","E"] ]],
    ["E", [ ["T","in","b"] , ["T","in","B"]]]
     
],

#  For
[

 ["E" , [["for","T","b"] , ["for","T","B"] , ["for","T","E"]]],
 ["T", [["for","T","T"]]],
 
],

# conditional
[
    
    ["I" , [ ["if","T","T"] , ["I","elif","T","b"] , ["I","elif","T","T"] , ["if","T","b"] ] ],
    ["E", [["I","else","B"] , ["I","else","b"]  ]],          
],

# While
[
    
    ["E" , [["while","T","E"] ,[ "while","T","B"] , ["while","T","b"] ]],
    ["T", [["while","T","T" ]]],
],

# function
[    
 
    ["M" , [ ["function","T","B"] , ["function","T","=>","E"]  ,
            ["function","T","=>","B" ] , ["function","T","b"] , ["function","T","=>","b"] ]]
],

# types
[
    
    ["M ", [["type","T","b"  ], ["type","T","inherits","T","b"] ]],
    ["T" , [ ["new","F"] ]],
],

# protocols
[
    ["M" , [["protocol","c","(",")","b"] ,[ "protocol","T","extends","T","b"] ,[ "protocol","T","B"] ,[ "protocol","T","extends","T","B"]]]
],

# vector
[
    
    ["T" , [[ "[","T","||","T" , "]"] , [ "[" , "p" , "]" ] , ["T" ,"[" , "T" , "]" ]  ]],
]
]

production_token = [
        
        "T",
        "M",
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
        "extends",
        "+=",
        "/=",
        "||",
        "[",
        "]",
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
        "|",
        "@@",
        "-=",
        
    ]

def traslator(token_list):
    
    parse_list=["$1"]
    parse_list.append("$2")
    
    index=0
    while index < len(token_list ):
        
        try:
            
            if token_list[index] == "PI" or token_list[index] == "E"  or float(token_list[index])  :
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
                parse_list.append("c")
            
            else:
                parse_list.append("T")
        index += 1
    
    parse_list.append("$3")
    
    return parse_list