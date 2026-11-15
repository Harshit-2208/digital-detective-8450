# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to develop practical competence with the command-line interface (CLI / Terminal). This includes:
1. Executing core POSIX directory and file management operations (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`) and recording observations.
2. Practising safe, non-destructive file editing techniques inside an isolated `terminal-practice` folder.
3. Understanding how command flags alter program behavior (`-l`, `-a`, `-h`) and how command pipelines (`|`) connect discrete programs.
4. Investigating system package managers (specifically Homebrew on macOS) and articulating their role in modern software environments.

---

## 2. Work completed
- **Task 2.1 (Core Terminal Operations)**: Executed all nine required operations inside the assignment repository and tabulated the command syntax, plain-language description, and observed system output.
- **Task 2.2 (Safe File Practice)**: Created an isolated `terminal-practice/` directory. Created `practice.txt`, wrote an initial line using standard output redirection (`>`), safely appended a second line using append redirection (`>>`), verified line preservation with `cat`, made a duplicate copy with `cp`, and renamed the backup using `mv`.
- **Task 2.3 (Flags & Pipelines)**: Compared vanilla `ls` with composite flag invocation `ls -lah` (long format, hidden dotfiles, human-readable file sizes). Constructed a pipeline (`ls -lah | head -n 5`) to pipe output streams, analyzing the contribution of each stage.
- **Task 2.4 (Package Management)**: Inspected Homebrew (`brew --version`), listed installed formulae and casks (`brew list`), and explained the architectural benefits of centralized dependency resolution.
- **Privacy Audit**: Sanitized all terminal paths and session logs to conceal personal usernames and device hostnames using `[redacted]`.

---

## 3. Commands / tools used
| Command / Syntax | Category | Purpose |
| :--- | :--- | :--- |
| `pwd` | Navigation | Print name of current / working directory. |
| `ls`, `ls -l`, `ls -lah` | File Inspection | List directory contents with various detail flags. |
| `cd ..`, `cd <dir>` | Navigation | Change working directory relative to current path. |
| `mkdir <dir>` | File Management | Create a new directory. |
| `touch <file>` | File Management | Create an empty file or update timestamp. |
| `echo "text" > <file>` | I/O Redirection | Overwrite / write text into a file. |
| `echo "text" >> <file>` | I/O Redirection | Append text to the end of an existing file. |
| `cat <file>` | File Inspection | Concatenate and print file contents to terminal. |
| `cp <source> <dest>` | File Management | Copy file to a new target path. |
| `mv <source> <dest>` | File Management | Move or rename a file or directory. |
| `head -n <lines>` | Text Utility | Output the first specified lines of text input. |
| `\|` (pipe symbol) | Shell Operator | Streams stdout of previous command into stdin of next command. |
| `brew --version`, `brew list` | Package Manager | Inspect package manager health and installed formula inventory. |

---

## 4. My understanding

### Task 2.1 — Basic Terminal Operations Table
| Operation / command name | What it does | What I observed (privacy-safe) |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full, absolute path from the root directory (`/`) to the active working folder. | `/Users/[redacted]/Desktop/digital-detective-8450` |
| **Directory listing (`ls`)** | Lists the visible names of files and folders in the current working directory in columnar layout. | Displayed `README.md`, `evidence`, `mission-00-setup`, ... `terminal-practice` |
| **Detailed listing (`ls -l`)** | Displays a formatted table including file permissions, link count, owner, group, byte size, modification timestamp, and filename. | Each entry displayed detailed metadata (e.g., `drwxr-xr-x`, 480 bytes, timestamps). |
| **Change directory (`cd ..` and `cd <dir>`)** | Updates the current shell environment pointer to the parent folder (`..`) or down into a child directory. | Changing to `..` placed the shell in `Desktop`; running `cd digital-detective-8450` safely returned to project root. |
| **Create directory (`mkdir terminal-practice`)** | Requests the OS filesystem allocate a new directory inode and namespace under the current path. | Directory was created silently without errors (standard Unix zero-status success). |
| **Create empty file (`touch practice.txt`)** | Creates a 0-byte file if it does not exist, or updates access and modification timestamps if it exists. | A new empty file appeared in `ls -l` with an initial size of 0 bytes. |
| **Copy file (`cp practice.txt practice_backup.txt`)** | Reads data from source file and writes an exact duplicate to a new target file inode. | Two separate files now exist; changes to one do not alter the other. |
| **Move / rename file (`mv practice_backup.txt practice_archive.txt`)** | Updates the directory table entry pointing to the file's data blocks, effectively renaming or moving it. | The old filename `practice_backup.txt` vanished and `practice_archive.txt` appeared in its place. |
| **Display file contents (`cat practice.txt`)** | Opens the file, reads its stream of stored characters, and prints them directly to standard output. | The two practice lines were rendered sequentially onto the terminal display. |

---

### Task 2.2 — Practise file changes safely
The operations were carried out inside `terminal-practice/`:
```bash
# 1. Write first line (truncate/create)
echo "Line 1: Exploring command line basics." > practice.txt

# 2. Append second line without removing first
echo "Line 2: Appending safe data without overwriting." >> practice.txt

# 3. Verify content
cat practice.txt
# Output:
# Line 1: Exploring command line basics.
# Line 2: Appending safe data without overwriting.

# 4. Duplicate and rename backup
cp practice.txt practice_backup.txt
mv practice_backup.txt practice_archive.txt
```

#### Analytical Questions & Answers:
1. **What is the difference between replacing a file's contents and adding text to the end?**
   - Using the single chevron redirector (`>`) *truncates* the destination file before writing. If the file already holds data, all existing content is erased and replaced by the new stream.
   - Using the double chevron redirector (`>>`) *appends* to the destination file. The operating system seeks directly to the end of the existing file stream and appends the new text, leaving all previous content completely intact.
2. **What is the difference between copying a file and moving a file?**
   - **Copying (`cp`)** duplicates the physical data. The OS allocates a new inode and writes a separate set of data blocks on storage. You end up with two independent files.
   - **Moving (`mv`)** updates the filesystem's directory catalog index without duplicating the underlying data blocks on disk (when within the same filesystem). The original reference ceases to exist, and only the new filename or location points to the data.
3. **What information does the current-directory display provide?**
   - The `pwd` (print working directory) command gives the absolute filesystem path starting from the root directory (`/`). It removes ambiguity about where commands will execute and where relative paths will resolve.
4. **Why is a directory-listing operation useful?**
   - Listing operations (`ls`) are essential for situational awareness in the CLI. They allow developers to confirm that files were created, verify exact spelling and capitalization, check read/write permissions, inspect file sizes, and verify modification timestamps.

---

### Task 2.3 — Understand flags and pipes

#### Flag Comparison: `ls` vs `ls -lah`
- Running plain `ls` only prints the names of visible files and folders in alphabetical columns.
- Adding flags changes the command's execution:
  - `-l`: Formats output into a detailed long table showing permissions, hard link count, owner, group, size, and modification date.
  - `-a`: Displays all directory entries, including hidden dotfiles (`.` for current directory, `..` for parent directory, and `.git` version control database).
  - `-h`: Human-readable size format; converts raw byte counts into intuitive units like `K`, `M`, or `G` (e.g., `3.2K` instead of `3276` bytes).

#### Pipeline Analysis: `ls -lah | head -n 5`
- **The Pipe Symbol (`|`)**: Acts as a unidirectional inter-process communication conduit in the shell. It connects the **standard output (stdout)** of the program on its left directly into the **standard input (stdin)** of the program on its right, eliminating the need to write intermediate temporary files to disk.
- **Left Side (`ls -lah`)**: Examines the filesystem and generates a comprehensive multi-line text stream containing all directory files and metadata.
- **Right Side (`head -n 5`)**: Consumes that text stream, intercepts the first 5 lines, prints them to the terminal display, and immediately closes the stream.

```text
Privacy-safe Pipeline Output:
total 8
drwxr-xr-x@ 15 [redacted]  staff   480B Nov 15 23:28 .
drwx------@ 37 [redacted]  staff   1.2K Nov 15 23:19 ..
drwxr-xr-x@ 12 [redacted]  staff   384B Nov 15 23:27 .git
-rw-r--r--@  1 [redacted]  staff   3.2K Nov 15 23:23 README.md
```

---

### Task 2.4 — Understand package managers

#### Environment Investigation
- **Package Manager Detected**: Homebrew (macOS)
- **Version**: `Homebrew 7.0.12`
- **Managed Packages Sample**:
  - *Formulae*: `git`, `curl`, `node`, `openjdk`, `openssl@3`, `sqlite`, `zstd`, `cmatrix`, `htop`, `ca-certificates`.
  - *Casks*: `codex`.

#### Why Package Managers are Useful
A package manager is a specialized software utility that automates the downloading, compiling, configuring, installing, upgrading, and removing of computer software packages through a centralized command line. Instead of manually searching the web for installer archives, verifying cryptographic checksums, and manually configuring library path variables, developers run a single command (e.g., `brew install git`). Crucially, package managers resolve complete dependency trees—if a tool requires five underlying shared libraries, the package manager installs all prerequisite dependencies in the correct order, prevents library version conflicts, and ensures clean uninstalls.

---

## 5. Difficulties faced
- **Shell Redirection Accidental Overwrite Risk**: In early command line practice, confusing `>` with `>>` can accidentally erase an important file's contents in an instant.
- **Sanitizing Multi-Column Output**: Detailed listings include username and group metadata by default, requiring careful redacting before publication to protect personal privacy.

---

## 6. How I resolved them
- **Deliberate Habit Building**: Strictly verified target filenames and ensured `>>` was used for progressive logging. Confirmed file line counts using `cat` and `wc -l`.
- **Systematic Privacy Redaction**: Substituted local user accounts with `[redacted]` in all recorded logs and tables.

---

## 7. Evidence / files
- Mission 2 Documentation: [mission-02-terminal/README.md](README.md)
- Terminal Practice Workspace: [terminal-practice/practice.txt](../terminal-practice/practice.txt)
- Terminal Practice Renamed Backup: [terminal-practice/practice_archive.txt](../terminal-practice/practice_archive.txt)

---

## 8. Commit details
- **Commit Message**: `Complete Terminal and file management mission`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
