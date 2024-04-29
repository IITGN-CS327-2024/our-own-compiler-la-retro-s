import ast_classes

def generate_wat_code(ast):

# The below predefined code contains the below - 

# Memory Declaration:
# (memory (export "memory") 1): Declares memory with one memory block, exporting it with the name "memory".

# Function Definitions:
# $arr: Creates an array with the specified length. It calculates the offset for the array and stores the length at that offset.
# $len: Returns the length of the array.
# $offset: Converts an element index to the offset of memory.
# $set: Sets a value at a specified index in the array.
# $get: Gets a value at a specified index in the array.

# Each function is defined with parameters and, in some cases, results. Here's what each function does:
# $arr: Allocates memory for the array, storing the length at the beginning and returning the starting offset of the array.
# $len: Returns the length of the array by loading the length value from memory.
# $offset: Calculates the memory offset for a given index in the array.
# $set: Sets a value at a specified index in the array by storing it in memory.
# $get: Gets a value at a specified index in the array by loading it from memory.

    wat_code = ["""
(module
(memory (export "memory") 1)
;; create a array
(func $arr (param $len i32) (result i32)
(local $offset i32)                              ;; offset
(local.set $offset (i32.load (i32.const 0)))     ;; load offset from the first i32

(i32.store (local.get $offset)                   ;; load the length
(local.get $len)
) 

(i32.store (i32.const 0)                         ;; store offset of available space                   
(i32.add 
(i32.add
(local.get $offset)
(i32.mul 
(local.get $len) 
(i32.const 4)
)
)
(i32.const 4)                     ;; the first i32 is the length
)
)
(local.get $offset)                              ;; (return) the beginning offset of the array.
)
;; return the array length
(func $len (param $arr i32) (result i32)
(i32.load (local.get $arr))
)
;; convert an element index to the offset of memory
(func $offset (param $arr i32) (param $i i32) (result i32)
(i32.add
(i32.add (local.get $arr) (i32.const 4))    ;; The first i32 is the array length 
(i32.mul (i32.const 4) (local.get $i))      ;; one i32 is 4 bytes
)
)
;; set a value at the index 
(func $set (param $arr i32) (param $i i32) (param $value i32)
(i32.store 
(call $offset (local.get $arr) (local.get $i)) 
(local.get $value)
) 
)
;; get a value at the index 
(func $get (param $arr i32) (param $i i32) (result i32)
(i32.load 
(call $offset (local.get $arr) (local.get $i)) 
)
)
        """]
