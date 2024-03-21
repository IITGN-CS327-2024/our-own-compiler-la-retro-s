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
    def program(self, children):
        children = remove_none(children)
        return ast_classes.program(children)

    def typedef(children):
        children = remove_none(children)
        return ast_classes.typedef(children)

    def statements(self, children):
        children = remove_none(children)
        return ast_classes.statements(children)

    def statement(self, children):
        children = remove_none(children)
        return ast_classes.statement(children)

    def modify(self, children):
        children = remove_none(children)
        return ast_classes.modify(children)

    def push_back(self, children):
        children = remove_none(children)
        return ast_classes.push_back(children)

    def push_front(self, children):
        children = remove_none(children)
        return ast_classes.push_front(children)

    def display_statement(self, children):
        children = remove_none(children)
        return ast_classes.display_statement(children)

    def input_statement(self, children):
        children = remove_none(children)
        return ast_classes.input_statement(children)

    def if_statement(self, children):
        children = remove_none(children)
        return ast_classes.if_statement(children)

    # def if_statement(self, children):
    #     expression, statements = children
    #     return ast_classes.if_statement(expression, statements)

    def otif_statement(self, children):
        children = remove_none(children)
        return ast_classes.otif_statement(children)

    def otw_statement(self, children):
        children = remove_none(children)
        return ast_classes.otw_statement(children)

    def for_loop(self, children):
        children = remove_none(children)
        return ast_classes.for_loop(children)

    def while_loop(self, children):
        children = remove_none(children)
        return ast_classes.while_loop(children)

    def function_definition(self, children):
        children = remove_none(children)
        return ast_classes.function_definition(children)

    def exception_handling(self, children):
        children = remove_none(children)
        return ast_classes.exception_handling(children)

    def expression(self, children):
        children = remove_none(children)
        return ast_classes.expression(children)

    def list_slice(self, children):
        children = remove_none(children)
        return ast_classes.list_slice(children)

    def list_perf(self, children):
        children = remove_none(children)
        return ast_classes.list_perf(children)

    def perform(self, children):
        children = remove_none(children)
        return ast_classes.perform(children)

    def compound_variable_declaration(self, children):
        children = remove_none(children)
        return ast_classes.compound_variable_declaration(children)

    def word_dec(self, children):
        children = remove_none(children)
        return ast_classes.word_dec(children)

    def tuple_dec(self, children):
        children = remove_none(children)
        return ast_classes.tuple_dec(children)

    def tuple_arg(self, children):
        children = remove_none(children)
        return ast_classes.tuple_arg(children)

    def list_dec(self, children):
        children = remove_none(children)
        return ast_classes.list_dec(children)

    def list_arg(self, children):
        children = remove_none(children)
        return ast_classes.list_arg(children)

    def data_format(self, children):
        children = remove_none(children)
        return ast_classes.data_format(children)

    def for_args(self, children):
        children = remove_none(children)
        return ast_classes.for_args(children)

    def function_args(self, children):
        children = remove_none(children)
        return ast_classes.function_args(children)

    def expression(self, children):
        children = remove_none(children)
        return ast_classes.expression(children)

    def typedef(self, children):
        children = remove_none(children)
        return ast_classes.typedef(children)

    def conditionaloperator(self, children):
        children = remove_none(children)
        return ast_classes.conditionaloperator(children)

    def arithmeticoperator(self, children):
        children = remove_none(children)
        return ast_classes.arithmeticoperator(children)

    # def QUOTATION(self, children):
    #     children = remove_none(children)
    #     return ast_classes.QUOTATION(children)
    def QUOTATION(self, children):
        return "'"

    def program(self, children):
        children = remove_none(children)
        return ast_classes.program(children)
