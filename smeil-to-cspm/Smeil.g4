grammar Smeil;



process : 'proc' ident vardecl* ;

vardecl : 'var' ident ': int ;' ;


expression : name
           | name '(' expression* ')'
           | '(' expression ')'
           ;

name : ident
     | name '.' name
     ;

ident : (ALPHANUM | ALPHA | NUM | '_' | '-') '()'? ;

ALPHA : [A-Za-z]+ ;

NUM : [0-9]+ ;

ALPHANUM : [A-Za-z0-9\-_]+;

WHITESPACE : [ \t\r\n]+ -> skip ;
