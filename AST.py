from lark import Lark, Transformer
from lark.tree import Tree

gram_file = """

program : typedef WS START LPAREN RPAREN LCURLY statements RETURN ZERO RCURLY

RETURN : "return"

ZERO : "0;"

START : "start"

LPAREN : "("
RPAREN : ")"
LCURLY : "{"
RCURLY : "}"
LSQUARE : "["
RSQUARE : "]"


statements : statement (SEMICOLON statements)?
        | statement statements
        |


SEMICOLON : ";"

QUOTATION : "'"

statement : display_statement
        | input_statement
        | if_statement
        | otif_statement
        | otw_statement
        | for_loop
        | while_loop
        | GET_OUT
        | GO_ON
        | function_definition
        | exception_handling
        | expression
        | modify

modify : push_back | push_front

push_back : word POINT PUSH_BACK LPAREN data_format RPAREN

PUSH_BACK : "push_back"

push_front : word POINT PUSH_FRONT LPAREN data_format RPAREN

PUSH_FRONT : "push_front"

display_statement : DISPLAY LPAREN display_args RPAREN

DISPLAY : "display"

display_args : expression COMMA display_args
            | expression
            | QUOTATION expression QUOTATION


input_statement : INPUT LPAREN expression RPAREN

INPUT : "input"

if_statement : IF LPAREN expression RPAREN LCURLY statements RCURLY

IF : "if"

otif_statement : OTIF LPAREN expression RPAREN LCURLY statements RCURLY

OTIF : "otif"

otw_statement : OTW LCURLY statements RCURLY

OTW : "otw"

for_loop : FOR LPAREN for_args RPAREN LCURLY statements RCURLY

FOR : "for"

for_args : expression SEMICOLON expression SEMICOLON expression

while_loop : WHILE LPAREN expression RPAREN LCURLY statements RCURLY

WHILE : "while"

GET_OUT : "get_out"

GO_ON : "go_on"

function_definition : typedef word LPAREN function_args RPAREN LCURLY statements RETURN word SEMICOLON RCURLY
                    | typedef word LPAREN RPAREN LCURLY statements RETURN word SEMICOLON RCURLY

function_args : typedef word COMMA function_args
            | typedef word

COMMA : ","

exception_handling : TRY LCURLY statements RCURLY "catch" LPAREN word RPAREN LCURLY statements RCURLY "finally" LCURLY statements RCURLY

TRY : "try"

expression : number
        | decimal
        | word
        | string
        | bool
        | variable_declaration
        | variable_assignment
        | expression arithmeticoperator expression
        | expression logicaloperator expression
        | LPAREN expression RPAREN
        | function_call
        | for_condition
        | compound_variable_declaration
        | list_slice
        | list_perf

list_perf : word POINT perform

perform : FRONT | BACK | EMPTY

FRONT : "front"

BACK : "back"

EMPTY : "empty"


list_slice : word LSQUARE number COMMA number RSQUARE

compound_variable_declaration : word_dec | list_dec | tuple_dec

word_dec : WORD word EQUALS QUOTATION word QUOTATION

WORD : "word"

tuple_dec : TUPLE word EQUALS LPAREN tuple_arg RPAREN

TUPLE : "tuple"

tuple_arg : tuple_data (COMMA tuple_data)*

tuple_data : string | number | bool | decimal

list_dec : dtype word LSQUARE RSQUARE EQUALS LSQUARE list_arg RSQUARE

dtype : WORD | typedef

list_arg : data_format (COMMA data_format)*

data_format : number | string | bool

for_condition : expression conditionaloperator expression

# typedef : "int" | "bool" | "dotie" | "bigint" | "char"

typedef : INT | BOOL | DOTIE | BIGINT | CHAR

INT : "int"

BOOL : "bool"

DOTIE : "dotie"

BIGINT : "bigint"

CHAR : "char"

# conditionaloperator : "<" | ">" | "<=" | ">=" | "==" | "!="

conditionaloperator : LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL | EQUAL | NOT_EQUAL

LESS_THAN : "<"

GREATER_THAN : ">"

LESS_THAN_OR_EQUAL : "<="

GREATER_THAN_OR_EQUAL : ">="

EQUAL : "=="

NOT_EQUAL : "!="

# arithmeticoperator : "+" | "-" | "/" | "*" | "**" | "%"

arithmeticoperator : ADDITION | SUBTRACTION | DIVISION | MULTIPLICATION | EXPONENTIATION | MODULUS

ADDITION : "+"

SUBTRACTION : "-"

DIVISION : "/"

MULTIPLICATION : "*"

EXPONENTIATION : "**"

MODULUS : "%"

# logicaloperator : "&&" | "||"

logicaloperator  : AND | OR

AND : "&&"

OR : "||"


variable_declaration : typedef word EQUALS expression

variable_assignment : word EQUALS expression

function_call : word LPAREN function_call_args RPAREN

function_call_args : expression COMMA function_call_args
                    | expression

string : QUOTATION string_cont QUOTATION

string_cont : word (WS word)* (WS number)*

word : identifier

EQUALS : "="

decimal : number POINT number

POINT : "."

identifier : /[a-zA-Z_][a-zA-Z0-9_]*/

number : /[0-9]+/

bool : "True" | "False"

%import common.WS
%ignore WS
"""



class TerminalTransformer(Transformer):
    def __default__(self, data, children, meta):
        return data

    def program(self, children):
        # We expect only one child, which is the "program" node
        return children[0]

    def statements(self, children):
        # Flatten the statements
        return [child for statement in children for child in statement]

    def statement(self, children):
        return children[0]

    def expression(self, children):
        return children[0]

    def typedef(self, children):
        print("Children in typedef:", children)
        if len(children) > 1:
            return children[1]  # Extract the terminal within quotes
        else:
            return children[0]  # No need to extract if it's a single terminal

    def QUOTATION(self, children):
        print("Children in QUOTATION:", children)
        return children[0]  # Extract the content within quotes
            



# parser = Lark(gram_file, start='program', transformer='terminal')
src_text = """
            int start(){
            for (int i = 1; i = i+1; i <= 10){
                display('inside for');
                if (i == 7){
                    get_out;
                }
            }
            return 0;
            }
            """
parser = Lark(gram_file, start='program')
tree = parser.parse(src_text)
print(tree.pretty())
terminal_tree = TerminalTransformer().transform(tree)

def extract_terminals(tree):
    if isinstance(tree, Tree):
        return [extract_terminals(child) for child in tree.children]
    else:
        return tree


extracted_terminals = extract_terminals(tree)

def print_tree(tree, depth=0):
    if isinstance(tree, list):
        for child in tree:
            print_tree(child, depth + 1)
    else:
        print("  " * depth + str(tree))

print_tree(extracted_terminals)

