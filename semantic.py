import lark


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

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, tree):
        self.visit(tree)

    def visit(self, node):
        method_name = 'visit_' + node.data
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.children:
            self.visit(child)

    def visit_program(self, node):
        self.visit(node.children[5])  # Visit statements node
        self.visit(node.children[6])  # Visit return node

    def visit_statements(self, node):
        for statement in node.children:
            self.visit(statement)

    def visit_variable_declaration(self, node):
        typedef = node.children[0].value
        identifier = node.children[1].value
        if identifier in self.symbol_table:
            raise Exception(f"Variable '{identifier}' redeclaration error.")
        self.symbol_table[identifier] = {'type': typedef}
        self.visit(node.children[-1])  # Visit expression node

    def visit_display_statement(self, node):
        self.visit(node.children[2])  # Visit display_args node

    def visit_input_statement(self, node):
        self.visit(node.children[2])  # Visit expression node

    def visit_if_statement(self, node):
        self.visit(node.children[2])  # Visit expression node
        self.visit(node.children[5])  # Visit statements node

    def visit_otif_statement(self, node):
        self.visit(node.children[2])  # Visit expression node
        self.visit(node.children[5])  # Visit statements node

    def visit_otw_statement(self, node):
        self.visit(node.children[2])  # Visit statements node

    def visit_for_loop(self, node):
        self.visit(node.children[2])  # Visit for_args node
        self.visit(node.children[6])  # Visit statements node

    def visit_while_loop(self, node):
        self.visit(node.children[2])  # Visit expression node
        self.visit(node.children[5])  # Visit statements node

    def visit_function_definition(self, node):
        self.visit(node.children[-2])  # Visit statements node

    def visit_exception_handling(self, node):
        self.visit(node.children[2])  # Visit statements node
        self.visit(node.children[7])  # Visit statements node
        self.visit(node.children[12])  # Visit statements node

    def visit_expression(self, node):
        if len(node.children) == 1:
            if isinstance(node.children[0], lark.Token):
                # This is a terminal node
                pass
            else:
                self.visit(node.children[0])  # Visit the child node if it's not a terminal
        elif len(node.children) == 3:
            # Visit left and right expression nodes
            self.visit(node.children[0])
            self.visit(node.children[2])

    def visit_list_slice(self, node):
        # Visit word, number, and number nodes
        self.visit(node.children[0])
        self.visit(node.children[2])
        self.visit(node.children[4])

    def visit_compound_variable_declaration(self, node):
        # Visit word_dec, list_dec, or tuple_dec node
        self.visit(node.children[0])

    def visit_modify(self, node):
        self.visit(node.children[0])  # Visit push_back or push_front node

    def visit_push_back(self, node):
        self.visit(node.children[4])  # Visit data_format node

    def visit_push_front(self, node):
        self.visit(node.children[4])  # Visit data_format node

    def visit_display_args(self, node):
        for child in node.children:
            self.visit(child)  # Visit each expression node

    def visit_function_args(self, node):
        for child in node.children:
            self.visit(child)  # Visit each typedef and word node

    def visit_tuple_arg(self, node):
        for child in node.children:
            self.visit(child)  # Visit each tuple_data node

    def visit_list_arg(self, node):
        for child in node.children:
            self.visit(child)  # Visit each data_format node

    def visit_for_condition(self, node):
        self.visit(node.children[0])  # Visit expression node
        self.visit(node.children[2])  # Visit expression node

    def visit_word_dec(self, node):
        self.visit(node.children[4])  # Visit word node

    def visit_tuple_dec(self, node):
        self.visit(node.children[1])  # Visit word node
        self.visit(node.children[4])  # Visit tuple_arg node

    def visit_list_dec(self, node):
        self.visit(node.children[1])  # Visit word node
        self.visit(node.children[6])  # Visit list_arg node

    def visit_string(self, node):
        self.visit(node.children[1])  # Visit string_cont node

    def visit_string_cont(self, node):
        for child in node.children:
            self.visit(child)  # Visit each expression node

    def visit_function_call(self, node):
        self.visit(node.children[-1])  # Visit function_call_args node

    def visit_function_call_args(self, node):
        for child in node.children:
            self.visit(child)  # Visit each expression node
            
    def visit_list_perf(self, node):
        self.visit(node.children[0])  # Visit word node
        self.visit(node.children[1])  # Visit perform node

    def visit_tuple_data(self, node):
        for child in node.children:
            self.visit(child)  # Visit each tuple_data node

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

# Example usage:
parser = lark.Lark(gram_file, start='program')
tree = parser.parse(src_text)
analyzer = SemanticAnalyzer()
analyzer.analyze(tree)
