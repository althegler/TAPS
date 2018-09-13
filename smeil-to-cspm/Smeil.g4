grammar Smeil;

/* NOTE! Not completed */
module : entity entity* ;

entity : network
       | process
       ;

network : 'network' IDENT '(' params? ')' '{' networkdecl '}';

/* NOTE! Not completed */
process : 'proc' IDENT '(' params? ')' declaration* '{' statement* '}';

/* process : ('sync'|'async')? 'proc' IDENT '(' params? ')' declaration* '{' statement* '}'; */

networkdecl : instance* /* NOTE! Not how it is in the original grammer. I need to talk to Truls about this */
            /* | busdecl */
            /* | constdecl */
            /* | gendecl */
            ;

declaration : vardecl
            /* | constdecl */
            | busdecl
            /*| enum*/
            /*| instance */
            /*| gendecl*/
            ;

params : param (',' param)* ;

/* NOTE! Not completed */
param : direction IDENT ;
/* param : ('[' INTEGER? ']')? direction ident ; */

direction : 'in'
          | 'out'
          | 'const'
          ;

vardecl : 'var' IDENT ':' TYPENAME ('=' expression )? ranges? ';' ;

ranges : 'range' expression 'to' expression ;

/* enum : 'enum' IDENT '{' enumfield (',' enumfield)* '}' ';' ; */

/* enumfield : IDENT ('=' INTEGER)? ; */

/* constdecl : 'const' IDENT ':' TYPENAME '=' expression ';' */

busdecl : 'exposed'? 'bus' IDENT '{' bussignaldecls '}' ';' ;

bussignaldecls : bussignaldecl bussignaldecl* ;

bussignaldecl : IDENT ':' TYPENAME ('=' expression )? ranges? ';' ;

/* NOTE! This is not how the original grammar is */
instance : 'instance' instancename 'of' IDENT '(' (name '.' name)? ')' ';' ;

instancename : IDENT
             /* | IDENT '[' expression ']' */
             /* | '_' */
             ;
/* gendecl : 'generate' IDENT '=' expression 'to' expression '{' networkdecl* '}' ; */

statement : name '=' expression ';'
          /*| 'if' '(' expression ')' '{' statement* '}' elifblock* elseblock?*/
          /*| 'for' IDENT '=' expression 'to' expression '{' statement* '}'*/
          /*| 'switch' expression '{' switchcase switchcase* ('default' '{' statement statement* '}')? '}'*/
          | 'trace' '(' formatstring (','expression)* ')' ';'
          /*| 'assert' '(' expression (',' LETTER)? ')' ';'*/
          /*| 'break' ';'*/
          ;

/* switchcase : 'case' expression '{' statement* '}' ; */

/* elifblock : 'elif' '(' expression ')' '{' statement* '}' ; */

/* elseblock : 'else' '{' statement* '}' ; */

formatstring : '"' (formatstringpart*) '"' ;

/* NOTE! This is not how the original grammar is - should be changed*/
formatstringpart : '{}'
                 | LETTER
                 ;

expression : name
           | literal
           | expression binop expression
           /*| unop expression*/
           /*| '(' expression ')'*/
           ;

binop : '+'
      | '-'
      | '*'
      | '/'
      | '%'
      | '=='
      | '!='
      | '<<'
      | '>>'
      | '<'
      | '>'
      | '>='
      | '<='
      | '&'
      | '|'
      | '^'
      | '&&'
      | '||'
      ;

unop : '-'
      | '+'
      | '!'
      | '~'
      ;

/* NOTE! Not completed */
literal : INTEGER
        /* | floating */
        /* | '[' INTEGER (',' INTEGER)* ']' */
        /* | 'true' */
        /* | 'false' */
        /* | specialliteral */
        ;

TYPENAME : ('i' INTEGER)
         /* | 'int' - Should not be possible for simulated programs? */
         | ('u' INTEGER)
         /* | 'uint' - Should not be possible for simulated programs?*/
         /* | 'f32' */
         /* | 'f64' */
         /* | 'bool' */
         /* | '[' expression? ']' TYPENAME */
         ;


IDENT : LETTER (LETTER | NUMBER | '_' | '-')* ;

name : IDENT
     | name '.' name
     /* | name '[' arrayindex ']' */
     ;

/* arrayindex : '*' */
           /* | expression */
           /* ; */


INTEGER : NUMBER+ ;

LETTER : [a-z]
       | [A-Z]
       ;

NUMBER : [0-9]
    ;


WHITESPACE : [ \t\r\n]+ -> skip ;


