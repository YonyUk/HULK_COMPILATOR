
`NOTES:`

    P is an in-Line caLL , P '' is expression part caLL and P ' is an about to build function call , that derives in P or P '' , L ' is variable in brackets ( L '' ) where L '' is the variable , S ' is string , N ' is number , B ' is boolean , V ' is vector


## Function caLL:
 
* `P '` -> L '' ( E ' , $|$ P ' E ' ,
* `P '` -> L '' ( L ''' , $|$ P ' L ''' ,
* `P '` -> L '' ( F  $|$ P ' F ,
* `P '` -> L '' ( C  $|$ P ' C  ,
* `P ''` -> P ' )
* `P ''` -> P '' 
* `P ''` -> ( P '' )
* `P` -> P '' ;

## Strings

By default every non-token element is taken to `S '` if it is a word like inside quotation marks , `""`

* `S '` -> E ' @ E ' 
* `S '` -> E ' @@ E ' 
* `S '` -> ( S ' )
* `S` -> S ' ;

## Expression block

* `E '` -> S ' $|$ N ' $|$ P '' $|$ B ' $|$ L ' $|$ L '' $|$ V ' $|$ D ' $|$ X '
* `bl '` -> { }
* `bl ''` -> { E $|$ { bl ' $|$ { bl $|$ {F $|$ {C   
* `bl ''` -> bl '' E $|$ bl '' bl $|$ bl '' F $|$ bl '' C    
* `bl '` -> bl '' }
* `bl` -> bl ';
* `E '` -> ( E ' )
* `E`  -> E ;

## Literals:

By default every non-token element is taken to `L ''` if it is a word like

* `D '` -> ( D ' )
* `D '` -> let E0
* `E '` -> L '' := E ' $|$ L ''' := E ' $|$ L ''' := E '
* `E0` -> L '' = E ' $|$ L ''' = E '
* `D` -> D '; 
* `L '` -> ( L '' ) 
* `L '''` -> L '' : L '' // let x: Number = 42;
* `E '` -> L ''

## Booleans

* `K` -> B ' $|$ L '' $|$ P '' $|$ L ' $|$ X '
* `G` -> L '' $|$ L ' $|$ N ' $|$ P '' $|$ X '
* `B '` -> K & K
* `B '` -> K || K
* `B '` -> E ' != E ' 
* `B '` ->  G > G $|$ G < G
* `B '` ->  G >= G $|$ G <= G
* `B '` -> E ' == E ' 
* `B '` ->  E ' is E '
* `B '` -> ( B ' )
* `B` -> B ' ; 

## Numbers:

By default every non-token element is taken to `N '` if it is a number like.

* `G '` -> L '' $|$ L ' $|$ N ' $|$ P '' $|$ X '
* `G '` -> PI
* `G '` -> e 

### Operators

* `G '` -> G ' +  G '
* `G '` -> G ' -  G '
* `G '` -> G ' *  G '
* `G '` -> G ' /  G '
* `G '` -> G ' ^  G '
* `G '` -> G ' %  G '
* `G '` -> ( G ' )

### No operator , but numbers

* `N '` -> L ' -= G '
* `N '` -> L ' += G '
* `N '` -> L ' /= G '
* `N '` -> L ' *= G '
* `N '` -> G ' --
* `N '` -> G ' ++
* `N '` -> G '
* `N` -> G ' ; 

## in

* `E '` -> D ' in E ' $|$ D ' in bl ' 
* `E` -> D ' in bl $|$ D ' in E

## for

* `E '` -> for( L '' in E ' ) bl '
* `E` -> for( L '' in E ' ) bl
* `E` -> for( L '' in E ' ) E

##  Conditional

* `K` -> B ' $|$ L '' $|$ P '' $|$ L ' $|$ X '
* `I` -> if ( K ) E
* `I` -> if ( K ) bl
* `If` -> I else bl $|$ I else E
* `I` -> I elif ( K ) bl $|$ I  elif ( K ) E
* `E` -> If

## while

* `K` -> B ' $|$ L '' $|$ P '' $|$ L ' $|$ X '
* `W`-> while( K ) E
* `W`-> while( K ) bl
* `W '` -> while( K ) bl '

## function

* `F` -> function P '' bl $|$ function P '' : L '' bl
* `F` -> function P '' => E $|$ function P '' : L '' => E
* `F` -> function P '' => bl $|$ $|$ function P '' : L '' => bl  // case : function tan(x: Number): Number => sin(x) / cos(x);
  
## Types

* `C`-> type L '' bl '
* `C`-> type P '' bl ' 
* `C`-> type L '' inherits L '' bl '
* `C`-> type P '' inherits L '' bl '
* `C`-> type L '' inherits P '' bl '
* `C`-> type P '' inherits P '' bl '
* `E '` -> new P ''

## Special block

* `bls '` -> { P '' : L ''; $|$ bls ' P '' : L '';
* `bls ` -> bl 's }

## Protocols

* `Q` -> protocol L '' bls $|$ protocol L '' extends L '' bls

## Vector

* `V '` -> [ E ' || L '' in E ' ]
* `V ''` -> [ E ' , $|$ V '' E ' ,
* `V '` -> V '' ]
* X '-> L ''[ E ']

# Procedencia

 * Arithmetic Operations
 * Comparison Operations
 * Logical Operations
 * Assignment Operations
 * Control Flow Operations
 * If-else statements
 * Loops (for, while, do-while)
 * Switch-case statements (in some languages)
 * Function Calls
 * Array and List Operations
 * String Operations
 * Object and Class Operations
 * Accessing properties (object.property)
 * Method calls (object.method())
 * Type Conversion


# Strategy

    Shift: ++ , --
    Shift: -+
    Reduce: -+

n + n * * n * n ^ n ^ n - n * n ^ n
