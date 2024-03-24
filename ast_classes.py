class ASTNodeMeta(type):
    def __new__(cls, name, bases, dct):
        if name != 'ASTNode':
            def repr_func(self):
                return name
            dct['__repr__'] = repr_func
        return super().__new__(cls, name, bases, dct)

class ASTNode(metaclass=ASTNodeMeta):
    """Abstract base class for AST nodes."""
    pass

# class program(ASTNode):
#     def __init__(self, typedef, statements):
#         self.typedef = typedef
#         self.statements = statements


class start(ASTNode):
    def __init__(self, values):
        values = values[:-1]
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

class program(ASTNode):
    def __init__(self, values):
        # indices_to_remove = [1, 2, 3, 4, 6, 7, 8]
        # values = [values[i] for i in range(len(values)) if i not in indices_to_remove]
        # values = values[:-1]
        for i, child in enumerate(values):
            setattr(self, f'value{i}', child)


class typedef(ASTNode):
    def __init__(self, typedef):
        # print("fk")
        self.typedef = typedef
        for i, value in enumerate(typedef):
            setattr(self, f'values{i}', value)


class statements(ASTNode):
    def __init__(self, values):
        # self.statements = values
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)


class statement(ASTNode):
    def __init__(self, values):
        # self.statement = statement
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)


class DataFormat(ASTNode):
    def __init__(self, values):
        # self.value = value
        for i, value in enumerate(values):
            setattr(self, f'values{i}', value)

# class statement(ASTNode):
#     pass

# class statement(ASTNode):
#     def __init__(self, statements):
#         self.statements = statements

class display_statement(statement):
    def __init__(self, display_args):
        self.display_args = display_args

class inputstatement(statement):
    def __init__(self, expression):
        self.expression = expression

# class if_statement(statement):
#     def __init__(self, expression, statements):
#         self.expression = expression
#         self.statements = statements

class if_statement(statement):
    def __init__(self, expression, statements):
        self.expression = expression
        self.statements = statements

class otif_statement(statement):
    def __init__(self, expression, statements):
        self.expression = expression
        self.statements = statements

class otw_statement(statement):
    def __init__(self, statements):
        self.statements = statements

class while_loop(statement):
    def __init__(self, expression, statements):
        self.expression = expression
        self.statements = statements

class for_loop(statement):
    def __init__(self, for_args, statements):
        self.for_args = for_args
        self.statements = statements

class function_definition(statement):
    def __init__(self, typedef, word, function_args, statements):
        self.typedef = typedef
        self.word = word
        self.function_args = function_args
        self.statements = statements

class ExceptionHandling(statement):
    def __init__(self, word, statements, catch_word, catch_statements, finally_statements):
        self.word = word
        self.statements = statements
        self.catch_word = catch_word
        self.catch_statements = catch_statements
        self.finally_statements = finally_statements

class expression(statement):
    def __init__(self, expression):
        self.expression = expression

class Modify(statement):
    def __init__(self, modify):
        self.modify = modify

class PushBack(Modify):
    def __init__(self, word, data_format):
        self.word = word
        self.data_format = data_format

class PushFront(Modify):
    def __init__(self, word, data_format):
        self.word = word
        self.data_format = data_format

class DisplayArgs(ASTNode):
    def __init__(self, expressions):
        self.expressions = expressions

class FunctionArgs(ASTNode):
    def __init__(self, function_args):
        self.function_args = function_args

class for_args(ASTNode):
    def __init__(self, expressions):
        self.expressions = expressions

class TupleArg(ASTNode):
    def __init__(self, tuple_data):
        self.tuple_data = tuple_data

class ListArg(ASTNode):
    def __init__(self, data_formats):
        self.data_formats = data_formats

class ListSlice(statement):
    def __init__(self, word, start_index, end_index):
        self.word = word
        self.start_index = start_index
        self.end_index = end_index

class CompoundVariableDeclaration(statement):
    pass

class WordDec(CompoundVariableDeclaration):
    def __init__(self, word, word_value):
        self.word = word
        self.word_value = word_value

class TupleDec(CompoundVariableDeclaration):
    def __init__(self, word, tuple_arg):
        self.word = word
        self.tuple_arg = tuple_arg

class ListDec(CompoundVariableDeclaration):
    def __init__(self, typedef, word, list_arg):
        self.typedef = typedef
        self.word = word
        self.list_arg = list_arg

class ListPerf(statement):
    def __init__(self, word, perform):
        self.word = word
        self.perform = perform

class Perform(ASTNode):
    def __init__(self, perform_type):
        self.perform_type = perform_type

class conditionaloperator(ASTNode):
    def __init__(self, operator):
        self.operator = operator

class arithmeticoperator(ASTNode):
    def __init__(self, operator):
        self.operator = operator

class logicaloperator(ASTNode):
    def __init__(self, operator):
        self.operator = operator

# Constants for operators
LESS_THAN = "<"
GREATER_THAN = ">"
LESS_THAN_OR_EQUAL = "<="
GREATER_THAN_OR_EQUAL = ">="
EQUAL = "=="
QUOTATION = "'"
