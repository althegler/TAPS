grammar Smeil;


entity : process+
       /*| network*/
       ;

process : 'proc' ident '(' params? ')' declaration* '{' statement* '}';

/*process : ('sync'|'async')? 'proc' ident '(' params? ')' declaration* '{' statement* '}';*/

declaration : vardecl
            | busdecl
            /*| constdecl
            /*| enum*/
            /*| function*/
            /*| instance */
            /*| generate*/
            ;

params : param (',' param)* ;

param : direction ident ;
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
          /*| 'trace' '(' formatstring '{' ','expression '}' ')' ';'*/
          /*| 'assert' '(' condition '{' ',' formatstring '}' ')' ';'*/
          /*| 'barrier' ';'*/
          /*| 'break' ';'*/
          /*| 'return' expression? ';'*/
          ;

busdecl : 'exposed'? 'bus' ident '{' bussignaldecls '}' ';' ;

bussignaldecls : bussignaldecl bussignaldecl* ;

bussignaldecl : ident ':' typename ('=' expression )? ranges ';' ;

vardecl : 'var' ident ':' typename ('=' expression )? ranges? ';' ;

typename : 'int' ;// not finished

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
      ;

name : ident
     | name '.' name
     ;

ident : (ALPHANUM | ALPHA | NUM | '_' | '-') ;

ALPHA : [A-Za-z]+ ;

NUM : [0-9]+ ;

ALPHANUM : [A-Za-z0-9\-_]+;

WHITESPACE : [ \t\r\n]+ -> skip ;
