grammar SimpleLang;

block: ( stat? NEWLINE )* ;

stat: ifconditional                      #ifcondition
    | REPEAT repetitions block ENDREPEAT #repeat
	| PRINT (ID	| STRING)	             #print
	| ID '=' expr	                     #assign
	| READ ID 		                     #read
;

expr  : literal                        # literalexpr
      | ID                             # variableExpr
      | 'sqrt' parentheses             # sqrtexpr
      | parentheses                    # parexpr
      | expr '^' expr                  # powerexpr
      | expr parentheses               # implicitexpr
      | expr op=('*'|'/') expr         # muldivexpr
      | expr op=('+'|'-') expr         # addsubexpr
      | STRING                         # stringExpr;


ifconditional: IF condition_block THEN blockif ENDIF;

condition_block: gt | lt | eq | gte | lte;
gt: ID GT (INT | FLOAT);
lt: ID LT (INT | FLOAT);
eq: ID EQ (INT | FLOAT);
gte: ID GTE (INT | FLOAT);
lte: ID LTE (INT | FLOAT);
blockif: block;

parentheses: '(' expr ')';

repetitions: value;

value: ID
     | INT;

literal: ('-'|'+')? (INT|FLOAT);
INT: [0-9]+;
FLOAT : [0-9]+ '.' [0-9]*;
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
REPEAT: 'repeat';
ENDREPEAT: 'endrepeat';
IF:     'if';
THEN: 'then';
ENDIF: 'endif';
PRINT:	'print' ;
READ:	'read' ;
ID:   ('a'..'z'|'A'..'Z')+;
STRING :  '"' ( ~('\\'|'"') )* '"';
NEWLINE:	'\r'? '\n';
EQ: '==';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
WS:   (' '|'\t')+ -> skip;
