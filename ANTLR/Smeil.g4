grammar Smeil;

prog               :  module EOF ;

module             :  'hej' orden* ;

orden : WORD ;


WORD                : [A-Za-z]+ ;

WHITESPACE          : [ \t\r\n]+ -> skip ;