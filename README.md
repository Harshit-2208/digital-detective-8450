# The Digital Detective: Explore Your Computer • Build a Mini System Report

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.13+](https://img.shields.io/badge/Python-3.13.15-blue.svg)](https://www.python.org/)
[![Git: 2.55+](https://img.shields.io/badge/Git-2.55.0-orange.svg)](https://git-scm.com/)

An investigative, hands-on computer systems report exploring hardware architectures, POSIX terminal operations, operating system process and memory management, compilers versus interpreters, binary data representations, Git collaboration workflows, and computer networking.

---

## Student Information
| Parameter | Details |
| :--- | :--- |
| **Assignment** | The Digital Detective — Diwali Independent Learning Assignment |
| **Repository Name** | `digital-detective-8450` |
| **GitHub Username** | `Harshit-2208` |
| **Repository URL** | [https://github.com/Harshit-2208/digital-detective-8450](https://github.com/Harshit-2208/digital-detective-8450) |
| **USN Identifier** | `8450` (Last four digits) |
| **Platform** | macOS 27.2 (Darwin arm64 / Apple Silicon) |

> **Privacy Notice**: In strict adherence to assignment instructions, all personal identifiable information (usernames, local network IP addresses, Wi-Fi SSIDs, device hardware serials, and system credentials) has been sanitized or designated as `[redacted]`.

---

## Mission Index & Completion Matrix
Every mission is isolated within its dedicated directory and accompanied by an extensive, standardized 8-part `README.md`. Each was committed and pushed sequentially.

| Mission | Directory | Focus / Topic | Primary Deliverables | Status |
| :---: | :--- | :--- | :--- | :---: |
| **0** | [mission-00-setup/](mission-00-setup/README.md) | Repository & Workspace Setup | Naming convention, folder hierarchy, tool verification | **Completed** |
| **1** | [mission-01-computer-basics/](mission-01-computer-basics/README.md) | Computer Fundamentals & IPOS | IPOS activity trace, HW/SW taxonomy, embedded systems | **Completed** |
| **2** | [mission-02-terminal/](mission-02-terminal/README.md) | Terminal & File Management | POSIX command reference, safe redirection, pipelines, Homebrew | **Completed** |
| **3** | [mission-03-operating-system/](mission-03-operating-system/README.md) | Operating System & Permissions | Kernel inspection, process analysis (PID), paths, POSIX permissions | **Completed** |
| **4** | [mission-04-programs/](mission-04-programs/README.md) | How Programs Run | `hello.py` execution, Compiler vs Interpreter matrix | **Completed** |
| **5** | [mission-05-numbers-data/](mission-05-numbers-data/README.md) | Numbers, Data & Text Encoding | Manual math derivations, Python verification, `number_converter.py`, ASCII/UTF-8 | **Completed** |
| **6** | [mission-06-git-github/](mission-06-git-github/README.md) | Git, GitHub & Collaboration | `update-about` branch, PR proposal & merge, Git command glossary | **Completed** |
| **7** | [mission-07-networking/](mission-07-networking/README.md) | Computer Networks | LAN/WAN taxonomy, live `ping`/`nslookup` diagnostics, 6-step website lifecycle | **Completed** |
| **8** | [mission-08-final-report/](mission-08-final-report/README.md) | Final Review & Submission | Repository audit, checklist verification, submission metadata | **Completed** |

---

## Topics Explored
Across the nine missions of this assignment, the following fundamental computer science concepts were investigated:
1. **Computer Architecture & The IPOS Cycle**:
   - Tracing data transformation through **Input** (sensors, key switches), **Processing** (CPU arithmetic/logic, RAM caching), **Output** (GPU framebuffers, displays), and **Storage** (non-volatile NVMe flash, filesystems).
   - Classifying software into Operating Systems, Applications, and Utility software.
   - Analyzing dedicated embedded systems (ATMs, smart traffic controllers, microwave controllers).
2. **Command-Line Interface Mastery**:
   - Navigation (`pwd`, `cd`), inspection (`ls`, `ls -lah`), file operations (`mkdir`, `touch`, `cp`, `mv`, `cat`).
   - Standard I/O streams and redirection: overwrite (`>`) versus safe append (`>>`).
   - Inter-process communication conduits: Unix pipelines (`|`) streaming stdout into stdin.
   - Package managers (Homebrew) for automated dependency resolution and software lifecycle management.
3. **Operating System Fundamentals**:
   - Kernel abstractions, CPU thread scheduling, memory virtualization, device drivers, and filesystem hierarchies.
   - Process lifecycles, Process Identifiers (PIDs), foreground versus background daemon architectures.
   - Filesystem navigation using absolute versus relative paths.
   - POSIX security and permission triplets (`rwx` for Owner, Group, and Others).
4. **Program Execution Paradigms**:
   - Ahead-of-Time (AOT) machine compilation (C/C++, Rust) versus Just-in-Time / runtime bytecode interpretation (Python).
   - Execution performance, memory overhead, optimization, and platform portability trade-offs.
5. **Data Representation & Encodings**:
   - Mathematical conversions between Decimal (base 10), Binary (base 2), and Hexadecimal (base 16).
   - Binary bitmasks and hexadecimal nibble compaction ($2^4 = 16$).
   - Character encoding history: 7-bit ASCII code points versus variable-length UTF-8 universal Unicode representations.
6. **Distributed Version Control & Collaboration**:
   - The three-tier Git architecture: working directory, staging area (index), and cryptographic commit log.
   - Non-destructive feature branching (`git checkout -b <branch>`).
   - Pull Requests (PRs), code reviews, and upstream branch merging.
7. **Computer Networks & Web Transactions**:
   - Network scopes: Local Area Networks (LAN), Metropolitan Area Networks (MAN), and Wide Area Networks (WAN).
   - Protocols (TCP/IP, HTTPS, ICMP, DNS), packet switching, and client-server architectures.
   - Diagnosing live network latency and reachability using `ping` and `nslookup`.
   - The complete 6-stage lifecycle of an HTTP/HTTPS web request.

---

## How to Run the Number Converter
The Python number converter built in Mission 5 accepts an input decimal integer and outputs its binary and hexadecimal equivalents.

### Prerequisites
- Python 3.8+ installed (tested on `Python 3.13.15`).

### Execution Instructions
You can execute the converter either directly from the repository root or from within the `mission-05-numbers-data/` folder:

**Option 1: Running from repository root**
```bash
python3 mission-05-numbers-data/number_converter.py
```

**Option 2: Running from within the mission folder**
```bash
cd mission-05-numbers-data
python3 number_converter.py
```

### Sample Interactive Session
```text
=============================================
   Digital Detective: Number Converter
=============================================
Enter a positive decimal number: 25

--- Conversion Results ---
Decimal (Base 10):     25
Binary (Base 2):       0b11001  (Raw: 11001)
Hexadecimal (Base 16): 0X19  (Raw: 19)
=============================================
```

---

## My Learning
Through this assignment, I developed a deeper understanding of how modern computers operate beneath the graphical user interface:
- **Demystifying the Machine**: Interacting directly with the kernel and terminal removed the "black box" abstraction of computers. Understanding that a simple keypress triggers hardware interrupts, CPU cache allocations, and GPU framebuffer updates changed how I view everyday software.
- **The Elegance of the Unix Philosophy**: Discovering command pipelines (`|`) demonstrated the power of small, single-purpose tools that combine seamlessly to solve complex data processing tasks without writing custom code.
- **Architectural Rigor & Data Integrity**: Working through manual binary-to-hexadecimal derivations and character encodings made concrete how physical electrical voltages translate into logical computations and multilingual text.
- **Professional Engineering Habits**: Maintaining an isolated feature branch (`update-about`), documenting every milestone, sanitizing sensitive data, and maintaining a clean Git commit history reinforced professional version control hygiene.

---

## Verification & Commit Discipline Note
In strict accordance with the assignment guidelines:
- Every mission was undertaken sequentially.
- Each mission folder contains its own self-contained `README.md` following the standardized 8-part template.
- Work for each mission was staged and committed individually with clear, meaningful commit messages before proceeding to subsequent tasks.
- All branches and commits are synchronized with the public GitHub remote repository.
