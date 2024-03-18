# from lark import Lark, Transformer
from lark.tree import Tree
import graphviz

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

# def visualize_ast(ast):
    # dot = graphviz.Digraph()

    # def add_nodes(parent, tree):
    #     if isinstance(tree, dict):
    #         for key, value in tree.items():
    #             child = f"{parent}_{key}"
    #             dot.node(child, str(key))
    #             dot.edge(parent, child)
    #             add_nodes(child, value)
    #     elif isinstance(tree, list):
    #         for item in tree:
    #             add_nodes(parent, item)
    #     else:
    #         dot.node(f"{parent}_{tree}", str(tree))

    # dot.node("root", "AST")
    # add_nodes("root", ast)

    # return dot
            



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

class ASTTransformer(Transformer):
    def program(self, items):
        return {'program': items}

    def statements(self, items):
        return {'statements': items}

    def statement(self, items):
        return {'statement': items}

    def display_statement(self, items):
        return {'display_statement': items}

    def input_statement(self, items):
        return {'input_statement': items}

    def if_statement(self, items):
        return {'if_statement': items}

    def otif_statement(self, items):
        return {'otif_statement': items}

    def otw_statement(self, items):
        return {'otw_statement': items}

    def for_loop(self, items):
        return {'for_loop': items}

    def while_loop(self, items):
        return {'while_loop': items}

    def GET_OUT(self, items):
        return {'GET_OUT': items}

    def GO_ON(self, items):
        return {'GO_ON': items}

    def function_definition(self, items):
        return {'function_definition': items}

    def exception_handling(self, items):
        return {'exception_handling': items}

    def expression(self, items):
        return {'expression': items}

    def modify(self, items):
        return {'modify': items}

    def push_back(self, items):
        return {'push_back': items}

    def push_front(self, items):
        return {'push_front': items}

    def display_args(self, items):
        return {'display_args': items}

    def function_args(self, items):
        return {'function_args': items}

    def tuple_arg(self, items):
        return {'tuple_arg': items}

    def list_arg(self, items):
        return {'list_arg': items}

    def list_slice(self, items):
        return {'list_slice': items}

    def compound_variable_declaration(self, items):
        return {'compound_variable_declaration': items}

    def word_dec(self, items):
        return {'word_dec': items}

    def tuple_dec(self, items):
        return {'tuple_dec': items}

    def list_dec(self, items):
        return {'list_dec': items}

    def for_args(self, items):
        return {'for_args': items}

    def for_condition(self, items):
        return {'for_condition': items}

    def conditionaloperator(self, items):
        return {'conditionaloperator': items}

    def arithmeticoperator(self, items):
        return {'arithmeticoperator': items}

    def logicaloperator(self, items):
        return {'logicaloperator': items}

    def function_call(self, items):
        return {'function_call': items}

    def function_call_args(self, items):
        return {'function_call_args': items}

    def string(self, items):
        return {'string': items}

    def string_cont(self, items):
        return {'string_cont': items}

    def word(self, items):
        return {'word': items}

    def identifier(self, items):
        return {'identifier': items}

    def number(self, items):
        return {'number': items}

    def bool(self, items):
        return {'bool': items}

    def decimal(self, items):
        return {'decimal': items}

    def typedef(self, items):
        return {'typedef': items}

    def QUOTATION(self, items):
        return {'QUOTATION': items}

    def POINT(self, items):
        return {'POINT': items}

    def LPAREN(self, items):
        return {'LPAREN': items}

    def RPAREN(self, items):
        return {'RPAREN': items}

    def LCURLY(self, items):
        return {'LCURLY': items}

    def RCURLY(self, items):
        return {'RCURLY': items}

    def LSQUARE(self, items):
        return {'LSQUARE': items}

    def RSQUARE(self, items):
        return {'RSQUARE': items}

    def SEMICOLON(self, items):
        return {'SEMICOLON': items}

    def COMMA(self, items):
        return {'COMMA': items}

    def ADDITION(self, items):
        return {'ADDITION': items}

    def SUBTRACTION(self, items):
        return {'SUBTRACTION': items}

    def DIVISION(self, items):
        return {'DIVISION': items}

    def MULTIPLICATION(self, items):
        return {'MULTIPLICATION': items}

    def EXPONENTIATION(self, items):
        return {'EXPONENTIATION': items}

    def MODULUS(self, items):
        return {'MODULUS': items}

    def AND(self, items):
        return {'AND': items}

    def OR(self, items):
        return {'OR': items}

    def EQUALS(self, items):
        return {'EQUALS': items}

    def LESS_THAN(self, items):
        return {'LESS_THAN': items}

    def GREATER_THAN(self, items):
        return {'GREATER_THAN': items}

    def LESS_THAN_OR_EQUAL(self, items):
        return {'LESS_THAN_OR_EQUAL': items}

    def GREATER_THAN_OR_EQUAL(self, items):
        return {'GREATER_THAN_OR_EQUAL': items}

    def EQUAL(self, items):
        return {'EQUAL': items}

    def NOT_EQUAL(self, items):
        return {'NOT_EQUAL': items}


parser = Lark(gram_file, start='program')
tree = parser.parse(src_text)

print(tree)

transformer = ASTTransformer()
ast = transformer.transform(tree)
print("\n AST: \n")
print(ast)


# # Assuming 'ast' is the AST generated from your code
# dot = visualize_ast(ast)
# dot.render('ast_5', format='png', cleanup=True)








