# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to investigate the mechanics of computer program execution by:
1. Creating and executing a first Python script (`hello.py`) from the Terminal.
2. Comparing how compiled languages (compilers) and interpreted languages (interpreters) translate human-readable source code into machine instructions.
3. Analyzing the trade-offs in execution speed, portability, feedback loops, and output artifacts between both paradigms.

---

## 2. Work completed
- **Task 4.1 (Python Script Execution)**: Created `mission-04-programs/hello.py` containing `print("Hello from Python")`. Successfully ran the script using Python 3 via the command-line interface and captured the output.
- **Task 4.2 (Compiler vs. Interpreter Analysis)**: Constructed an analytical comparison table evaluating translation timing, output format, representative languages, and primary architectural advantages. Formulated an original comparative synthesis.
- **Documentation**: Completed this `README.md` adhering strictly to the required 8-part mission report specification.

---

## 3. Commands / tools used
| Tool / Command | Invocation / Syntax | Purpose |
| :--- | :--- | :--- |
| **Python 3 Interpreter** | `python3 mission-04-programs/hello.py` | Executed the Python script through the CPython virtual machine runtime. |
| **Python Interactive REPL** | `python3` | Tested interactive command interpretation and expression evaluation. |
| **File Creation** | Text Editor / `write_file` | Authored `hello.py` and mission documentation. |

---

## 4. My understanding

### Task 4.1 — Create and run a Python program
- **Source File**: `mission-04-programs/hello.py`
  ```python
  print("Hello from Python")
  ```
- **Execution Command**:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- **Observed Terminal Output**:
  ```text
  Hello from Python
  ```
- **Execution Mechanism**: When `python3` is invoked on the file, the CPython interpreter reads the text characters, parses the syntax into an Abstract Syntax Tree (AST), compiles the tree into intermediate Python bytecode instructions, and evaluates them sequentially within the Python Virtual Machine (PVM).

---

### Task 4.2 — Compare compiler and interpreter

#### Comparison Table
| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | **Ahead-of-Time (AOT)**: The compiler analyzes and translates the entire source code file completely into machine code before any execution begins. | **At Runtime**: The interpreter parses, translates, and executes the program instructions line-by-line or statement-by-statement dynamically while the program is running. |
| **Typical output** | A standalone executable binary file containing native machine code (such as a Mach-O binary on macOS or `.exe` on Windows). | Direct in-memory execution; no permanent standalone machine code binary is written to disk (though temporary bytecode caches like `.pyc` may be saved). |
| **One example** | **C / C++** (compiled using `clang` or `gcc`) or **Rust** (`rustc`). | **Python** (CPython engine) or **Ruby**. |
| **One advantage** | **Maximum Runtime Performance**: Because translation and optimization happen once prior to execution, compiled programs run at near-native hardware speed with zero interpreter overhead. | **Rapid Development & Portability**: Developers can test changes instantly without waiting for lengthy compilation steps, and the same script can run on any OS that has the interpreter installed. |

#### Comparative Explanation
A compiler and an interpreter represent two distinct strategies for bridging human-readable code and computer hardware. As illustrated in the table above, a compiler takes the entire program and translates it ahead-of-time directly into a standalone binary of native CPU machine instructions, allowing it to run with maximum efficiency and speed. In contrast, an interpreter processes source code dynamically at runtime, analyzing and executing statements on the fly without producing a separate machine-code binary. While compiled languages like C++ and Rust offer optimal performance for resource-intensive applications, interpreted languages like Python provide immediate feedback, simplified debugging, and great cross-platform portability.

---

## 5. Difficulties faced
- **Distinguishing Bytecode from Pure Machine Code**: Understanding that Python is not purely interpreted in the historical sense, but rather a hybrid system that compiles source code to an internal bytecode representation before interpreting it in the Python Virtual Machine.
- **Handling Pathing during Execution**: Ensuring the script is executed cleanly whether invoked from the repository root or from inside the `mission-04-programs` directory.

---

## 6. How I resolved them
- **Conceptual Clarification**: Documented the two-phase nature of modern interpreters (source code -> bytecode -> virtual machine evaluation loop) versus ahead-of-time machine code compilers.
- **Explicit Path Reference**: Verified execution using both relative workspace paths (`python3 mission-04-programs/hello.py`) and local execution (`cd mission-04-programs && python3 hello.py`).

---

## 7. Evidence / files
- Mission 4 Documentation: [mission-04-programs/README.md](README.md)
- Executable Python Program: [mission-04-programs/hello.py](hello.py)
- Root Overview: [README.md](../README.md)

---

## 8. Commit details
- **Commit Message**: `Compare compilers and interpreters`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
