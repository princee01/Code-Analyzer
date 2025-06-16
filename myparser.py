import ast

def parse_code(code: str):
    tree = ast.parse(code)
    return tree