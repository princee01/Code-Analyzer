# analyzer.py
import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loop_count = 0
        self.recursive_calls = 0
        self.function_defs = []
        self.list_creations = 0
        self.dict_creations = 0
        self.variable_count = 0

    
    def visit_For(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loop_count += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.function_defs.append(node.name)
        self.current_function = node.name
        self.variable_count += len(node.args.args) 
        self.generic_visit(node)

    def visit_Call(self, node):
        if hasattr(self, 'current_function') and isinstance(node.func, ast.Name):
            if node.func.id == self.current_function:
                self.recursive_calls += 1
        self.generic_visit(node)

    def visit_List(self, node):
        self.list_creations += 1
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.dict_creations += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.variable_count += len(node.targets)
        self.generic_visit(node)    

    def report(self):
        # Time Complexity
        # if self.loop_count == 0 and self.recursive_calls == 0:
        #     time_complexity = "O(1)"
        # elif self.recursive_calls:
        #     time_complexity = "Recursive"
        # elif self.loop_count == 1:
        #     time_complexity = "O(n)"
        # elif self.loop_count == 2:
        #     time_complexity = "O(n^2)"
        # else:
        #     time_complexity = "High Complexity"
        if self.recursive_calls and self.loop_count:
              time_complexity = f"O(n) + Recursive"
        elif self.recursive_calls:
              time_complexity = "Recursive"
        elif self.loop_count == 1:
              time_complexity = "O(n)"
        elif self.loop_count == 2:
              time_complexity = "O(n^2)"
        elif self.loop_count > 2:
              time_complexity = "High Complexity"
        else:
              time_complexity = "O(1)"

        

        # Space Complexity
        extra_space = self.list_creations + self.dict_creations
        if self.recursive_calls:
            space_complexity = "O(n) (recursion stack)"
        elif extra_space == 0 and self.variable_count <= 2:
            space_complexity = "O(1)"
        elif extra_space == 1:
            space_complexity = "O(n)"
        elif extra_space >= 2:
            space_complexity = "O(n^2)"
        else:
            space_complexity = "Unknown"

        return {
            "Loops": self.loop_count,
            "Recursive Calls": self.recursive_calls,
            "Estimated Time Complexity": time_complexity,
            "Estimated Space Complexity": space_complexity
        }