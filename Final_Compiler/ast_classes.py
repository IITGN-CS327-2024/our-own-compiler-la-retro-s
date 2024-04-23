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

        self.children = []
        for i, value in enumerate(values):
            self.children.append(value)

class Start(start): 
   def __init__(self, values):
      super().__init__(values)

class program(start):
   def __init__(self, values):
      super().__init__(values)


class typedef(start):
   def __init__(self, values):
      super().__init__(values)


class statements(start):
   def __init__(self, values):
      super().__init__(values)


class statement(start):
   def __init__(self, values):
      super().__init__(values)


# class DataFormat(start):
#    def __init__(self, values):
#       super().__init__(values)

# class statement(ASTNode):
#     pass

# class statement(ASTNode):
#     def __init__(self, statements):
#         self.statements = statements

class display_statement(start):
   def __init__(self, values):
      super().__init__(values)

class inputstatement(start):
   def __init__(self, values):
      super().__init__(values)

# class if_statement(statement):
#     def __init__(self, expression, statements):
#         self.expression = expression
#         self.statements = statements

class if_statement(start):
   def __init__(self, values):
      super().__init__(values)

class otif_statement(start):
   def __init__(self, values):
      super().__init__(values)

class otw_statement(start):
   def __init__(self, values):
      super().__init__(values)

class while_loop(start):
   def __init__(self, values):
      super().__init__(values)

class for_loop(start):
   def __init__(self, values):
      super().__init__(values)

class for_arg(start):
   def __init__(self, values):
      super().__init__(values)

class for_condition(start):
   def __init__(self, values):
      super().__init__(values)

class function_definition(start):
   def __init__(self, values):
      super().__init__(values)

class function_args(start):
   def __init__(self, values):
      super().__init__(values)

class ExceptionHandling(start):
   def __init__(self, values):
      super().__init__(values)

class expression(start):
   def __init__(self, values):
      super().__init__(values)

class Modify(start):
   def __init__(self, values):
      super().__init__(values)

class PushBack(start):
   def __init__(self, values):
      super().__init__(values)

class PushFront(start):
   def __init__(self, values):
      super().__init__(values)

class DisplayArgs(start):
   def __init__(self, values):
      super().__init__(values)

class FunctionArgs(start):
   def __init__(self, values):
      super().__init__(values)

class for_args(start):
   def __init__(self, values):
      super().__init__(values)

class TupleArg(start):
   def __init__(self, values):
      super().__init__(values)

class ListArg(start):
   def __init__(self, values):
      super().__init__(values)

class ListSlice(start):
   def __init__(self, values):
      super().__init__(values)

# class CompoundVariableDeclaration(start):
#    def __init__(self, values):
#       super().__init__(values)

class WordDec(start):
   def __init__(self, values):
      super().__init__(values)

class TupleDec(start):
   def __init__(self, values):
      super().__init__(values)

class ListDec(start):
   def __init__(self, values):
      super().__init__(values)

class ListPerf(start):
   def __init__(self, values):
      super().__init__(values)

# class Perform(start):
#    def __init__(self, values):
#       super().__init__(values)

class conditionaloperator(start):
   def __init__(self, values):
      super().__init__(values)

class arithmeticoperator(start):
   def __init__(self, values):
      super().__init__(values)

class logicaloperator(start):
   def __init__(self, values):
      super().__init__(values)

class variable_declaration(start):
   def __init__(self, values):
      super().__init__(values)

class variable_assignment(start):
   def __init__(self, values):
      super().__init__(values)

class function_call(start):
   def __init__(self, values):
      super().__init__(values)

class function_call_args(start):
   def __init__(self, values):
      super().__init__(values)

# class ntype(start):
#    def __init__(self, values):
#       super().__init__(values)

# class number1(start):
#    def __init__(self, values):
#       super().__init__(values)

# class decimal1(start):
#    def __init__(self, values):
#       super().__init__(values)

class number(start):
   def __init__(self, values):
      super().__init__(values)

class decimal(start):
   def __init__(self, values):
      super().__init__(values)

class bool2(start):
   def __init__(self, values):
      super().__init__(values)

# Constants for operators
LESS_THAN = "<"
GREATER_THAN = ">"
LESS_THAN_OR_EQUAL = "<="
GREATER_THAN_OR_EQUAL = ">="
EQUAL = "=="
QUOTATION = "'"
