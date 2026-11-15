# The Digital Detective: Explore Your Computer • Build a Mini System Report

## Project Overview
This repository contains the completed **Diwali Independent Learning Assignment — The Digital Detective**. The goal of this assignment is to investigate how a modern personal computer works from the ground up, gain practical comfort with the command-line interface (CLI/Terminal), explore operating system management of processes, storage, and permissions, understand data representations and character encoding, and apply Git and GitHub workflows to document and publish technical findings.

The assignment is structured into sequential missions (Missions 0 through 8). Each mission investigates a core area of computing, captures reproducible system observations, solves practical tasks, and is documented and committed separately to demonstrate incremental progress.

---

## Student Information
| Field | Details |
| :--- | :--- |
| **Assignment Name** | The Digital Detective — Diwali Independent Learning Assignment |
| **Repository Name** | `digital-detective-8450` |
| **GitHub Username** | `Harshit-2208` |
| **Repository URL** | [https://github.com/Harshit-2208/digital-detective-8450](https://github.com/Harshit-2208/digital-detective-8450) |
| **USN Identifier** | `8450` (Last 4 digits) |

> **Privacy Notice**: In accordance with the assignment guidelines, personal identifying details such as private IP addresses, Wi-Fi network names (SSIDs), computer hardware serial numbers, and account credentials have been kept private or marked as `[redacted]`.

---

## My Learning
Through the hands-on investigations conducted across these missions, I have developed a practical understanding of how computers function beneath graphical abstractions:
1. **The IPOS Cycle & Hardware Interaction**: I learned how physical user actions (like pressing keys) travel from hardware microcontrollers via interrupts into the CPU and RAM, render onto the display framebuffer, and persist to secondary SSD storage through filesystem drivers.
2. **Terminal Fluency & POSIX Pipelines**: Working directly in the shell deepened my understanding of file system navigation, file descriptors, and standard input/output redirection. I saw firsthand how the Unix pipe (`|`) connects independent programs together into powerful data processing streams without writing temporary files to disk.
3. **Data Representation & Encodings**: Performing manual base conversions and writing `number_converter.py` solidified how numbers are structured in binary bits, compacted into hexadecimal nibbles, and how text characters are mapped through universal encoding standards like ASCII and UTF-8.
4. **Git Branching & Collaborative Version Control**: Using isolated branches like `update-about` demonstrated how developers can draft, verify, and propose changes safely before merging them into the production `main` branch.

---

## Mission Index
| Mission | Directory | Focus / Topic | Status |
| :---: | :--- | :--- | :---: |
| **0** | [mission-00-setup/](mission-00-setup/README.md) | Repository and Workspace Setup | Completed |
| **1** | [mission-01-computer-basics/](mission-01-computer-basics/README.md) | Computer Fundamentals and IPOS | Completed |
| **2** | [mission-02-terminal/](mission-02-terminal/README.md) | Terminal and File Management | Completed |
| **3** | [mission-03-operating-system/](mission-03-operating-system/README.md) | Operating System, Processes, and Permissions | Completed |
| **4** | [mission-04-programs/](mission-04-programs/README.md) | How Programs Run: Compilers vs Interpreters | Completed |
| **5** | [mission-05-numbers-data/](mission-05-numbers-data/README.md) | Number Systems, Python, and Text Encoding | Completed |
| **6** | [mission-06-git-github/](mission-06-git-github/README.md) | Git, GitHub, Branches, and Pull Requests | In Progress |
| **7** | [mission-07-networking/](mission-07-networking/README.md) | Computer Networks and Communications | Planned |
| **8** | [mission-08-final-report/](mission-08-final-report/README.md) | Final Review and Submission Checklist | Planned |

---

## Workflow & Commit Discipline
Each mission is treated as an isolated milestone. As required by the assignment guidelines:
- Work is completed sequentially.
- A dedicated Git commit is created for each completed mission using a descriptive message.
- Each mission commit is pushed to the remote GitHub repository before work on the subsequent mission begins.
- Every mission directory features a standalone `README.md` following a standardized 8-part documentation structure.
