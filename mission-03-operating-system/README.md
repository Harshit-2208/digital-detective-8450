# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to investigate how the operating system (OS) serves as the primary resource manager and abstraction layer between hardware components and user applications. This includes:
1. Inspecting OS platform details, active account identity, available disk storage, and active system processes while preserving privacy.
2. Understanding process execution, the Process Identifier (PID) column, and differentiating between foreground and background processes.
3. Distinguishing between absolute and relative file paths, and analyzing POSIX file permissions (`r`, `w`, `x`) on user files.
4. Explaining the six fundamental responsibilities of modern operating systems with real-world examples.

---

## 2. Work completed
- **Task 3.1 (OS Exploration)**: Queried system details using `sw_vers`, `uname -srm`, `whoami`, `df -h /`, and inspected system activity. Consolidated findings into a privacy-safe observation table where sensitive usernames and device names are replaced with `[redacted]`.
- **Task 3.2 (Process Management)**: Analyzed process fundamentals, identified the purpose of the PID column, and documented concrete examples of running processes (including system daemons and user applications).
- **Task 3.3 (Paths & Permissions)**: Navigated between the project root and subdirectories to demonstrate path translation, detailed the distinction between absolute and relative paths with project-specific examples, and broke down the permission bits (`-rw-r--r--`) of `terminal-practice/practice.txt`.
- **Task 3.4 (OS Responsibilities Table)**: Formulated comprehensive, original explanations and real-world computing examples for Process Management, Memory Management, Device Management, File Management, User Interface/Shell, and Security/Permissions.

---

## 3. Commands / tools used
| Command | Options / Args | Purpose |
| :--- | :--- | :--- |
| `sw_vers` | default | Checked macOS product name, version, and build version. |
| `uname` | `-srm` | Displayed OS kernel name (`Darwin`), release version, and hardware architecture (`arm64`). |
| `whoami` | default | Displayed currently logged-in active user account. |
| `df` | `-h /` | Displayed total, used, available, and percentage capacity of the root solid-state disk filesystem. |
| `ps` / `top` | `aux` / `-l 1` | Inspected running processes, CPU load, and memory usage. |
| `ls` | `-l <file>` | Inspected POSIX file attributes, owner, group, and permissions. |
| `cd` / `pwd` | relative paths | Navigated folder hierarchies and verified path changes. |

---

## 4. My understanding

### Task 3.1 — Explore your operating system

#### System Exploration Table
| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the commercial OS distribution, underlying UNIX kernel family, and CPU architecture. | `macOS 27.2 (Build 26B123), Kernel: Darwin arm64 (Apple Silicon)` |
| **Current account identity** | Confirms the username and privilege context executing terminal commands. | `[redacted]` (Non-root standard user account) |
| **Available and used storage** | Shows overall storage capacity, consumed gigabytes, free space, and mount points on the main SSD. | `Total: 926 GiB, Used: 13 GiB, Available: 771 GiB (Capacity: 2% utilized on /dev/disk3s1s1)` |
| **System activity snapshot** | Provides real-time metrics on CPU load, thread distribution, memory occupancy, and active process states. | Multi-core CPU load active, unified memory shared between kernel and applications, `launchd` managing services. |

---

### Task 3.2 — Understand processes

#### 1. What is a process?
A **process** is an active, executing instance of a computer program. When a program resides on disk, it is simply passive stored code (a binary or script). When launched, the operating system kernel loads its machine code into memory, allocates dedicated memory segments (address space containing code, global variables, stack, and heap), assigns system resources (such as file handles and network sockets), and schedules its execution threads across CPU cores.

#### 2. What does the PID column represent?
The **PID (Process Identifier)** is a unique, positive integer assigned by the operating system kernel to each running process at the moment of its creation. The PID serves as an unambiguous handle that allows the operating system, administrative utilities, and other programs to track, communicate with, send signals to (such as `SIGTERM` or `SIGKILL`), and adjust the scheduling priority of that specific process. When a process terminates, its PID is freed and eventually recycled by the kernel.

#### 3. Two examples of processes running on the computer:
1. **`launchd` (PID 1)**: The root bootstrap daemon and init process on macOS. Spawned directly by the kernel during system startup, it initializes system services, monitors daemons, and manages the execution lifecycle of all background user sessions.
2. **`zsh` (Interactive Shell Process)**: The command-line interpreter process hosting the current terminal session. It reads keyboard input commands from the user, forks child processes to execute external binaries (like `git` or `python3`), and manages shell environment variables.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Path vs Relative Path
- **Absolute Path**: An absolute path specifies the complete, unambiguous location of a file or directory starting from the very root of the filesystem (`/`). It is globally valid regardless of which folder the user is currently located in.
  - *Example from assignment*: `/Users/[redacted]/Desktop/digital-detective-8450/mission-03-operating-system/README.md`
