import ast_classes
import lark

def remove_none(lst):  # It flattens the lst
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

    # def num(self, children):
    #     return len(children)

    def start(self, children):
        children = remove_none(children)
        return ast_classes.Start(children)

    def program(self, children):
        # children = remove_none(children)
        # return ast_classes.program(children)
        # children = remove_none(children)
        # return ast_classes.program(children)
        
        children = remove_none(children)
        values = children
        indices_to_remove = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        values = values[:-1]
        return ast_classes.program(values)

    def typedef(self, children):
        children = remove_none(children)
        return ast_classes.typedef(children)

    def RETURN(self, children):
        children = remove_none(children)
        return children

    def statements(self, children):
        # print(children)
        children = remove_none(children)
        return ast_classes.statements(children)

    def statement(self, children):
        # children = remove_none(children)
        # return ast_classes.statement(children)
        children = remove_none(children)
        return ast_classes.statement(children)
        

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
        # children = remove_none(children)
        # return ast_classes.display_statement(children)

        children = remove_none(children)
        values = children
        indices_to_remove = [0, 1, 2, 3, 4, 5, 6, 7, 9]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.display_statement(values)

    def display_args(self, children):
        # children = remove_none(children)
        # return ast_classes.DisplayArgs(children)
        children = remove_none(children)
        values = children
        indices_to_remove = [0, 2]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.DisplayArgs(values)
    
    def DISPLAY(self, children):
        children = remove_none(children)
        return children

    def input_statement(self, children):
        children = remove_none(children)
        return ast_classes.inputstatement(children)

    def if_statement(self, children):
        # children = remove_none(children)
        # return ast_classes.if_statement(children)
        children = remove_none(children)
        values = children
        indices_to_remove = [0, 1, 3, 4, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.if_statement(values)
        # expression = children[0]
        # statements = children[1]
        # return ast_classes.if_statement(expression, statements)

    def otif_statement(self, children):
        children = remove_none(children)
        values = children
        indices_to_remove = [1, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.otif_statement(values)
        # children = remove_none(children)
        # return ast_classes.otif_statement(children)
        # expression = children[0]
        # statements = children[1]
        # return ast_classes.otif_statement(expression, statements)

    def otw_statement(self, children):
        children = remove_none(children)
        values = children
        indices_to_remove = [0, 1, 3, 4, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.otw_statement(values)
        # children = remove_none(children)
        # return ast_classes.otw_statement(children)

    def for_loop(self, children):
        children = remove_none(children)
        values = children
        indices_to_remove = [0, 1, 3, 4, 6]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.for_loop(values)
        # children = remove_none(children)
        # return ast_classes.for_loop(children)

        # print(children)
        # print(children[2])
        # print(children[5])
        # expression = children[2]
        # statements = children[5]
        # return ast_classes.for_loop(expression, statements)

    def for_args(self, children):
        children = remove_none(children)
        values = children
        indices_to_remove = [1, 3]
        values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        return ast_classes.for_arg(values)
        # expression = children[2]
        # statements = children[5]
        # children = remove_none(children)
        # return ast_classes.for_arg(children)

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
        return children
        # return ast_classes.Perform(children)

    def compound_variable_declaration(self, children):
        children = remove_none(children)
        return children
        # return ast_classes.CompoundVariableDeclaration(children)

    def variable_declaration(self, children):
        children = remove_none(children)
        # if(children[0] == "typedef")
        #     childen[0] = typedef(slef, children)
        return ast_classes.variable_declaration(children)

    def variable_assignment(self, children):
        children = remove_none(children)
        return ast_classes.variable_assignment(children)

    def function_call(self, children):
        children = remove_none(children)
        return ast_classes.function_call(children)

    def function_call_args(self, children):
        children = remove_none(children)
        return ast_classes.function_call_args(children)

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
        return children
        # return ast_classes.DataFormat(children)

    def for_condition(self, children):
        children = remove_none(children)
        return ast_classes.for_condition(children)

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

    # def ntype(self, children):
    #     children = remove_none(children)
    #     return ast_classes.ntype(children)

    def number(self, children):
        children = remove_none(children)
        return ast_classes.number(children)

    def decimal(self, children):
        children = remove_none(children)
        return ast_classes.decimal(children)

    def bool2(self, children):
        children = remove_none(children)
        return ast_classes.bool2(children)

    def argument(self, children):
        children = remove_none(children)
        return ast_classes.argument(children)

    def string(self, children):
        children = remove_none(children)
        return children

    def string_cont(self, children):
        children = remove_none(children)
        return children

    def word(self, children):
        children = remove_none(children)
        return children

    def dtype(self, children):
        children = remove_none(children)
        return children

    def push_back_exp(self, children):
        children = remove_none(children)
        return children
    
    def push_front_exp(self, children):
        children = remove_none(children)
        return children

    def list_access(self, children):
        children = remove_none(children)
        return children
    
    def list_assign(self, children):
        children = remove_none(children)
        return children

    def LPAREN(self, children):
        return children

    def RPAREN(self, children):
        return children
    
    def LCURLY(self, children):
        return children

    def RCURLY(self, children):
        return children
    
    def LSQUARE(self, children):
        return children

    def RSQUARE(self, children):
        return children

    def identifier(self, children):
        return children

    def SEMICOLON(self, children):
        return children

    def ZERO(self, children):
        return children

    def EQUALS(self, children):
        return children

    def POINT(self, children):
        return children

    def OR(self, children):
        return children

    def AND(self, children):
        return children

    def MODULUS(self, children):
        return children

    def EXPONENTIATION(self, children):
        return children

    def MULTIPLICATION (self, children):
        return children

    def DIVISION(self, children):
        return children

    def SUBTRACTION(self, children):
        return children

    def ADDITION(self, children):
        return children

    def NOT_EQUAL(self, children):
        return children

    def EQUAL(self, children):
        return children

    def GREATER_THAN_OR_EQUAL(self, children):
        return children

    def LESS_THAN_OR_EQUAL(self, children):
        return children

    def GREATER_THAN_OR_EQUAL(self, children):
        return children

    def GREATER_THAN(self, children):
        return children

    def LESS_THAN(self, children):
        return children

    def CHAR(self, children):
        return children

    def BIGINT(self, children):
        return children

    def DOTIE(self, children):
        return children

    def BOOL(self, children):
        return children

    def INT(self, children):
        return children

    def TUPLE(self, children):
        return children

    def EMPTY(self, children):
        return children

    def BACK(self, children):
        return children

    def FRONT(self, children):
        return children

    def TRY(self, children):
        return children

    def COMMA(self, children):
        return children

    def GO_ON(self, children):
        return children

    def GET_OUT(self, children):
        return children

    def WHILE(self, children):
        return children

    def FOR(self, children):
        return children

    def OTW(self, children):
        return children

    def OTIF(self, children):
        return children

    def IF(self, children):
        return children

    def PUSH_FRONT(self, children):
        return children

    def PUSH_BACK(self, children):
        return children

    
    # def decimal(self, children):
    #     return children

    # def number(self, children):
    #     return children

    # def decimal1(self, children):
    #     return children

    # def number1(self, children):
    #     return children

    # def bool(self, children):
    #     return children
     
    def QUOTATION(self, children):
        return children
