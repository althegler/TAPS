grammar Example;

name : IDENT
     ;


IDENT : LETTER (LETTER | NUMBER | '_' | '-')* ;


/* fragment
Nondigit
    :   [a-zA-Z_\-]
    ; */

INTEGER : NUMBER+ ;

/* fragment
Number
    :   [0-9]
    ; */


LETTER : [a-z]
       | [A-Z]
       ;

NUMBER : [0-9]
    ;

WHITESPACE : [ \t\r\n]+ -> skip ;

