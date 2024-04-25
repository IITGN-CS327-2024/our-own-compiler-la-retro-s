import ast_classes

def handle_arithmetic_operator(operation, left, right):
    """Generate WAT code for an arithmetic operation."""
    operators = {
        '+': 'i32.add',
        '-': 'i32.sub',
        '*': 'i32.mul',
        '/': 'i32.div_s',
        '%': 'i32.rem_s'
    }
    op = operators[operation]
    return f"    local.get ${left}\n    local.get ${right}\n    {op}"

def generate_wat_function(name, operation):
    """Generate WAT code for a function definition."""
    body = handle_arithmetic_operator(operation, 'a', 'b')
    return f"""
  (func ${name} (export "{name}") (param $a i32) (param $b i32) (result i32)
{body}
  )"""

def main():
    operations = {
        'add': '+',
        'sub': '-',
        'mul': '*',
        'div': '/',
        'mod': '%'
    }
    module_content = "(module"

    for name, op in operations.items():
        module_content += generate_wat_function(name, op)

    module_content += "\n)"

    with open("arithmetic_test1.wat", "w") as file:
        file.write(module_content)

if __name__ == "__main__":
    main()
