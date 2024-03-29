import HULK_LANGUAGE_DEFINITION as HK

function_caLL={
        
    "call" :[ "name(param)"],
    "E '": ["call"]
}

strings={
    
    "E '": ["E '@E '","E '@@E '"],
}

expression_block = {
    
    "bl '":[ "{ }", "bl ''}"],
    "bl ''": ["{E", "{bl '" ,"{bl" ,"{tf", "{tf", "bl ''E" , "bl ''bl", "bl ''tf","bl ''tf"],
    "bl" : ["bl ';"],
    "E" : ["E;"],
    "E '":  ["E '.E '"]
}

literals={

"E '" : [ "letE '" ],
"param" : [ "E ',E '" , "param,E '" ],
"E '" : [ "E ':=E '" , "E ' := E '" , "E ':=E '" ],
"E '" : [ "E '=E '" ],
"E '" : [ "E 'asE '" ],
"E '" : [ "E ':E '" ],
"E": ["E ';"],

}

booleans = {
    
    "E '" : ["E&E" , "E|E" , "E '!=E '", "E '>E '" , "E '<E '" ,
             "E '<=E '" , "E '>=E '" , "E '==E '" , "E 'isE '"
             ],
}

numbers = {
    
    "E '" : ["E ' '+E '", "E '-E '", "E '*E '", "E '/E '", "E '^E '", "E '%G '"],
    "E '" : [ "E '-=E '" ,"E '+=E '" ,"E '/=E '" ,"E '*=E '" , "E '--" , "E '++" , "E '" ]
}

IN = {
    "E '": ["E 'inE '" , "paraminE '" , "paraminparam"],
    "E": [ "E 'inbl '" , "E 'inbl"]
     
}
FOR = {
 "for" : ["for(E ')bl '" , "for(E ')bl", "for(E ')E"],
 "E" : ["for"],
 "for '": ["for(E ')E '"],
 "E '" : ["for '"]

} 
conditional = {
    
    "I" : [ "if(E ')E '" , "Ielif(E ')bl '" , "Ielif(E ')E '" , "if(E ')bl '" ] ,
    "If": ["Ielsebl" , "Ielsebl '"  ],      
    "E" : ["If"]
    
}
While = {
    
    "W" : ["while(E ')E" , "while(E ')bl" , "while(E ')bl '" ],
    "W '": ["while(E ')E '" ],
    "E '": ["W '"],
    "E" : ["W"]
    
}
function = {    
 
    "tf" : [ "functionE 'bl" , "functionE '=>E" , 
            "functionE '=>bl"  , "functionE 'bl '" , "functionE '=>bl '" ]
}
types = {
    
    "tf ": ["typeE 'bl '"  , "typeE 'inheritsE 'bl '" ],
    "E '" : [ "newE '" ]
}
protocols = {
    "tf" : ["protocolE 'bl '" , "protocolE 'extendsE 'bl '" , "protocolE 'bl" , "protocolE 'extendsE 'bl"]
}

vector ={
    
    "E '" : ["[E '||E ']" , "[params]" ],
    "E '": ["E '[E ']"]
}

def traslator(token_list):
    
    print(token_list)
    parse_list=[]
    index=0
    while index < len(token_list ):
        
        try:
            
            if token_list[index] == "PI" or token_list[index] == "e"  or float(token_list[index])  :
                parse_list.append("V")
                index += 1
                continue
        
        except:
            pass
        
        if token_list[index] =="'" or token_list[index] == "\"" : 
            
            index1 = index + 1
            while index1 < len(token_list):
                
                if token_list[index1] == "'" or token_list[index1] == "\"" :
                    parse_list.append("V")
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
                parse_list.append("Z ''")
            
            else:
                parse_list.append("V")
        index += 1
    
    parse_list.append("$")
    return parse_list
