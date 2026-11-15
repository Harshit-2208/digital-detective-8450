# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to investigate and document the fundamental operational cycle of computer systems—Input, Processing, Output, and Storage (IPOS). This involves:
1. Tracing an everyday computing activity across all four IPOS stages with specific hardware components.
2. Identifying and categorizing at least four hardware components and four software applications (distinguishing between Operating System, Application, and Utility software).
3. Analyzing three embedded or dedicated computer-based systems found in modern daily life outside of personal laptops and smartphones.

---

## 2. Work completed
- **Task 1.1 (IPOS Activity Trace)**: Traced the complete lifecycle of "Writing, editing, and saving a source code file or document" through Input, Processing, Output, and Storage stages, explaining the electrical, architectural, and data path transitions between each phase.
- **Task 1.2 (Hardware & Software Classification)**: Compiled a detailed classification table with 5 physical hardware components and 5 software items (covering OS, Application, and Utility software categories) with explicit technical purposes.
- **Task 1.3 (Everyday Computer Systems)**: Analyzed three ubiquitous embedded computing systems—an Automated Teller Machine (ATM), an Adaptive Smart Traffic Controller, and a Modern Digital Microwave Oven—documenting their core purpose, primary sensory/user inputs, and operational outputs.
- **Documentation**: Fully populated all tables and theoretical analyses according to the required 8-section mission template.

---

## 3. Commands / tools used
While Mission 1 focuses primarily on computer architecture and systems analysis, the following tools were used to verify local hardware architecture and inspect operating system attributes:
| Tool / Utility | Invocation | Purpose |
| :--- | :--- | :--- |
| **System Info** | `uname -m` | Verified machine processor architecture (`arm64` Apple Silicon). |
| **macOS Version** | `sw_vers` | Verified the underlying operating system environment (`macOS 27.2`). |
| **Storage Diagnostics** | `df -h /` | Checked the local mounted solid-state storage filesystem. |
| **Markdown Editor** | Text Editor / VS Code | Formatted structural tables and architectural explanations. |

---

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity**: Writing, compiling/formatting, and saving a Markdown lab report in an editor.

#### IPOS Stages Table
| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | The user presses mechanical keys on the keyboard to enter text and clicks the trackpad to position the cursor. | Keyboard (mechanical switches producing scan codes), Trackpad (capacitive touch sensor). |
| **Processing** | The keyboard microcontroller sends interrupt signals via the internal bus. The CPU executes the text editor's event loop, allocates character buffers in RAM, calculates font glyph layouts, and checks syntax in real time. | Central Processing Unit (Apple Silicon M-series cores), Primary Memory (Unified LPDDR RAM cache/bus). |
| **Output** | The graphics engine renders the formatted text and GUI cursor onto the display buffer, refreshing visual pixels at 60Hz/120Hz. An audible click sound confirms trackpad engagement. | High-resolution Retina Display (Liquid Retina screen panel), Taptic Engine / Internal Speakers. |
| **Storage** | When the user triggers the Save command (`Ctrl+S` or `Cmd+S`), the operating system's file system driver flushes the active buffer from volatile RAM into a permanent file block on non-volatile flash storage. | Solid-State Drive (NVMe NAND Flash controller), File System (APFS - Apple File System). |

#### Step-by-Step Data Flow Explanation
1. **From Input to Processing**: When a key is pressed, an electrical circuit completes. The keyboard's integrated controller translates the physical contact into a digital scan code, triggering a hardware interrupt. The OS kernel's input driver converts this into an ASCII/UTF-8 character code and places it onto the application event queue. The CPU loads the editor's active buffer from RAM into high-speed L1/L2 cache, appends the new character code, and recomputes document layout.
2. **From Processing to Output**: The CPU coordinates with the GPU to rasterize the font glyphs into a display frame buffer located in unified memory. The display controller reads this buffer and modulates pixels on the screen, updating the visual representation almost instantaneously with negligible input latency.
3. **From Processing to Storage**: Because RAM is volatile memory (its contents disappear if power is lost), persistent safety requires secondary storage. When "Save" is commanded, the OS kernel requests disk write operations via NVMe commands. The SSD controller writes the data blocks into NAND flash cells, updating file metadata in the APFS file allocation table so the file remains intact even after computer shutdown.

