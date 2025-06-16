# main.py
from myparser import parse_code
from analyzer import CodeAnalyzer

if __name__ == "__main__":
    with open("test_code.py", "r") as f:
        code = f.read()

    tree = parse_code(code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    result = analyzer.report()

    print("Algorithm Analysis Report:")
    for key, value in result.items():
        print(f"{key}: {value}")
