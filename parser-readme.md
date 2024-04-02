
# HULK PROGRAMMING LANGUAGE




# Function caLL

- $F -> cP | cN | cT$
- $P -> ( p )$
- $T -> F$
- $N ->( )$

# Strings

- $T -> T@T | F@T | T@@T | F@@T$
- $E -> T@E | F@E | T@@E | F@@E$


# Expression_block

- $O -> EE | O\$2O | T\$2 O | OE | OB | O \$2 b | b \$2 E | ME | EM | OM | MO | OQ | Q \$2$
- $O -> E \$2 M | M \$2 O$
- $O -> O \$2 E | E \$2 b  | E \$2 O | O \$2 | O; | E \$2 E | b \$2 b | O \$2 M$
- $b -> { O } | { E } | { B } | { } | b \$2 | { b } | { T }$
- $B -> b;$
- $T -> T \$2$
- $E -> E \$2 | B$
- $E -> \$2 ; \$3 | E;$
- $b -> { M }$
- $E -> T;$
- $T -> T.E | F.E | T.T | F.T |$
- $E -> T.E$

# Literals

- $T -> let T | T:T$
- $E -> letE | T:E$
- $p -> T \$2 T | T \$2 p$
- $T -> T:=T$
- $E -> T:=E$
- $T -> T=T$
- $E -> T=E$
- $T -> T as T | F as T | T as E$
- $E -> T as E$
- $E -> T;\$2$
- $T -> ( T )$

# booleans

    
    [T , [[T,&,T] , [F,&,T] , [T,|,T] , [F,|,T]  , [T,!=,T] , [F,!=,T] , 
            [T,>,T] , [F,>,T]  , [T,<,T] , [F,<,T]  , [T,<=,T] , [F,<=,T] ,
            [T,>=,T] ,[F,>=,T] , [T,==,T] ,[F,==,T] , 
            [T,is,T] , [F,is,T] ]],
    
    [E , [[T,&,E]  , [T,|,E]  , [T,!=,E] ,
            [T,>,E]  , [T,<,E]  , [T,<=,E] ,
            [T,>=,E] , [T,==,E] , 
            [T,is,E] ]],

# numbers

    [T , [[T,+,T] , [T,+,T] , [T,-,T],[ T,*,T], [T,/,T],[T,/,T], [T,^,T], [T,%,T],[T,**,T]]],
    [T , [[T,$2,+,T] , [T,$2,+,T] , [T,$2,-,T],[ T,$2,*,T], [T,$2,/,T],[T,$2,/,T], [T,$2,^,T], [T,$2,%,T],[T,$2,**,T]]],
    [E , [[T,$2,+,E] , [T,$2,+,E] , [T,$2,-,E],[ T,$2,*,E], [T,$2,/,E],[T,$2,/,E], [T,$2,^,E], [T,$2,%,E],[T,$2,**,E]]],
    [E , [[T,+,E], [F+E],[T,-,E],[ T,*,E], [T,/,E],[T,/,E], [T,^,E], [T,E]],
    
    [T , [ [T,-=,T] ,[T,+=,T] ,[T,/=,T] ,[T,*=,T] , [T,--]  , [T,++]]],
    [E , [ [T,-=,E] ,[T,+=,E] ,[T,/=,E] ,[T,*=,E] , [E,--] , [E,++] ],[E,**],[E,**,E]]],


# IN

    [p,[[p,$2]]],
    [T, [[T,in,T] ,[T,$2,in,T],[p,$2,in,T],[p,$2,in,p], [p,in,T] , [p,in,p]]],
    [T, [[T,$2]]],
    [E, [[T,in,E], [T,$2,in,E] ,[T,in,b],[T,$2,in,b] ,[p,$2,in,E] ,[p,in,E],[p,in,b],[p,$2,in,b]]],
       

#  For

    [E , [[for,T,$2,B] , [for,T,$2,E], [for,T,E]]],
    [E, [ [for,T,$2,b]]],
    

# conditional

    [if,[[if,T,$2,E],[if,T,$2,b],[if,T,$2,B],[if,$2],[if, T, $2, T,]]],
    
    [elif,[[if,elif,T,$2,E],[if,elif,T,$2,b],[if,elif,T,$2,B],[elif,$2],[if,elif, T, $2, T,]]],
    
    [E,[[if,else,E],[if,else,b],[if,else,B]]],
    
    [E,[[elif,else,E],[elif,else,b],[elif,else,B]]],
    
    [T,[[elif,else,T],[if, else, T]]],
    

# While

    
    [E , [[while,T,$2,B] , [while,T,$2,E],[while,T,E]]],
    [E, [ [while,T,$2,b]]],


