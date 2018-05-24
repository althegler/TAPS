grammar Smeil;

prog               :  module+ EOF ;

module             :  WORD ;


WORD                : [A-Za-z]+ ;

WHITESPACE          : [ \t\r\n]+ -> skip ;