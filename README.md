# 🧠 AlgoAnalyzer – Code Complexity Detector

## 📖 Overview  
This project is a static code analysis tool developed in Python to estimate the **time and space complexity** of Python programs. It uses **Tree-sitter** to parse the abstract syntax tree (AST) of the source code and analyze control structures like loops and recursion to predict algorithmic complexity.

The tool provides an educational foundation for understanding code behavior and lays the groundwork for a more advanced multi-language analysis engine.

---

## 🚀 Features

✅ **Code Parsing with Tree-sitter**: Uses Tree-sitter to generate a precise syntax tree of Python code.  
✅ **Time & Space Complexity Estimation**: Heuristically analyzes code for loops and recursion to estimate computational complexity.  
✅ **Modular Design**: Organized in a clean structure for easy extension and maintenance.  
✅ **Testing Support**: Includes example test files to verify analyzer functionality.

---

## 🧰 Requirements

Make sure Python 3.x is installed, then install required libraries:

```bash
pip install tree_sitter
```

---

## 🧪 Usage Instructions

1. Place the Python file you want to analyze in the project directory.  
2. Open `main.py` and set the test file name in the script:
   ```python
   file_path = "test_code.py"
   ```
3. Run the analyzer:
   ```bash
   python main.py
   ```
4. The output will include:
   - Loops detected  
   - Recursive functions  
   - Estimated time and space complexity

---

## 📂 Project Structure

```
AlgoAnalyzer/
│
├── analyzer.py        # Logic for complexity estimation
├── myparser.py        # Tree-sitter parser integration
├── main.py            # Main runner script
├── test_code.py       # Sample Python code for analysis
└── requirements.txt   # Python dependencies
```

---

## Example(code to be tested)

![Screenshot 2025-06-17 172207](https://github.com/user-attachments/assets/b2c3f634-e5a8-441b-bfa1-2f024a996f3f)

## Output

![Screenshot 2025-06-17 172222](https://github.com/user-attachments/assets/1e5d25dc-bcc4-4442-9f67-92de55f81c70)


## 🛠️ Ongoing Changes

- Improving detection accuracy of nested loops and compound conditions  
- Adding function-level complexity analysis  
- Modularizing logic for better extensibility

---

## 🔮 Future Scope

🛠️ **C++ Rewrite**: Rebuilding the core engine in C++ to support multiple languages and boost performance.  
🌐 **Multi-language Analysis**: Extend support to C++, Java, and JavaScript using language grammars from Tree-sitter.  
🖥️ **User Interface**: Build a web-based frontend where users can upload code and view visual complexity reports.  
📊 **Interactive Dashboard**: Show complexity breakdowns, suggestions for optimization, and coding insights.

---

## 📥 Example Output

```
Algorithm Analysis Report:
Loops Detected: 2
Recursive Calls: 1
Estimated Time Complexity: O(n)
Estimated Space Complexity: O(n)
```

---

## 🤝 Contributing

Want to help? Feel free to fork this repository, make improvements, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License – see the `LICENSE` file for details.

---

## 👨‍💻 Author

**Prince**  
B.Tech CSE | Developer | AI & Software Enthusiast  
[GitHub](http://github.com/princee01) | [LinkedIn](https://www.linkedin.com/in/prince-kumar99107/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
