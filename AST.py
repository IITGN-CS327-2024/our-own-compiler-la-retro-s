# from lark import Lark, Transformer
# from lark.tree import Tree
from ast import main
import lark
import AST_final
import graphviz

gram_file = """

start : program

program : typedef START LPAREN RPAREN LCURLY statements RETURN ZERO RCURLY

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
        | (statement)?


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

typedef : INT | BOOL | DOTIE | BIGINT | CHAR

INT : "int"

BOOL : "bool"

DOTIE : "dotie"

BIGINT : "bigint"

CHAR : "char"

conditionaloperator : LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL | EQUAL | NOT_EQUAL

LESS_THAN : "<"

GREATER_THAN : ">"

LESS_THAN_OR_EQUAL : "<="

GREATER_THAN_OR_EQUAL : ">="

EQUAL : "=="

NOT_EQUAL : "!="

arithmeticoperator : ADDITION | SUBTRACTION | DIVISION | MULTIPLICATION | EXPONENTIATION | MODULUS

ADDITION : "+"

SUBTRACTION : "-"

DIVISION : "/"

MULTIPLICATION : "*"

EXPONENTIATION : "**"

MODULUS : "%"

logicaloperator  : AND | OR

AND : "&&"

OR : "||"


variable_declaration : typedef word EQUALS expression

variable_assignment : word EQUALS expression

function_call : word LPAREN function_call_args RPAREN

function_call_args : expression COMMA function_call_args
                    | expression

string : QUOTATION string_cont QUOTATION

string_cont : expression (WS expression)*

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

def visualize_ast(ast):
    dot = graphviz.Digraph()

    def add_nodes(parent, tree):
        if isinstance(tree, dict):
            for key, value in tree.items():
                child = f"{parent}_{key}"
                dot.node(child, str(key))
                dot.edge(parent, child)
                add_nodes(child, value)
        elif isinstance(tree, list):
            for item in tree:
                add_nodes(parent, item)
        else:
            dot.node(f"{parent}_{tree}", str(tree))

    dot.node("root", "AST")
    add_nodes("root", ast)

    return dot
            



# parser = Lark(gram_file, start='program', transformer='terminal')
src_text = """
            int start(){
            for (int i = 1; i = i+1; i <= 10){
                display('inside');
                if (i == 7){
                    get_out;
                }
            }
            return 0;
            }
            """






# parser = Lark(gram_file, start='program')
# tree = parser.parse(src_text)

# print(tree)

# print(tree.pretty())

# transformer = ASTTransformer()
# ast = transformer.transform(tree)
# print("\n AST: \n")
# print(ast)


# # # Assuming 'ast' is the AST generated from your code
# dot = visualize_ast(ast)
# dot.render('ast_5', format='png', cleanup=True)


# new code

# parser = lark.Lark(gram_file, parser="lalr")

#     # Step 2: Use the parser (and lexer) to create a parse tree
#     # (concrete syntax)
#     # src_file = open("example_sums.txt", "r")
#     # src_text = "".join(src_file.readlines())
# concrete = parser.parse(src_text)
# print("Parse tree (concrete syntax):")
# print(concrete.pretty())

#     # Step 3: Transform the concrete syntax tree into
#     # an abstract tree, starting from the leaves and working
#     # up.
#     # Warning:  Lousy exceptions because of the way Lark applies these.
# transformer = AST_final.OurTransformer()
# ast = transformer.transform(concrete)
# print(ast.pretty())
# # print(f"as {repr(ast)}")

# # # # Assuming 'ast' is the AST generated from your code
# # dot = visualize_ast(ast)
# # dot.render('ast_6', format='png', cleanup=True)
# # print("done")

# if __name__ == '__main__':
#     main()

def main():
    # Your script logic here
    parser = lark.Lark(gram_file, parser="lalr")
    concrete = parser.parse(src_text)
    print("Parse tree (concrete syntax):")
    # print(concrete.pretty())
    
    transformer = AST_final.OurTransformer()
    print("AST:")
    ast = transformer.transform(concrete)
    # print("AST:")
    # print(ast.pretty())
    print(ast)

# # Assuming 'ast' is the AST generated from your code
    dot = visualize_ast(ast)
    dot.render('ast_51', format='png', cleanup=True)
    print("done")


if __name__ == "__main__":
    main()