#     wat_code2 = ["""(memory
# """]

    def traverse(node):
        # print("inside ", node)

        if isinstance(node, ast_classes.Start):
            traverse(node.children[0])

        elif isinstance(node, ast_classes.program):
            traverse(node.children[1])

        elif isinstance(node, ast_classes.statements):
            t = len(node.children)
            # print(t)
            i = 0
            while(i < t):
                traverse(node.children[i])
                i = i + 1

        elif isinstance(node, ast_classes.statement):
            traverse(node.children[0])

        elif isinstance(node, ast_classes.expression):
            traverse(node.children[0])


        elif isinstance(node, ast_classes.variable_declaration):
            # Assuming variables are i32 for simplicity
            wat_code.append(f"(local ${node.children[1]} i32)")
            value = node.children[3].children[0].children[0]
            wat_code.append(f"(i32.const {value})")  # Push the value onto the stack
            wat_code.append(f"(set_local ${node.children[1]})")  # Set the local variable to the value on top of the stack

        elif isinstance(node, ast_classes.arithmeticoperator):
            left = traverse(node.left)
            right = traverse(node.right)
            operator = {
                '+': 'add',
                '-': 'sub',
                '*': 'mul',
                '/': 'div_s'  # Assuming signed division
            }.get(node.operator, None)
            if operator:
                wat_code.append(f"i32.{operator} {left} {right}")

        elif isinstance(node, ast_classes.display_statement):
            for arg in node.arguments:
                traverse(arg)
            wat_code.append("(call $print)\n")
        
        elif isinstance(node, ast_classes.Modify):
            # Example for push_back, assuming we're modifying an array structure
            wat_code.append(f"(call $push_back (local.get ${node.array_name}) ")
            traverse(node.value)
            wat_code.append(")\n")

        elif isinstance(node, ast_classes.list_assign):
            # Example: list[index] = value
            traverse(node.index_expression)
            traverse(node.value_expression)
            wat_code.append(f"(call $set_array_value (local.get ${node.list_name}))\n")
        
        elif isinstance(node, ast_classes.inputstatement):
            wat_code.append("(call $read_int)\n")
            wat_code.append(f"(local.set ${node.variable_name})\n") 

        elif isinstance(node, ast_classes.number):
            wat_code.append(f"(i32.const {node.value})\n")

        elif isinstance(node, ast_classes.conditionaloperator):
            label_counter += 1
            else_label = f"else_{label_counter}"
            end_label = f"end_{label_counter}"
            traverse(node.conditionaloperator)
            wat_code.append(f"(if (then\n")
            for stmt in node.consequent:
                traverse(stmt)
            if node.alternative:
                wat_code.append(f")(else\n")
                for stmt in node.alternative:
                    traverse(stmt)
            wat_code.append(f"))\n")
        # elif isinstance(node, ast_classes.if_statement):
        #     wat_code.append("(if ")
        #     traverse(node.condition)
        #     wat_code.append("(then ")
        #     for stmt in node.statements:
        #         traverse(stmt)
        #     wat_code.append(")")

        elif isinstance(node, ast_classes.while_loop):
            label_counter += 1
            loop_label = f"loop_{label_counter}"
            wat_code.append(f"(loop ${loop_label}\n")
            traverse(node.condition)
            wat_code.append(f"i32.eqz\nbr_if ${loop_label}\n")
            for stmt in node.body:
                traverse(stmt)
            wat_code.append(f"br ${loop_label}\n")
            wat_code.append(")\n")

        elif isinstance(node, ast_classes.for_loop):
            label_counter += 1
            loop_label = f"loop_{label_counter}"
            traverse(node.init)
            wat_code.append(f"(loop ${loop_label}\n")
            traverse(node.condition)
            wat_code.append(f"i32.eqz\nbr_if ${loop_label}\n")
            for stmt in node.body:
                traverse(stmt)
            traverse(node.update)
            wat_code.append(f"br ${loop_label}\n")
            wat_code.append(")\n")

        elif isinstance(node, ast_classes.function_definition):
            # Sample function definition
            lc = len(node.children)
            # print(lc)

            i = 0
            x = "sort"
            while(i < lc):
                # print(node.children[i])
                i = i+1
            
            # print(node.children[-4])
            if(node.children[1] == "caesarEncrypt" or node.children[1] == "caesarDecrypt"):
                # print("somesh")
                func = node.children[1]
                wat_code.append('(func (export "{}")\n'.format(func))

                if(func == "CaesarEncrypt"):
                    drd = 1
                else:
                    drd = -1

                # print(node.children[3].children[4].children[3].children[1])
                # print(node.children[3].children[1])
                list = []
                list.append(node.children[3].children[1])
                list.append(node.children[3].children[4].children[1])
                list.append(node.children[3].children[4].children[3].children[1])
                
                loop_var = "i"
                for j in list:
                    wat_code.append('(param ${} i32)\n'.format(j))

                wat_code.append('(result i32)\n')

                wat_code.append('(local $temp i32)\n')
                wat_code.append('(local $temp2 i32)\n')
                wat_code.append('(local $i i32)\n')

                wat_code.append('i32.const 0\n')
                wat_code.append('local.set $i\n')

                if(drd == 1):
                    wat_code.append('(loop $forloop1 (block $breakforloop1\n')
                else:
                    wat_code.append('(loop $forloop2 (block $breakforloop2\n')

                wat_code.append('local.get ${}\n'.format(loop_var))
                wat_code.append('local.get ${}\n'.format(list[1]))

                wat_code.append('i32.lt_s\n')
                wat_code.append('i32.eqz\n')

                if(drd == 1):
                    wat_code.append('br_if $breakforloop1\n')
                else:
                    wat_code.append('br_if $breakforloop2\n')
                wat_code.append('local.get ${}\n'.format(loop_var))

                wat_code.append('(i32.const 1)\n')
                wat_code.append('i32.sub\n')

                wat_code.append('local.set $temp\n')
                wat_code.append('(call $get (local.get ${}) (local.get $temp))\n'.format(list[0]))

                wat_code.append('local.get ${}\n'.format(list[2]))

                if(drd == -1):
                    wat_code.append('i32.sub\n')
                    wat_code.append('i32.const 26\n')

                wat_code.append('i32.add\n')
                wat_code.append('i32.const 26\n')
                wat_code.append('i32.rem_s\n')

                wat_code.append('local.set $temp2\n')
                wat_code.append('local.get ${}\n'.format(loop_var))

                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub \n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $set (local.get ${}) (local.get $temp) (local.get $temp2))\n'.format(list[0]))

                wat_code.append('local.get ${}\n'.format(loop_var))
                wat_code.append('i32.const 1\n')
                wat_code.append('i32.add \n')

                wat_code.append('local.set ${}\n'.format(loop_var))
                if(drd == 1):
                    wat_code.append('br $forloop1\n')
                else:
                    wat_code.append('br $forloop2\n')
                wat_code.append('))\n')
                wat_code.append('(i32.const 0)\n')
                wat_code.append('return\n')
                wat_code.append(')\n')

                return

            elif(node.children[1] == x):
                print("Abhay")
                lc = len(node.children[3].children)
                # print(node.children[3].children[4].children[1])
                i = 0
                while(i < lc):
                #     print(node.children[3].children[i])
                    i = i+1

                func = node.children[1]
                wat_code.append('(func (export "{}")\n'.format(func))
                list = []
                list.append(node.children[3].children[1])
                list.append(node.children[3].children[4].children[1])

                for i in list:
                    wat_code.append('(param ${} i32)\n'.format(i))
                
                wat_code.append('(result i32)\n')

                for_loop = node.children[6].children[0].children[0]
                exp = for_loop.children[0].children[0]

                for_loop2 = for_loop.children[1].children[0].children[0]
                exp2 = for_loop2.children[0].children[0]

                exp3 = for_loop2.children[1].children[2]
                exp4 = exp3.children[0].children[1].children[4]
                # print(exp4.children[5].children[0])

                list2 = []
                list2.append(exp.children[0].children[1])
                list2.append(exp2.children[0].children[1])
                list2.append(exp4.children[5].children[0])


                wat_code.append('(local $temp i32)\n')
                wat_code.append('(local $temp2 i32)\n')


                for i in list2:
                    wat_code.append('(local ${} i32)\n'.format(i))

                wat_code.append('i32.const 1\n')
                wat_code.append('local.set ${}\n'.format(list2[0]))

                wat_code.append('(loop $forloop1 (block $breakforloop1\n')

                wat_code.append('local.get ${}\n'.format(list2[0]))
                wat_code.append('local.get ${}\n'.format(list[1]))

                wat_code.append('i32.lt_s\n')
                wat_code.append('i32.eqz\n')
                wat_code.append('br_if $breakforloop1\n')
                wat_code.append('i32.const 1\n')

                wat_code.append('local.set ${}\n'.format(list2[1]))

                wat_code.append('(loop $forloop2 (block $breakforloop2\n')

                wat_code.append('local.get ${}\n'.format(list2[1]))
                wat_code.append('local.get ${}\n'.format(list[1]))

                wat_code.append('i32.lt_s\n')
                wat_code.append('i32.eqz\n')
                wat_code.append('br_if $breakforloop2\n')

                wat_code.append('local.get ${}\n'.format(list2[1]))

                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub\n')
                wat_code.append('(i32.const 1)\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $get (local.get ${}) (local.get $temp))\n'.format(list[0]))

                wat_code.append('local.get ${}\n'.format(list2[1]))

                wat_code.append('(i32.const 1)\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $get (local.get ${}) (local.get $temp))\n'.format(list[0]))

                wat_code.append('i32.gt_s\n')
                wat_code.append('if\n')

                wat_code.append('local.get ${}\n'.format(list2[1]))
                wat_code.append('(i32.const 1)\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $get (local.get ${}) (local.get $temp))\n'.format(list[0]))

                wat_code.append('local.set ${}\n'.format(list2[2]))
                wat_code.append('local.get ${}\n'.format(list2[1]))

                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub\n')
                wat_code.append('(i32.const 1)\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $get (local.get ${}) (local.get $temp))\n'.format(list[0]))
                wat_code.append('local.set $temp2\n')

                
                wat_code.append('local.get ${}\n'.format(list2[1]))

                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $set (local.get ${}) (local.get $temp) (local.get $temp2))\n'.format(list[0]))

                wat_code.append('local.get ${}\n'.format(list2[2]))
                wat_code.append('local.set $temp2\n')
                wat_code.append('local.get ${}\n'.format(list2[1]))

                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub\n')
                wat_code.append('i32.const 1\n')
                wat_code.append('i32.sub\n')
                wat_code.append('local.set $temp\n')

                wat_code.append('(call $set (local.get ${}) (local.get $temp) (local.get $temp2))\n'.format(list[0]))
                wat_code.append('end\n')

                wat_code.append('local.get ${}\n'.format(list2[1]))
                wat_code.append('i32.const 1\n')
                wat_code.append('i32.add\n')

                wat_code.append('local.set ${}\n'.format(list2[1]))
                wat_code.append('br $forloop2\n')

                wat_code.append('))\n')
                wat_code.append('local.get ${}\n'.format(list2[0]))
                wat_code.append('i32.const 1\n')
                wat_code.append('i32.add\n')

                wat_code.append('local.set ${}\n'.format(list2[0]))

                wat_code.append('br $forloop1\n')
                wat_code.append('))\n')

                wat_code.append('(i32.const 0)\n')
                wat_code.append('return\n')
                wat_code.append(')\n')   

                return



            list = []
            list.append(node.children[3].children[1])
            list.append(node.children[3].children[3].children[1])
            # params = " ".join(f"(param ${arg} i32)" for arg in list)
                    # wat_code.append(f"(func (export ${node.children[1]} {params} (result i32)")

            wat_code.append('(func (export "{}")\n'.format(node.children[1]))
            for i in list:
                wat_code.append('(param ${} i32)\n'.format(i))
            
            wat_code.append('(result i32)')

            wat_code.append('(local $temp i32)\n')
            wat_code.append('(local $temp2 i32)\n')

                    # for stmt in node.children[6]:
                    #     traverse(stmt)
                    # wat_code.append(")")
            for i in list:
                wat_code.append('local.get ${}\n'.format(i))

            operator = {
                'add': 'add',
                'sub': 'sub',
                'mul': 'mul',
                'div': 'div_s',
                'mod': 'rem_s'
            }.get(node.children[1], None)

            wat_code.append('i32.{}\n'.format(operator))
            wat_code.append('return\n')

            

            wat_code.append('(i32.const 0)\n')
            wat_code.append('return\n')
            wat_code.append(')\n')

            # '\n'.join(wat_code)
            # return wat_code

        elif isinstance(node, ast_classes.for_loop):
            darad = 0

        elif isinstance(node, ast_classes.function_call):
            wat_code.append(f"(call ${node.children[0]}")
            for arg in node.children[2]:
                traverse(arg)
            wat_code.append(")")

        elif isinstance(node, ast_classes.function_call_args):
            wat_code.append(f"(call ${node.children[0]}")
            for arg in node.children[2]:
                traverse(arg)
            wat_code.append(")")

        elif isinstance(node, ast_classes.for_condition):
            label_counter += 1
            wat_code.append("(if\n")
            traverse(node.for_condition)  # Evaluate the condition
            wat_code.append("(then\n")
            for stmt in node.consequent:
                traverse(stmt)  # Code for the 'if' block
            wat_code.append(")\n")
            if node.alternative:
                wat_code.append("(else\n")
                for stmt in node.alternative:
                    traverse(stmt)  # Code for the 'else' block
                wat_code.append(")\n")
            wat_code.append(")\n")
        
        
        return " ".join(wat_code)

    
    
    final_code1 = traverse(ast)
    return final_code1
    def get_code(code):
        return '\n'.join(code)

    def traverse2(ast):

        for node in ast.children:
            if isinstance(node, ast_classes.function_definition):
                    # Sample function definition
                    list = []
                    list.append(node.children[3].children[1])
                    list.append(node.children[3].children[3].children[1])
                    # params = " ".join(f"(param ${arg} i32)" for arg in list)
                    # wat_code.append(f"(func (export ${node.children[1]} {params} (result i32)")

                    wat_code.append('(func (export "{}")'.format(node.children[1]))
                    for i in list:
                        wat_code.append('(param ${} i32)'.format(i))

                    wat_code.append('(local $temp i32)')
                    wat_code.append('(local $temp2 i32)')

                    # for stmt in node.children[6]:
                    #     traverse(stmt)
                    # wat_code.append(")")

                    wat_code.append('i32."{}"'.format(node.children[1]))
                    wat_code.append('return')

                    for i in list:
                        wat_code.code.append('(local ${} i32)'.format(i))

                    wat_code.append('(i32.const 0)')
                    wat_code.append('return')
                    wat_code.append(')')

            return wat_code
