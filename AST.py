# from lark import Lark, Transformer
# from lark.tree import Tree
from ast import main
import lark
import ast_classes
import AST_final
import graphviz
from graphviz import Digraph

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


statements : statement+
    

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
        | SEMICOLON

modify : push_back_exp | push_front_exp

push_back_exp : word POINT PUSH_BACK LPAREN data_format RPAREN

PUSH_BACK : "push_back"

push_front_exp : word POINT PUSH_FRONT LPAREN data_format RPAREN

PUSH_FRONT : "push_front"

display_statement : DISPLAY LPAREN display_args RPAREN

DISPLAY : "display"

display_args : expression COMMA display_args
            | display_args COMMA expression
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
                        | typedef word

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
        print("node")
        if isinstance(tree, dict):
            print("if node")
            for key, value in tree.items():
                child = f"{parent}_{key}"
                dot.node(child, str(key))
                dot.edge(parent, child)
                add_nodes(child, value)
        elif isinstance(tree, list):
            print("ielf node")
            for item in tree:
                add_nodes(parent, item)
        else:
            dot.node(f"{parent}_{tree}", str(tree))
    print("hi")
    dot.node("root", "AST")
    add_nodes("root", ast)

    return dot


def tree_to_graphviz(tree, graph=None):

    if graph is None:
        graph = Digraph()

    if isinstance(tree, ast_classes.ASTNode):
        graph.node(str(id(tree)), label=str(tree))

        try:
            for child in tree.children:
                if isinstance(child, ast_classes.ASTNode):
                    graph.node(str(id(child)), label = str(child))
                    graph.edge(str(id(tree)), str(id(child)))
                    tree_to_graphviz(child, graph)

                else:
                    graph.node(str(id(child)), label=str(child))
                    graph.edge(str(id(tree)), str(id(child)))
               
        except: pass 
        
    return graph      






class Variable:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type

class VariableStorage:
    def __init__(self):
        self.variables = {}

    def add_variable(self, name, data_type):
        if name in self.variables:
            print(f"Variable '{name}' already exists.")
        else:
            self.variables[name] = Variable(name, data_type)
            # print(f"Variable '{name}' added successfully.")

    def is_variable_present(self, name):
        return name in self.variables

    def print_variables(self):
        print("Variables:")
        for name, variable in self.variables.items():
            print(f"{name}: {variable.data_type}")

    def get_data_type(self, name):
        if name in self.variables:
            return self.variables[name].data_type
        else:
            return None


variable_storage = VariableStorage()

def Semantic(tree):
    
    for child in tree.children:
        # print(child)
        # variable_storage.print_variables()
        # if(child == program):
        #     print("Abhay")
        if isinstance(child, ast_classes.variable_declaration):
                variable_storage.add_variable(child.children[1], child.children[0].children[0])
                # print(child.children[0].children[0])
                # print(child.children[1])
                # variable_storage.print_variables()
                # if isinstance(child, ast_classes.variable_declaration):
        elif isinstance(child, ast_classes.variable_assignment):
            if(not variable_storage.is_variable_present(child.children[0])):
                print("Semantic Error : Variable", child.children[0], "not declared")
            
            exp = child.children[0]
            i = len(exp)
            # for children in child.children[2]:
            #     i = i + 1
            if(i == 1):
                # print(child.children[0])
                if(variable_storage.is_variable_present(child.children[2].children[0])):
                    exp1 = child.children[2].children[0]
                else:
                    exp1 = child.children[2].children[0].children[0]
                    # print(exp1)
                # print(exp1)
                t1 = variable_storage.get_data_type(exp)
                t2 = variable_storage.get_data_type(exp1)

                if isinstance(child.children[2].children[0], ast_classes.number):
                    # print(exp1)
                    variable_storage.add_variable(exp1, 'int')
                    # variable_storage.print_variables()
                elif isinstance(child.children[2].children[0], ast_classes.decimal):
                    variable_storage.add_variable(exp1, 'dotie')
                else:
                    if(not variable_storage.is_variable_present(exp1)):
                        print("Semantic Error : Variable", exp1, "not declared")

                # print(t1, t2)

                if(t1 == t2):
                    drd = 0
                else:
                    print("Typecast Error : ")
                    print(exp, ", datatype - ",t1)
                    print(exp1, ", datatype - ",t2)
                continue

            exp1 = child.children[2].children[0].children[0]
            exp2 = child.children[2].children[2].children[0]
            # print(exp1)
            # print(exp2)

            if isinstance(exp1, ast_classes.number):
                variable_storage.add_variable(exp1, 'int')
            elif isinstance(exp1, ast_classes.decimal):
                variable_storage.add_variable(exp1, 'dotie')
            else:
                if(not variable_storage.is_variable_present(exp1)):
                    print("Semantic Error : Variable", exp1, "not declared")


            if isinstance(exp2, ast_classes.number):
                variable_storage.add_variable(exp2, 'int')
            elif isinstance(exp2, ast_classes.decimal):
                variable_storage.add_variable(exp2, 'dotie')
            else:
                if(not variable_storage.is_variable_present(exp2)):
                    print("Semantic Error : Variable", exp2, "not declared")
                    continue


            ## Typecast check
            t1 = variable_storage.get_data_type(exp)
            t2 = variable_storage.get_data_type(exp1)
            t3 = variable_storage.get_data_type(exp2)
            
            if(t1 == t2 and t2 == t3):
                drd = 0
            else:
                print("Typecast Error : ")
                print(exp, ", datatype - ",t1)
                print(exp1, ", datatype - ",t2)
                print(exp2, ", datatype - ",t3)
            

            
        if isinstance(child, ast_classes.ASTNode):
            Semantic(child)
        # else:








# parser = Lark(gram_file, start='program', transformer='terminal')
# src_text = """
#             int start(){
#                 display('inside');
#                 return 0;
#             }
#             """

# src_text = """
#             int start(){
#             for (int i = 1; i = i+1; i <= 10){
#                 display('inside');
#                 if (i == 7){
#                     get_out;
#                 }
#             }
#             return 0;
#             }
#             """


src_text = """
            int start(){
            int x = 10;
            int y = 2;
            bool z;
            dotie p = 3.14;
            p = p + 3.2;
            bool a = true;
            bool b = false;
            return 0;
            }
            """
# nums.push_front(60);
            # nums.push_back(87)
# dotie y;
#             y = 2.54;
#             x = x + 1;
#             y = 2.54;
#             int k = 2929;
#             k = 'abhay';
#             if( a < 10){
#                 x = x + 1;
#             }a
#             otif ( 10 < a < 15){
#                 x = x + 2;
#             }
#             otw {
#                 x = x + 3;
#             }

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
    print(concrete.pretty())
    print(type(concrete))
    print("1")
    transformer = AST_final.OurTransformer()
    print("AST:")
    ast = transformer.transform(concrete)
    print(type(ast))
    print("1")
    # print("AST:")
    # print(ast.pretty())
    print(ast)
    Semantic(ast)
# # Assuming 'ast' is the AST generated from your code
    # dot = visualize_ast(ast)
    dot = tree_to_graphviz(ast)
    dot.render('ast_55', format='png', cleanup=True)
#     # print("done")


if __name__ == "__main__":
    main()




