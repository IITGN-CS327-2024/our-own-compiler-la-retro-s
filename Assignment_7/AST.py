# from lark import Lark, Transformer
# from lark.tree import Tree
from ast import main
import lark
import ast_classes
import AST_final
import graphviz
from graphviz import Digraph
from code_generation import generate_wat_code
from Semantic_analyser import Semantic

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return ''.join(lines)

########################################################## GRAMMAR & SOURCE FILE  READ #####################################

gram_file = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/gram_file.txt")
# src_text = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/sort.kul")
# src_text = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/caesar.kul")
src_text = read_file("/Users/abhaykumar/Music/Compilers_project/AST2/arithmetic.kul")



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


################################################ MAIN CODE ###########################################


def main():

    parser = lark.Lark(gram_file, parser="lalr")
    concrete = parser.parse(src_text)
    print("Parse tree (concrete syntax):")
    # print(concrete.pretty())
    print(type(concrete))
    print("1")
    transformer = AST_final.OurTransformer()
    print("AST:")
    ast = transformer.transform(concrete)
    print(type(ast))

    print("Semantic")
    # Semantic(ast)

    wc = generate_wat_code(ast)
    print("WAT")
    print(wc)
    print("WAT_done")

    # print(wc.get_code)

    with open("Caesar", "w") as f:
        f.write(wc)

    # with open("Sort", "w") as f:
    #     f.write(wc)

    print("WAT_write_done")

    dot = tree_to_graphviz(ast)
    dot.render('ast_501', format='png', cleanup=True)


if __name__ == "__main__":
    main()




