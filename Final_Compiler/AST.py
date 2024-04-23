# from lark import Lark, Transformer
# from lark.tree import Tree
from ast import main
import lark
import ast_classes
import AST_final
import graphviz
from graphviz import Digraph

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return ''.join(lines)


gram_file = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/gram_file.txt")
src_text = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/src_text.txt")


########################################################## AST VISUALIZATION #####################################
   
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

################################################ SEMANTIC ANALYSER ###########################################

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
        if isinstance(child, ast_classes.variable_declaration):
                variable_storage.add_variable(child.children[1], child.children[0].children[0])
                exp4 = child.children[1]
                if isinstance(child, ast_classes.variable_declaration):
                    number_of_children = len(child.children)

                if(number_of_children > 2):
                    if(variable_storage.get_data_type(exp4) == 'bool'):
                        continue

                    exp5 = child.children[3].children[0]
                    if isinstance(exp5, ast_classes.number):
                        variable_storage.add_variable(exp5, 'int')
                    elif isinstance(exp5, ast_classes.decimal):
                        variable_storage.add_variable(exp5, 'dotie')
                    else:
                        if(not variable_storage.is_variable_present(exp5)):
                            print("Semantic Error in declaration : Variable", exp5, "not declared")
                    
                    t4 = variable_storage.get_data_type(exp4)
                    t5 = variable_storage.get_data_type(exp5)
                    
                    if(t4 == t5):
                        drd = 0
                    else:
                        print("Typecast Error : ")
                        print(exp4, ", datatype - ",t4)
                        print(exp5, ", datatype - ",t5)

        elif isinstance(child, ast_classes.variable_assignment):
            if(not variable_storage.is_variable_present(child.children[0])):
                print("Semantic Error : Variable", child.children[0], "not declared")
            
            exp = child.children[0]
            tmp = child.children[2]
            if isinstance(child, ast_classes.variable_assignment):
                    number_of_children = len(child.children)
            i = number_of_children
            if(i == 1):
                if(variable_storage.is_variable_present(child.children[2].children[0])):
                    exp1 = child.children[2].children[0]
                else:
                    exp1 = child.children[2].children[0].children[0]
                t1 = variable_storage.get_data_type(exp)
                t2 = variable_storage.get_data_type(exp1)

                if isinstance(child.children[2].children[0], ast_classes.number):
                    variable_storage.add_variable(exp1, 'int')
                elif isinstance(child.children[2].children[0], ast_classes.decimal):
                    variable_storage.add_variable(exp1, 'dotie')
                else:
                    if(not variable_storage.is_variable_present(exp1)):
                        print("Semantic Error : Variable", exp1, "not declared")


                if(t1 == t2):
                    drd = 0
                else:
                    print("Typecast Error : ")
                    print(exp, ", datatype - ",t1)
                    print(exp1, ", datatype - ",t2)
                continue

            exp1 = child.children[2].children[0].children[0]
            exp2 = child.children[2].children[2].children[0]

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




def main():

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

    print("Semantic")
    Semantic(ast)


    dot = tree_to_graphviz(ast)
    dot.render('ast_501', format='png', cleanup=True)


if __name__ == "__main__":
    main()




