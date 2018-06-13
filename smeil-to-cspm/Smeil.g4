grammar Smeil;

module : entity entity* ;

entity : process process*
       | network
       ;

network : 'network' IDENT '(' params? ')' '{' networkdecl '}';

networkdecl : instance*
            /* | busdecl */
            ;

/* NOTE! This is not how the original grammar is */
instance : 'instance' instancename 'of' IDENT '(' (name '.' name)? ')' ';' ;

/* NOTE! Not completed */
instancename : IDENT ;

process : 'proc' IDENT '(' params? ')' declaration* '{' statement* '}';

/*process : ('sync'|'async')? 'proc' IDENT '(' params? ')' declaration* '{' statement* '}';*/

declaration : vardecl
            | busdecl
            /*| constdecl
            /*| enum*/
            /*| function*/
            /*| instance */
            /*| generate*/
            ;

params : param (',' param)* ;

param : direction IDENT ;
/* param : ('[' expression* ']')* direction ident ; */

direction : 'in'
          | 'out'
          | 'const'
          ;

statement : name '=' expression ';'
          /*| 'if' '(' condition ')' '{' statement* '}' elifblock* elseblock?*/
          /*| 'for' ident '=' expression 'to' expression '{' statement* '}'*/
          /*| 'while' condition '{' statement* '}'*/
          /*| 'switch' expression '{' switchcase switchcase* ('default' '{' statement statement* '}')? '}'*/
          | 'trace' '(' formatstring (','expression)* ')' ';'
          /*| 'assert' '(' condition '{' ',' formatstring '}' ')' ';'*/
          /*| 'barrier' ';'*/
          /*| 'break' ';'*/
          /*| 'return' expression? ';'*/
          ;

formatstring : '"' (formatstringpart*) '"' ;

/* TODO not completed */
formatstringpart : '{}'
                 | IDENT
                 ;


busdecl : 'exposed'? 'bus' IDENT '{' bussignaldecls '}' ';' ;

bussignaldecls : bussignaldecl bussignaldecl* ;

bussignaldecl : IDENT ':' TYPENAME ('=' expression )? ranges ';' ;

vardecl : 'var' IDENT ':' TYPENAME ('=' expression )? ranges? ';' ;

TYPENAME : ('i' NUM)
         /* | 'int' - Should not be possible for simulated programs? */
         | ('u' NUM)
         /* | 'uint' - Should not be possible for simulated programs?*/
         /* TODO not finished */
         ;

/* typename : 'u2'
         | 'u4'
         | 'u6'
         | 'u7'
         | 'u17';// not finished */

ranges : 'range' expression 'to' expression ;


expression : name
           /*| litteral*/
           | expression binop expression
           /*| unop expression*/
           /* | name '(' expression* ')' */
           /*| '(' expression ')'*/
           ;

binop : '/'
      | '%'
      | '+'
      | '-'
      ;

name : IDENT
     | NUM
     | name '.' name
     ;

IDENT : (ALPHA (ALPHA | NUM)*) ;


fragment
Nondigit
    :   [a-zA-Z_\-]
    ;

fragment
Digit
    :   [0-9]
    ;


ALPHA :
    Nondigit+
    ;

NUM : Digit+
    ;

/* ALPHA : [A-Za-z]+ ; */

/* NUM : [0-9]+ ; */

/* ALPHANUM : [A-Za-z0-9\-_]+; */

WHITESPACE : [ \t\r\n]+ -> skip ;