# function

 
- $M -> function \space T \space \$2 \space => \space \$2 \space E \space$ 
- $M -> function \space T \space \$2 \space : \space T \space => \space \$2 \space E \space$ 
- $M -> function \space T \space \$2 \space => \space \$2 \space b \space$ 
- $M -> function \space T \space \$2 \space : \space T \space => \space \$2 \space b \space$ 
- $M -> function \space T \space \$2 \space : \space T \space b \space$ 
- $M -> function \space T \space \$2 \space b \space$
- $M -> function \space T \space E \space$
- $M -> function \space T \space => \space \$2 \space E \space$
- $M -> T \space \$2 \space : \space Q \space$ 
- $M -> T \space \$2 \space : \space E \space$ 
- $M -> T \space \$2 \space : \space T \space b \space$
- $M -> function \space T \space \$2 \space : \space Q$
- $Q -> T \space => \$2 \space E$
 - $M -> M \space \$2 \space | \space M \space \$2 \space M \space | \space M; | \space M M$

# types

- $M -> \space type \space T \space \$2 \space b \space | \space type \space T \space \$2 \space inherits \space T \space \$2 \space b | \space type \space T \space b \space | \space type \space T \space inherits \space T \space b$

- $T -> \space new \space F \space$


# protocols

- $M -> protocol \space T \space \$2 \space b$
- $M -> protocol \space T \space \$2 \space extends \space T \space \$2 \space b$
- $M -> protocol \space T \space b$
- $M -> protocol \space T \space extends \space T \space b$

# vector

- $T -> [T||T] \space | \space [p] | \space T[T]$


# Procedence

 * Arithmetic Operations
 * Comparison Operations
 * Logical Operations
 * Assignment Operations
 * Control Flow Operations
 * Function Calls
 * Array and List Operations
 * String Operations
 * Object and Class Operations
 * Accessing properties (object.property)
 * Type Conversion




# Reduction Strategy -> GRADIENT PARSER


  This parser tries to model operator procedence using a grammar of the for $<G,P>$ where in $G$ exist pairs of the form $X-> Y$ where $X$ is non-terminal and $Y$ is a sentence . In $P$ if $\alpha\in P$ and $\beta\in P$ , such that $\aleph>\beta$ or $\beta<\alpha$ is the procedece of each operator.


## Strategy

    Shift: ++ , --
    Shift: -+
    Reduce: -+

if an `operator procedence` is that $\alpha>\beta$ for some $\alpha$ and $\beta$ then in string of the form $W \alpha W \beta W$ we reduce to $\alpha$ once we compare procedence between $\alpha$ and $\beta$ , if the case where oposite , $\alpha<\beta$ or $\alpha=\beta$ , we shift to next `token`

e.j : let x := y + 4;

The token are `let` , `x` , `:=` , `y` , `+` , `4` , `;` if the operator precedence is 

- `+`
- `:=`
- `;`
- `$`

GRAMMAR :

- $S -> \$E\$$
- $E -> let  E$
- $E -> T := E$
- $E -> T := E$ 
- $E -> T + E$


we build the string in a default form `$` `let` `x` `:=` `y` `+` `4` `;` `$` and replace all non keywords and operator language to a default for `T`

The automaton iterate to state in that of token `:=` and compares procedence to `$`, as it is higher , we shift to the next operator token , in this case `+`. As can be seen , its higher so we shift again to operator token `;`. Reach this state, automaton determines it is time for reduction , so it `reduces` the string back to the operator that makes it do another `shift` . So it reduces to operator token `+` because it has a lower procedence , so the string remainds in the form:

|  `$` `let` `T` `:=` `T` `+` `E`   | $E -> T ;$

And again we go back to operator token `:=`:

|  `$` `let` `T` `:=` `E` | $E -> T + E$   

| `$` `let` `E` | $E -> T := E$   

| `$` `E` | $E -> let  E$   

At this time we `shift` because we have reached `$` 

| `$` `E` `$`

| `S` | $S -> \$E\$$

# HULK

In `HULK` programming languaje we used operator procedence in a form

### Procedence according to operator
  
- $[,(,\{$
- $],)$
- $c$
- $\}$
- $as$
- $\% , **$ , ^
- $*,/$
- $+,-$
- $<,>,>=,<=,==, ~ ,is$
- $\&,\|,!$
- $.$
- $=,+=,-=,/=,*=,--,:=,++,--$
- $let$
- $if$
- $elif$
- $else$
- $@,@@$
- $,$
- $=>$
- $in$
- $||$
- $;$
- $\$2$
- $\$1,\$3$