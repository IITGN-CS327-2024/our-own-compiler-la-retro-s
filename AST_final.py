import ast_classes
import lark

def remove_none(lst):
    flat_list = []
    for sublist in lst:
        if isinstance(sublist, list):
            flat_list.extend(remove_none(sublist))
        elif sublist is not None:
            flat_list.append(sublist)
    return flat_list

class OurTransformer(lark.Transformer):
    # def program(self, children):
    #     typedef, statements = children[0], children[5]
    #     # print(children[0], children[5])
    #     return ast_classes.program(typedef, statements)

    def start(self, children):
        children = remove_none(children)
        return ast_classes.start(children)

    def program(self, children):
        # children = remove_none(children)
        # return ast_classes.program(children)
        children = remove_none(children)
        if len(children)==0:
            return None
        else:
            return children
        
        # children = remove_none(children)
        # values = children
        # indices_to_remove = [1, 2, 3, 4, 6, 7, 8]
        # values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        # return ast_classes.program(values)

    def typedef(self, children):
        return ast_classes.typedef(children)

    def statements(self, children):
        # print(children)
        children = remove_none(children)
        return ast_classes.statements(children)

    def statement(self, children):
        # children = remove_none(children)
        # return ast_classes.statement(children)
        children = remove_none(children)
        return children
        

    def modify(self, children):
        children = remove_none(children)
        return ast_classes.Modify(children[0])

    def push_back(self, children):
        children = remove_none(children)
        return ast_classes.PushBack(children)

    def push_front(self, children):
        children = remove_none(children)
        return ast_classes.PushFront(children)

    def display_statement(self, children):
        children = remove_none(children)
        return ast_classes.display_statement(children)

    def input_statement(self, children):
        children = remove_none(children)
        return ast_classes.inputstatement(children)

    def if_statement(self, children):
        expression = children[0]
        statements = children[1]
        return ast_classes.if_statement(expression, statements)

    def otif_statement(self, children):
        expression = children[0]
        statements = children[1]
        return ast_classes.otif_statement(expression, statements)

    def otw_statement(self, children):
        children = remove_none(children)
        return ast_classes.otw_statement(children)

    def for_loop(self, children):
        # print(children)
        # print(children[2])
        # print(children[5])
        expression = children[2]
        statements = children[5]
        return ast_classes.for_loop(expression, statements)

    def while_loop(self, children):
        children = remove_none(children)
        return ast_classes.while_loop(children)

    def function_definition(self, children):
        children = remove_none(children)
        return ast_classes.function_definition(children)

    def exception_handling(self, children):
        children = remove_none(children)
        return ast_classes.ExceptionHandling(children)

    def expression(self, children):
        children = remove_none(children)
        return ast_classes.expression(children)

    def list_slice(self, children):
        children = remove_none(children)
        return ast_classes.ListSlice(children)

    def list_perf(self, children):
        children = remove_none(children)
        return ast_classes.ListPerf(children)

    def perform(self, children):
        children = remove_none(children)
        return ast_classes.Perform(children)

    def compound_variable_declaration(self, children):
        children = remove_none(children)
        return ast_classes.CompoundVariableDeclaration(children)

    def word_dec(self, children):
        children = remove_none(children)
        return ast_classes.WordDec(children)

    def tuple_dec(self, children):
        children = remove_none(children)
        return ast_classes.TupleDec(children)

    def tuple_arg(self, children):
        children = remove_none(children)
        return ast_classes.TupleArg(children)

    def list_dec(self, children):
        children = remove_none(children)
        return ast_classes.ListDec(children)

    def list_arg(self, children):
        children = remove_none(children)
        return ast_classes.ListArg(children)

    def data_format(self, children):
        children = remove_none(children)
        return ast_classes.DataFormat(children)

    def for_args(self, children):
        children = remove_none(children)
        print(children)
        return ast_classes.for_args(children)

    def function_args(self, children):
        children = remove_none(children)
        return ast_classes.FunctionArgs(children)

    def conditionaloperator(self, children):
        children = remove_none(children)
        return ast_classes.conditionaloperator(children)

    def arithmeticoperator(self, children):
        children = remove_none(children)
        return ast_classes.arithmeticoperator(children)

    def logicaloperator(self, children):
        children = remove_none(children)
        return ast_classes.logicaloperator(children)

    def QUOTATION(self, children):
        return "'"
