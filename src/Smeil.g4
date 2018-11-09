grammar Smeil;

/* NOTE! Not completed */
module : entity+ ;

entity : network
       | process
       ;

network : 'network' IDENT '(' params? ')' '{' networkdecl* '}';

/* NOTE! Not completed */
process : 'proc' IDENT '(' params? ')'
            (vardecl
            /* | constdecl */
            | busdecl )*
            /*| enum*/
            /*| instance */
            /*| gendecl - Not implemented in SMEIL yet */
            '{' statement* '}';

/* process : ('sync'|'async')? 'proc' IDENT '(' params? ')' processdecl* '{' statement* '}'; */

networkdecl : instance
            /* | busdecl */
            /* | constdecl */
            /*| gendecl - Not implemented in SMEIL yet */
            ;

/* processdecl : vardecl */
            /* | constdecl */
            /* | busdecl */
            /*| enum*/
            /*| instance */
            /*| gendecl - Not implemented in SMEIL yet */
            /* ; */

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

busdecl : 'exposed'? 'bus' IDENT '{' bussignaldecl+ '}' ';' ;

/* bussignaldecls : bussignaldecl+ ; */

/* NOTE: ranges should not optional in our situation, but they are in the
   original grammar */
bussignaldecl : IDENT ':' TYPENAME ('=' expression )? ranges ';' ;

/* TODO! This is not how the original grammar is.
I should implement it correctly*/
instance : 'instance' instancename 'of' IDENT '(' (name '.' name)? ')' ';' ;


/* TODO We probably want to label the alternatives */
instancename : IDENT
             /* | IDENT '[' expression ']'  - NOTE: Not implemented in SMEIL yet*/
             /* | '_' */
             ;


/* NOTE: This is not implemented in SMEIL yet */
/* gendecl : 'generate' IDENT '=' expression 'to' expression '{' networkdecl* '}' ; */

/* TODO We probably want to label the alternatives */
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

/* NOTE! This is not how the original grammar is - should be changed*/
formatstringpart : '{}'
                 | LETTER
                 ;

/* TODO We probably want to label the alternatives */
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

/* TODO We probably want to label the alternatives */
literal : INTEGER
        /* | floating */
        /* | stringliteral */
        /* | '[' INTEGER (',' INTEGER)* ']' */
        /* | 'true' */
        /* | 'false' */
        /* | 'U */
        ;

stringliteral : '"' STRINGCHAR* '"' ;

/* TODO We probably want to label the alternatives */
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


/* TODO We probably want to label the alternatives */
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


/* NOTE! This is not how the original grammar is - should be changed*/
STRINGCHAR : LETTER+ ;

WHITESPACE : [ \t\r\n]+ -> skip ;


