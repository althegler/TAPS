grammar Smeil;

module : entity+ ;

entity : network
       | process
       ;

network : 'network' IDENT '(' params? ')' '{' networkdecl* '}';

process : 'proc' IDENT '(' params? ')'
            (vardecl
            /* | constdecl */
            | busdecl )*
            /*| enum*/
            /*| instance */
            /*| gendecl - Not implemented in SMEIL yet */
            '{' statement* '}';

/* NOTE: simplified version of 'process'  */
/* process : ('sync'|'async')? 'proc' IDENT '(' params? ')' processdecl* '{' statement* '}'; */

networkdecl : instance
            /* | busdecl */
            /* | constdecl */
            /*| gendecl - Not implemented in SMEIL yet */
            ;

/* NOTE: To simplify this grammar, the processdecl have been added directly
in 'process' */
/* processdecl : vardecl */
            /* | constdecl */
            /* | busdecl */
            /*| enum*/
            /*| instance */
            /*| gendecl - Not implemented in SMEIL yet */
            /* ; */

params : param (',' param)* ;

/* NOTE! Simplified version */
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

busdecl : 'exposed'? 'bus' IDENT '{' bussignaldecl+ '}' ';' ;

/* NOTE: From the original grammar */
/* bussignaldecls : bussignaldecl+ ; */


bussignaldecl : IDENT ':' TYPENAME ('=' expression )? ranges ';' ;

/* NOTE! Different from the original grammar. */
instance : 'instance' instancename 'of' IDENT '(' (name '.' name)? ')' ';' ;


instancename : IDENT
             /* | IDENT '[' expression ']'  - NOTE: Not implemented in SMEIL yet*/
             /* | '_' */
             ;


/* NOTE: Not implemented in SMEIL yet */
/* gendecl : 'generate' IDENT '=' expression 'to' expression '{' networkdecl* '}' ; */

statement : name '=' expression ';'
          /*| 'if' '(' expression ')' '{' statement* '}' elifblock* elseblock?*/
          /*| 'for' IDENT '=' expression 'to' expression '{' statement* '}'*/
          /*| 'switch' expression '{' switchcase switchcase* ('default' '{' statement statement* '}')? '}'*/
          | 'trace' '(' formatstring (','expression)* ')' ';'
          /*| 'assert' '(' expression (',' stringliteral)? ')' ';'*/
          /*| 'break' ';'*/
          ;

/* switchcase : 'case' expression '{' statement* '}' ; */

/* elifblock : 'elif' '(' expression ')' '{' statement* '}' ; */

/* elseblock : 'else' '{' statement* '}' ; */

formatstring : '"' (formatstringpart*) '"' ;

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

literal : INTEGER
        /* | floating */
        /* | stringliteral */
        /* | '[' INTEGER (',' INTEGER)* ']' */
        /* | 'true' */
        /* | 'false' */
        /* | 'U */
        ;

stringliteral : '"' STRINGCHAR* '"' ;

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
     | name '.' name   /* # hierarchical_accessor */
     /* | name '[' arrayindex ']' */
     ;

/* arrayindex : '*' */
           /* | expression */
           /* ; */


INTEGER : NUMBER+
        | '0x' HEXDIGIT+
        | '0o' OCTALDIGIT+
        ;

FLOATING : NUMBER* '.' NUMBER+ ;

NUMBER : [0-9]
    ;

LETTER : [a-z]
       | [A-Z]
       ;

HEXDIGIT : NUMBER
       | [a-f]
       | [A-F]
       ;

OCTALDIGIT : [0-8]
    ;


/* NOTE! This is a bit different from the original grammar is*/
STRINGCHAR : LETTER+ ;

WHITESPACE : [ \t\r\n]+ -> skip ;


