# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
The objective of Mission 0 was to establish the workspace for the Digital Detective assignment. This involved naming the repository according to the required specification (`digital-detective-<last 4 digits of USN>`), validating the installation and versions of required local development tools (Python 3 and Git), initializing the standardized directory structure for all nine missions (Missions 0 through 8), creating the root `README.md`, and linking the local workspace to the remote GitHub repository.

---

## 2. Work completed
- **Repository Naming**: Named the local folder and GitHub repository `digital-detective-8450`, incorporating the last four digits of the student USN (`8450`) with lowercase letters and no spaces.
- **Environment Verification**: Verified the active installation of Python 3 and Git using Terminal commands.
- **Directory & File Hierarchy**: Structured the workspace with folders for each mission (`mission-00-setup` through `mission-08-final-report`) and an `evidence/` directory for safe outputs and logs.
- **Initial Documentation**: Prepared the root `README.md` providing an overview, student details table, mission navigation index, and workflow guidelines.
- **Mission 0 Documentation**: Created this `mission-00-setup/README.md` documenting tool versions, architectural reasoning, and setup verification.

---

## 3. Commands / tools used
| Tool / Command | Exact Syntax | Purpose |
| :--- | :--- | :--- |
| **Python 3** | `python3 --version` | Checked the installed version of Python 3. |
| **Git CLI** | `git --version` | Verified the installed version of Git. |
| **Git Status** | `git status` | Inspected working tree status and branch state. |
| **Git Remote** | `git remote -v` | Confirmed the upstream remote connection URL to GitHub. |
| **Directory Creation** | `mkdir` | Created folders for each mission and the evidence folder. |

### Verified Tool Versions
- **Python Version**: `Python 3.13.15`
- **Git Version**: `git version 2.55.0`
- **Operating Environment**: `macOS 27.2 (Darwin arm64 / Apple Silicon)`

---

## 4. My understanding
### What is a Git Repository?
A Git repository is a digital storage structure managed by the Git version control system. Rather than just being a folder on a disk, a repository tracks changes to files over time by recording historical snapshots known as commits. This enables developers to maintain a verifiable audit trail of work, revert mistakes, test features on isolated branches without affecting main code, and collaborate reliably across distributed systems via remote hosting services like GitHub.

### Why Organise the Folder Structure by Mission?
Organising the project into discrete mission folders (`mission-00-setup/`, `mission-01-computer-basics/`, etc.) serves several key software engineering and pedagogical goals:
1. **Modularity & Separation of Concerns**: Each computing concept is self-contained. Exercises, scripts, and documentation for operating system concepts do not interfere with networking observations or number conversion code.
2. **Incremental Progression & Clear Milestones**: Dividing the assignment into numbered missions mirrors agile development sprints. Each mission has its own deliverables, verification steps, and dedicated commit boundary.
3. **Auditability & Easy Navigation**: Anyone reviewing or grading the repository can directly inspect the specific folder and read its standardized `README.md` without wading through a monolithic, disorganized root directory.

---

## 5. Difficulties faced
- **Empty Directory Tracking in Git**: By default, Git tracks only files, not empty directories. Creating the directory structure initially would leave empty folders uncommitted until files were added.
- **Naming Rule Precision**: Ensuring the repository name strictly matched the pattern `digital-detective-8450` without uppercase characters, spaces, or mismatched folder paths.

---

## 6. How I resolved them
- **Directory Persistence**: Created empty initial markdown files (`README.md`) within each mission directory and added a `.gitkeep` file inside the `evidence/` folder so that Git correctly captures and persists the entire organizational structure in the initial commit.
- **Verification via CLI**: Ran `git status` and inspected directory listings with `ls -la` to confirm that all folder names and file paths precisely adhere to the assignment specification.

---

## 7. Evidence / files
- Root documentation: [README.md](../README.md)
- Mission 0 documentation: [README.md](README.md)
- Workspace layout:
  ```text
  digital-detective-8450/
  ├── README.md
  ├── evidence/
  │   └── .gitkeep
  ├── mission-00-setup/
  │   └── README.md
  ├── mission-01-computer-basics/
  │   └── README.md
  ├── mission-02-terminal/
  │   └── README.md
  ├── mission-03-operating-system/
  │   └── README.md
  ├── mission-04-programs/
  │   └── README.md
  ├── mission-05-numbers-data/
  │   └── README.md
  ├── mission-06-git-github/
  │   └── README.md
  ├── mission-07-networking/
  │   └── README.md
  └── mission-08-final-report/
      └── README.md
  ```

---

## 8. Commit details
- **Commit Message**: `Set up Digital Detective mission structure`
- **Target Branch**: `main`
- **Remote Visibility**: Committed locally and pushed to GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
