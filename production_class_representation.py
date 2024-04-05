import importing_file as impF

class function_call( impF.dt.ASTNode):
            
    def __init__( self, token_list ):
        
        self.set_identifier('FunctionCall')
        self.name = token_list[0]
        self.args = token_list[1]
        
        pass
    
class function_name(impF.dt.ASTNode):
        
        def __init__(self,token_list):

            self.set_identifier("function_name")
            self.name = token_list[0]
    
            pass
            
        pass

class params( impF.dt.ASTNode):
    
    def __init__(self,token_list):
        
        self.set_identifier('params')
        self.param = token_list[1]
        
        pass    
    pass

class binary_expression:
    
    def __init__(self,token_list):
        
        binary_expresion =[ ('+',self.plus(token_list)) , ('-', self.minus(token_list)) ,
                            ('*', self.multiplication(token_list)) ,('/', self.divition(token_list)) ,
                            ('^', self._pow(token_list)),('**', self._pow(token_list)),
                            ('%', self.per_cent(token_list)),('@', self.concatenation(token_list)),
                            ('@@', self.blank_space_concatenation(token_list), (':',self.double_dot(token_list))),
                            (':=', self.double_dot_equal(token_list), ('as',self.as_(token_list))),
                            ('is', self.is_(token_list), ('==',self.equal(token_list))),
                            ('>', self.bigger_than(token_list), ('<',self.smaller_than(token_list))),
                            ('>=', self.bigger_or_equal(token_list), ('<=',self.smaller_or_equal(token_list))),
                            ('=', self.assign(token_list), ('|',self.or_(token_list))),
                            ('&', self.and_(token_list), ('!=',self.different(token_list))),
                            ('/=', self.divide_and_assign(token_list), ('*=',self.multiply_and_assign(token_list))),
                            ('+=', self.plus_and_assign(token_list), ('-=',self.minus_and_assign(token_list))), ]
        
        for item in binary_expresion:
        
            if item[0] == token_list[1]:
    
                return item[1]
    
    
    class plus(impF.dt.ASTNode):
            
            def __init__(self,token_list):
              
                self.set_identifier('+')
                self.left = token_list[0]
                self.right = token_list[2]
                
            pass
        
    class minus(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class multiplication(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class divition(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class _pow(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('^')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class per_cent(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('%')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class concatenation(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
    class blank_space_concatenation(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('@@')
            self.left = token_list[0]
            self.right = token_list[2]

        pass
    
   
   
    class double_dot(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class double_dot_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier(':=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class as_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('as')
            self.left = token_list[0]
            self.right = token_list[2]
            
        pass
    
    class is_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('is')
            self.left = token_list[0]
            self.right = token_list[2]
            
        pass
    
    class equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('==')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class bigger_than(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class smaller_than(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class bigger_or_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('>=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class smaller_or_equal(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('<=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class or_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('|')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class and_(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('&')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class different(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('!=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class divide_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('/=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class multiply_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('*=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class plus_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('+=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
    class minus_and_assign(impF.dt.ASTNode):
        
        def __init__(self,token_list):
            
            self.set_identifier('-=')
            self.left = token_list[0]
            self.right = token_list[2]
        
        pass
    
class unary_expression:
    
    def __init__(self,token_list):
        
        
        pass
    
    