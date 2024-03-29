# Given tokens
production_token = [
   "M", "p", "c", "B", "b", "T", "W", "w", "E", "I", "If", "for", "FOR", "O", "new", "function", "let", "in", "protocol", "type", "while", "for", "if", "else", "elif", "e", "PI", "inherits", ",", ";", "=>", ":", "(", ")", "{", "}", ".", "!", "++", "*=", "!=", "--", "is", "as", "+", "-", "*", "/", "^", "%", "<", ">", "<=", ">=", "=", "==", "@", ":=", "!", "&", "|"
]

# List of lists to tokenize
data = [    
 
    ["M" , [ "functionTB" , "functionT=>E"  
            "functionT=>B"  , "functionTb" , "functionT=>b" ]]
]

# Function to tokenize a single string
def tokenize_string(s):
    for token in production_token:
        if token in s:
            return token
    return s # Return the original string if no token is found

# Function to tokenize a list of strings
def tokenize_list(lst):
    return [tokenize_string(s) for s in lst]

# Tokenizing the entire data structure


list_tokeniced=[]
for sub_list in data:
    
    for string in sub_list[1]:
        
        s=""
        for index,char in enumerate(string,start=0):
            
            if production_token.__contains__(char) and  index + 1 < len(string) and production_token.__contains__(production_token[index + 1]):
                
                list_tokeniced.append(s)
                s=""
                list_tokeniced.append(production_token[index] + production_token[index + 1] )                
            
            elif production_token.__contains__(char):
                
                list_tokeniced.append(s)
                s=""
                list_tokeniced.append(production_token[index] )                
                
            else:
                
                s+=production_token[index]
                
print(list_tokeniced)