- **Relative Path**: A relative path specifies the location of a target file or folder starting from the current working directory (`pwd`). It relies on contextual navigation symbols such as `.` (the current directory) and `..` (the parent directory).
  - *Example from assignment*: While in `digital-detective-8450/`, navigating to this mission file uses the relative path: `mission-03-operating-system/README.md` (or `../mission-02-terminal/README.md` from inside this folder).

#### POSIX File Permissions
Inspecting `terminal-practice/practice.txt` with `ls -l` yields:
```text
-rw-r--r--@ 1 [redacted] staff 88 Nov 15 23:28 practice.txt
```

#### Permission Breakdown:
- The leading `-` indicates a regular file (as opposed to `d` for directory).
- The next 9 characters are grouped into three distinct permission triplets:
  1. **Owner (`rw-`)**: The file's creator/owner has **Read** (`r`) and **Write** (`w`) permissions, but **no Execute** (`-`) permission. The owner can view and modify the file contents, but cannot execute it as a binary/script.
  2. **Group (`r--`)**: Members of the `staff` group have **Read-only** permission. They can open and view the file, but cannot alter or delete its contents.
  3. **Others (`r--`)**: All other accounts on the system have **Read-only** permission.

#### Permission Types Table
| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **`r` — Read** | Grants permission to open, view, and read the contents of a file. On a directory, allows listing its files (`ls`). | Opening and reading a text document or source code file. |
| **`w` — Write** | Grants permission to modify, overwrite, append to, or truncate a file. On a directory, allows creating and deleting files. | Editing code, saving document changes, or creating a new file in a folder. |
| **`x` — Execute** | Grants permission to run a compiled binary or script as a program. On a directory, grants permission to traverse/enter it (`cd`). | Executing a Python script (`./script.py`), running a shell binary, or entering a directory. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | The OS controls program lifecycles, creates and terminates processes, schedules execution time across CPU cores via time-slicing, and enables inter-process communication. | The CPU scheduler switches execution rapidly between your web browser, code editor, and music player so they appear to run simultaneously. |
| **Memory management** | The OS allocates and tracks chunks of primary RAM for active programs, guarantees process memory isolation so one crashing app cannot corrupt another, and manages virtual memory paging when physical RAM is full. | When launching a heavy graphic design tool, the OS assigns it a dedicated 4 GB virtual memory space while keeping the background terminal's memory protected. |
| **Device management** | The OS communicates with hardware peripherals using standardized device drivers, translating generic software requests into hardware-specific electrical commands. | When you click "Print" in a document, the OS print spooler and printer driver format the pages and stream data over USB or Wi-Fi to the physical printer. |
| **File management** | The OS organizes data into structured files and hierarchical directories on storage media, tracks file metadata (size, timestamps, inodes), and enforces file locking. | The Apple File System (APFS) manages file paths, directory trees, file creation, and quick cloning when copying files on the SSD. |
| **User interface / shell** | The OS provides an accessible interface for humans to control the computer, available as either a Graphical User Interface (GUI) with windows and pointers or a Command-Line Interface (CLI) shell. | Clicking desktop icons in macOS Finder or typing `mkdir` and `git commit` commands in the Zsh Terminal shell. |
| **Security and permissions** | The OS protects system integrity and user privacy by enforcing authentication, separating user and administrator privileges, validating file access control lists (ACLs), and sandboxing untrusted applications. | Preventing a regular user or standard script from altering protected root kernel files in `/System` without explicit administrator authorization. |

---

## 5. Difficulties faced
- **Understanding Multi-tenant Permission Triplets**: Remembering which three characters in `-rw-r--r--` belong to Owner, Group, and Others, and how directory execute (`x`) permissions differ from file execute permissions (directory `x` permits traversing via `cd`).
- **Process Isolation Concepts**: Visualizing how the OS kernel enforces boundary protection between separate processes running in RAM.

---

## 6. How I resolved them
- **Deconstructed `ls -l` Triplet Structure**: Memorized the structure: 1 type character + 3 owner bits + 3 group bits + 3 other bits. Tested file reading and script execution flags.
- **Reviewed Architectural Models**: Studied the role of virtual memory management (page tables and MMU hardware) to understand how the OS prevents processes from accessing memory outside their assigned virtual address space.

---

## 7. Evidence / files
- Mission 3 Documentation: [mission-03-operating-system/README.md](README.md)
- Root Overview: [README.md](../README.md)
- Terminal Practice File Inspected: [terminal-practice/practice.txt](../terminal-practice/practice.txt)

---

## 8. Commit details
- **Commit Message**: `Document operating system and file management`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
