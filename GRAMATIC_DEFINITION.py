import HULK_LANGUAGE_DEFINITION as HK

function_caLL={
    
    "P '" : ["Z ''(E '" ,  "P 'E '" , "Z ''(L '''" ,  "P 'L '''" , "Z ''(F" , "P 'F" ],
    "P ''" :[ "P ')" , "Z ''(E ')" , "Z ''(F)" , "Z ''(L ''')" , "P 'E ' )" , "P 'L ''')"  , "P 'F)" , "(P '')"]
    
}
strings={
    
    "G1" : [ "L ''" , "N '" , "P ''" , "S '", "T '"],
    "S '": ["G1 '@G1 ' ","G1 '@@G1 ' ","(S ')"],
}
expression_block = {
    
    "E '" : ["S '","N '", "P ''" , "B '", "L ''","V '", "D '" ,"X '","(E ')", "T '" , "K" , "G '" , "G1 '" , "W '" ],
    "bl '":[ "{ }", "bl ''}"],
    "bl ''": ["{E", "{bl '" ,"{bl" ,"{F", "{C", "bl ''E" , "bl ''bl", "bl ''F","bl ''C"],
    "bl" : ["bl ';"],
    "E" : ["E;"],
    "T '":  ["E '.P ''" , "S '.P ''" , "N '.P ''" , "P ''.P ''" , "B '.P ''" , "L ''.P ''" ,
             "V '.P ''" , "D '.P ''" , "X '.P ''" , "T '.P ''" , "K.P ''" , "G '.P ''" , "G1 '.P ''" ,
             "W '.P ''", "E '.L ''" , "S '.L ''" , "N '.L ''" , "L ''.L ''" , "B '.L ''" , "L ''.L ''" ,
             "V '.L ''" , "D '.L ''" , "X '.L ''" , "T '.L ''" , "K.L ''" , "G '.L ''" , "G1 '.L ''" , "W '.L ''" ]

}
literals={
    
"D '" : [ "letE0" ],
"D ''" : [ "E ',E0" , "E ',E '" , "D '',E0" , "D '',E '"],
"E '" : [ "L '':=E '" , "L ''' := E '" , "D ':=E '" ],
"E0" : [ "L ''=E '",  "L '''=E '" ],
"D" : [ "D ';" ],
"L ''" : [ "(L '')" , "L ''asL ''" ],
"L '''" : [ "L '':L ''" ],
   
}

booleans = {
    
    "K" : ["B '" , "L ''" , "P ''" , "L '" , "X '", "T '"],
    "G '" : ["L ''" , "N '" , "P ''" , "X '" , "T '"],
    "B '" : ["K&K" , "K||K" , "E '!=E '", "G '>G '" , "G '<G '" ,
             "G '<=G '" , "G '>=G '" , "E '==E '" , "E 'isE '" , "(B ')" ,"B ';",
             "K$B '" , "B '$K" , "K|B '" , "B '|K",
             ],

}

numbers = {
    
    "G '" : ["L ''" , "N '" , "P ''" ,  "X '" , "T '"  ,"PI" , "e" ,"G '+G '", "G '-G '", "G '*G '", "G '/G '", "G '^G '", "G '%G '", "(G ')"],
    "N '" : [ "L '-=G '" ,"L '+=G '" ,"L '/=G '" ,"L '*=G '" , "G '--" , "G '++" , "G '" ]
}

IN = {
    "E '": ["E 'inE '",  "D ''inbl '"],
    "E": [ "D ''inbl '" , "E 'inbl " , "E 'inE , D ''inE " ]
     
}
FOR = {
 "for" : ["for(L ''inE ')bl '" , "for(L ''inE ')E '" , "for(L ''inE ')bl", "for(L ''inE ')E"],
 "E" : ["for"],
 "E '" : ["for '"]

} 
conditional = {
    
    "K" : [ "L '' ","P ''", "X '" ,"T '" ],
    "I" : [ "if(K)E '" , "if(B ')E '" , "Ielif(K)bl" , "Ielif(K)E '", 
           "Ielif(B ')bl" , "Ielif(B ')E '" , "if(K)bl '" ] ,
    "If": ["Ielsebl" , "IelseE" , "if(B ')E" , "if(K)E" ],      
    "E'": ["IelseE '"],
    "E" : ["If"]
    
}
While = {
    
    "W" : ["while(K)E" , "while(B ')E" , "while(K)bl" , "while(B ')bl" ,
           "while(K)bl '" , "while(B ')bl '"],
    "W '": ["while(K)E '" , "while(B ')E '" ],
    "E" : ["W"]
    
}
function = {    
 
    "F" : [ "functionP ''bl" , "functionP '':L ''bl" , "functionP ''=>E" , 
           "functionP '':L ''=>E" , "functionP ''=>bl" , "functionP '':L ''=>bl"  ,
           "functionP ''bl '" , "functionP '':L ''bl '" , "functionP ''=>E" , 
           "functionP '':L ''=>E" , "functionP ''=>bl '" ,  "functionP '':L ''=>bl '" ]
}
types = {
    
    "C ": ["typeL ''bl '" , "typeP ''bl '" , "typeL ''inheritsL ''bl '" ,
           "typeP ''inheritsL ''bl '" , "typeL ''inheritsP ''bl '" , "typeP ''inheritsP ''bl '" ],
    "E '" : [ "newP ''" ]
    
}
special_block = {
    
    "bls '" : ["{P '':L '';" , "bls 'P '':L '';"],
    "bls" : ["bl 's}"]
    
}
protocols = {
 
    "Q" : ["protocolL ''bls" , "protocolL ''extendsL ''bls"]
}
vector ={
    "V '" : ["[E '||E 'inE ']" ,  "V '']"],
    "V ''" : [ "[E '," , "V ''E ',"] ,
    "X '": ["L ''[E ']"]
}

def traslator(token_list):
    
    print(token_list)
    parse_list=[]
    index=0
    while index < len(token_list ):
        
        try:
            
            if token_list[index] == "PI" or token_list[index] == "e"  or float(token_list[index])  :
                parse_list.append("N '")
                index += 1
                continue
        
        except:
            pass
        
        if token_list[index] =="'" or token_list[index] == "\"" : 
            
            index1 = index + 1
            while index1 < len(token_list):
                
                if token_list[index1] == "'" or token_list[index1] == "\"" :
                    parse_list.append("S '")
                    index = index1
                    index += 1
                    break
                
                index1 +=1
                    
        kw = False                    
        for arg in HK.SYMBOLS_and_OPERATORS_parser:            
            
            if token_list[index] == arg:
                
                if arg == 'is':
                
                    parse_list.append("~")                    
                    parse_list.append(token_list[index])
                    kw =True
                    break
                
                if arg == "==":
                    parse_list.append(token_list[index])
                    parse_list.append("#")                    
                    kw =True
                    break
                
                parse_list.append(token_list[index])
                kw =True
                break
            
        if not kw:
            if index + 1 < len(token_list) and token_list[index + 1 ] == "(" :
                parse_list.append("Z ''")
            
            else:
                parse_list.append("L ''")
        index += 1
    
    parse_list.append("$")
    return parse_list
