grammar Smeil;



process : 'proc' ident vardecl* ;

vardecl : 'var' ident ': int ;' ;

ident : (ALPHANUM | ALPHA | NUM | '_' | '-') ;

ALPHA : [A-Za-z]+ ;
NUM : [0-9]+ ;

ALPHANUM : [A-Za-z0-9\-_]+;

WHITESPACE : [ \t\r\n]+ -> skip ;
