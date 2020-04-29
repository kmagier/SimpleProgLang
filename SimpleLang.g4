grammar SimpleLang;

init: ( stat? NEWLINE )* ;

stat: expr           #exprlabel
	| PRINT ID		 #print
	| ID '=' expr	 #assign
	| READ ID 		 #read
;

expr  : literal                        # literalexpr
      | 'sqrt' parentheses             # sqrtexpr
      | parentheses                    # parexpr
      | expr '^' expr                  # powerexpr
      | expr parentheses               # implicitexpr
      | expr op=('*'|'/') expr         # muldivexpr
      | expr op=('+'|'-') expr         # addsubexpr;

parentheses: '(' expr ')';

literal: ('-'|'+')? NUMBER;

NUMBER : [0-9]+('.'[0-9]+)?;
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
PRINT:	'print' ;
READ:	'read' ;

ID:   ('a'..'z'|'A'..'Z')+;

NEWLINE:	'\r'? '\n';
WS:   (' '|'\t')+ -> skip;