---

### Task 1.2 — Identify hardware and software
A computer system consists of tangible physical electronics (hardware) and intangible instructions/programs (software) that govern hardware operation.

#### Hardware & Software Classification Table
| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures tactile physical keystrokes and transmits digital scan codes to the host computer. |
| **Retina Monitor Display** | Hardware | Not applicable | Displays high-resolution graphical desktop interfaces, application windows, and readable text output. |
| **Apple Silicon M-Series CPU** | Hardware | Not applicable | Executes machine-level binary instructions, performs arithmetic and logic computations, and schedules system processes. |
| **NVMe Solid-State Drive (SSD)** | Hardware | Not applicable | Provides high-speed, non-volatile persistent storage for the operating system, installed applications, and user files. |
| **Unified System Memory (RAM)** | Hardware | Not applicable | High-bandwidth volatile working memory storing currently running programs, kernel instructions, and active data buffers. |
| **macOS (Darwin Kernel)** | Software | Operating system software | Manages physical hardware resources, provides abstraction layers (drivers, virtual memory), schedules CPU threads, and enforces file permissions. |
| **Visual Studio Code** | Software | Application software | Provides an integrated developer environment for writing, editing, debugging, and managing source code files. |
| **Google Chrome / Safari** | Software | Application software | Renders web standards (HTML/CSS/JS), manages network HTTP/HTTPS sessions, and facilitates interactive internet browsing. |
| **Activity Monitor / Disk Utility** | Software | Utility software | Diagnostic tool used to inspect real-time CPU/RAM usage, kill non-responsive processes, verify filesystem integrity, and partition disks. |
| **Zsh / Terminal** | Software | Utility software (OS Shell) | Command-line interface shell enabling direct interactive communication with the operating system kernel via shell commands and scripts. |

---

### Task 1.3 — Computer systems around you
Computing devices are not limited to generic laptops or smartphones; specialized embedded computer systems power vital public and industrial infrastructure.

#### Everyday Computer Systems Table
| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Provides 24/7 self-service cash dispensing, balance inquiries, and account deposits securely. | Encrypted numeric PIN pad / Smartcard EMV chip reader. | Mechanical motorized cash dispenser / Thermal paper receipt printer. |
| **Smart Traffic Signal Controller** | Regulates vehicular intersection flow dynamically based on real-time traffic volume to prevent congestion. | Inductive loop magnetic vehicle sensors embedded under road asphalt / Optical traffic radar cameras. | Multi-aspect LED traffic signal lanterns (Red, Yellow, Green) / Pedestrian countdown indicator display. |
| **Modern Digital Microwave Oven** | Regulates high-frequency electromagnetic radiation to heat food accurately according to preset power levels and duration. | Capacitive touch membrane keypad / Internal thermal infrared temperature sensor. | High-voltage magnetron tube power relay / Digital vacuum fluorescent or 7-segment LED countdown display. |

---

## 5. Difficulties faced
- **Distinguishing Utility Software from OS Software**: Some built-in utilities (like Activity Monitor, Terminal, or Disk Utility) ship directly with the operating system, making it easy to conflate them with core kernel functions.
- **Clarifying the Volatile vs Non-Volatile Boundary**: Ensuring the explanation clearly articulates why the Processing stage relies on volatile RAM while the Storage stage necessitates non-volatile NAND flash.

---

## 6. How I resolved them
- **Clear Conceptual Definitions**: Reviewed computer architecture definitions: the Operating System core (kernel) directly manages low-level hardware abstraction, while Utility software comprises supporting maintenance and diagnostic programs that run on top of the OS to help users manage system health.
- **Technical Rigor in IPOS Trace**: Explicitly traced memory registers and RAM to the Processing stage, and dedicated disk controller persistence to the Storage stage.

---

## 7. Evidence / files
- Mission 1 Documentation: [mission-01-computer-basics/README.md](README.md)
- Root Overview: [README.md](../README.md)

---

## 8. Commit details
- **Commit Message**: `Complete computer basics and IPOS mission`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
