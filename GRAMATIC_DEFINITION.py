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
    ["T", [ ["T","@","T"] ,["F","@","T"], ["T","@@","T"] , ["F","@@","T"]] ],
    ["E", [["T","@","E"] ,["F","@","E"],["T","@@","E"] , ["F","@@","E"] ] ]
],

# expression_block
[
    ["O",[["E","E"], ["T","$2","O"] ,["O","E"],["O","B"],["O","$2","b"]]],
    ["O",[["O","$2","T"],["O","$2"] , ["O",";"],["E","$2","E"],["b","$2","b"]]],
    ["b",[["{","O","}"],["{","E","}"],["{","B","}"],["{","}"],["b","$2"],["{","b","}"]]],
    ["B",[["b",";","$2"]]],
    ["T",[["T","$2"]]],
    ["E",[["E","$2"],["B"]]],
    ["E",[["$2",";","$2"],["E",";"]]],
    
    # ["O", [["E","O"] , ["{","M"], ["{","M"], ["O","E"] , ["O","B"], ["O","M"]]],
    
    ["E" , [["T",";"]]],
    ["T",  [["T" ,".","E"] , ["F" ,".","E"], ["T" ,".","T"] , ["F" ,".","T"] ]],
    ["E",  [["T" ,".","E"] ]]
],

# literals
[

["T" , [ ["let","T"] ]],
["p" , [ ["T", "," ,"T" ] , ["T",",","p"] ]],
["T" , [ ["T",":=","T"] ]],
["E" , [ ["T",":=","E"] ]],
["T" , [ ["T","=","T"]  ]],
["E" , [  ["T","=","E"] ]],
["T" , [ ["T","as","T"] , ["F","as","T"] , ["T","as","E"] ]],
["E" , [ ["T","as","E"] ]],
["T" , [ ["T",":","T"] , ["F",":","T"]  ]],
["E" , [ ["T",":","E"] ]],
["E", [["T",";","$2"]]],
["T", [["(","T",")"]]],

],

# booleans
[
    
    ["T" , [["T","&","T"] , ["F","&","T"] , ["T","|","T"] , ["F","|","T"]  , ["T","!=","T"] , ["F","!=","T"] , 
            ["T",">","T"] , ["F",">","T"]  , ["T","<","T"] , ["F","<","T"]  , ["T","<=","T"] , ["F","<=","T"] ,
            ["T",">=","T"] ,["F",">=","T"] , ["T","==","T"] ,["F","==","T"] , 
            ["T","is","T"] , ["F","is","T"] ]],
    
    ["E" , [["T","&","E"]  , ["T","|","E"]  , ["T","!=","E"] ,
            ["T",">","E"]  , ["T","<","E"]  , ["T","<=","E"] ,
            ["T",">=","E"] , ["T","==","E"] , 
            ["T","is","E"] ]],
],

# numbers
[
    
    ["T" , [["T","+","T"] , ["T","-","T"],[ "T","*","T"], ["T","/","T"], ["T","^","T"], ["T","%","T"]]],
    ["T" , [["F","+","T"] , ["F","-","T"],[ "F","*","T"], ["F","/","T"], ["F","^","T"], ["F","%","T"]]],
    ["E" , [["T","+","E"], ["F"+"E"],["T","-","E"],[ "T","*","E"], ["T","/","E"], ["T","^","E"], ["T","%","E"]]],
    
    ["T" , [ ["T","-=","T"] ,["T","+=","T"] ,["T","/=","T"] ,["T","*=","T"] , ["T","--"] , ["F","--"] , ["T","++"] ,["F","++"] ]],
    ["E" , [ ["T","-=","E"] ,["T","+=","E"] ,["T","/=","E"] ,["T","*=","E"] , ["E","--"] , ["E","++"] ]]
],

# IN
[
    ["T", [["T","in","T"] , ["p","in","T"] , ["p","in","p"]]],
    ["T", [["F","in","T"]]],
    ["E", [["T","in","E"] , ["p","in","E"] ]],
    ["E", [ ["F","in","b"] , ["F","in","B"]]]
     
],

#  For
[
    ["E" , [["for","T","$2","B"] , ["for","T","$2","E"]]],
    ["E", [ ["for","T","$2","b"]]],
    
],

# conditional
[
    
    ["if",[["if","T","$2","E"],["if","T","$2","b"],["if","T","$2","B"],["if","$2"]]],
    ["elif",[["if","elif","T","E"],["if","elif","T","b"],["if","elif","T","B"],["elif","$2"]]],
    ["E",[["if","else","E"],["if","else","b"],["if","else","B"]]],
    ["E",[["elif","else","E"],["elif","else","b"],["elif","else","B"]]],
    ["E",[["if","else","E"],["if","else","b"],["if","else","B"]]],
    
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
    ["M" , [["protocol","F","b"] ,[ "protocol","T","extends","T","b"] ,[ "protocol","T","B"] ,[ "protocol","T","extends","T","B"]]]
],

# vector
[
    
    ["T" , [[ "[","T","||","T" , "]"] , [ "[" , "p" , "]" ] , ["[" , "T" , "]" ]  ]],
]
]

def traslator(token_list):
    
    parse_list=["$1"]
    parse_list.append("$2")
    
    index=0
    while index < len(token_list ):
        
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
                
                if arg == ";" or arg == ")" or arg == "}" or arg == "]":
                    parse_list.append("$2")
                    
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
