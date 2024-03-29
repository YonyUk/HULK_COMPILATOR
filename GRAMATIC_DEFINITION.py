import HULK_LANGUAGE_DEFINITION as HK

gramar =[

# function_caLL
[
    ["c",[ ["c","(","p",")"] , ["c","(","T",")" ] ] ],
    ["T", [["c"]]]
],

# strings
[
    ["T", [["T","@","T"],["T","@@","T"]]]
],

# expression_block
[
    ["b",[ ["{","}"], [ "b","}" ] ] ],
    ["O", [["{","E"], ["{","b"] ,["{","B"] ,["{","M"], ["{","M"], ["O","E"] , ["O","B"], ["O","M"]]],
    ["B" , [["b",";"]]],
    ["E" , [["T",";"]]],
    ["T",  [["T" ,".","T"]]]
],

# literals
[

["T" , [ ["let","T"] ]],
["p" , [ ["T", "," ,"T" ] , ["p",",","T"] ]],
["T" , [ ["T",":=","T"] , ["T",":=","T"] , ["T",":=","T"] ]],
["T" , [ ["T","=","T"] ]],
["T" , [ ["T","as","T"] ]],
["T" , [ ["T",":","T"] ]],
["E", [["T",";"]]],

],

# booleans
[
    
    ["T" , [["T","&","T"] , ["T","|","T"] , ["T","!=","T"], ["T",">","T"] , ["T","<","T"] , ["T","<=","T"] , ["T",">=","T"] , ["T","==","T"] , ["T","is","T"] ]]
],

# numbers
[
    
    ["T" , [["T","+","T"], ["T","-","T"],[ "T","*","T"], ["T","/","T"], ["T","^","T"], ["T","%","T"]]],
    ["T" , [ ["T","-=","T"] ,["T","+=","T"] ,["T","/=","T"] ,["T","*=","T"] , ["T","--"] , ["T","++"] ]]
],

# IN
[
    ["T", [["T","in","T"] , ["p","in","T"] , ["p","in","p"]]],
    ["E", [ ["T","in","b"] , ["T","in","B"]]]
     
],

#  For
[

 ["FOR" , [["for","T","b"] , ["for","T","B"], ["for","T","E"]]],
 ["for", [["for","T","T"]]],
 ["T" , [["for"]]]
 
],

# conditional
[
    
    ["I" , [ ["ifTT"] , ["I","elif","T","b"] , ["I","elif","T","T"] , ["if","T","b"] ] ],
    ["If", [["I","else","B"] , ["I","else","b"]  ]],      
    ["E" , [["If"]]]
    
],

# While
[
    
    ["W" , [["while","T","E"] ,[ "while","T","B"] , ["while","T","b"] ]],
    ["w", [["while","T","T" ]]],
    ["T", [["w"]]],
    ["E" , [["W"]]]
    
],

# function
[    
 
    ["M" , [ ["function","T","B"] , ["function","T","=>","E"]  
            ["function","T","=>","B" ] , ["function","T","b"] , ["function","T","=>","b"] ]]
],

# types
[
    
    ["M ", [["type","T","b"  ], ["type","T","inherits","T","b"] ]],
    ["T" , [ ["new","T"] ]]
],

# protocols
[
    ["M" , [["protocol","T","b"] ,[ "protocol","T","extends","T","b"] ,[ "protocol","T","B"] ,[ "protocol","T","extends","T","B"]]]
],

# vector
[
    
    ["T" , [[ "[","T","||","T" , "]"] , [ " [ " , " p " , " ] " ]  ]],
    ["T", [ [" T" ,"[" , "T" , "]" ]] ]
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
    parse_list=["$1"]
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
                parse_list.append("c")
            
            else:
                parse_list.append("T")
        index += 1
    
    parse_list.append("$2")
    return parse_list
