# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand how computer hardware represents, manipulates, and stores information at the lowest architectural level using binary digits (bits), hexadecimal notation, and character encoding standards. This involves:
1. Performing manual, step-by-step mathematical conversions between decimal (base-10), binary (base-2), and hexadecimal (base-16).
2. Verifying all mathematical calculations using Python's built-in conversion functions in the interactive environment.
3. Authoring and testing an interactive Python script (`number_converter.py`) that accepts user decimal input and renders binary and hexadecimal equivalents.
4. Analyzing text encoding mechanisms, examining ASCII codes for uppercase and lowercase characters, and explaining why universal encoding standards like UTF-8 are essential.

---

## 2. Work completed
- **Task 5.1 (Manual Conversions)**: Completed full mathematical derivations showing successive division-by-2 for decimal-to-binary, positional expansion powers-of-2 for binary-to-decimal, base-16 positional expansion, and 4-bit nibble grouping for binary-to-hexadecimal.
- **Task 5.2 (Python Interactive Verification)**: Evaluated all seven conversions in Python using `bin()`, `hex()`, and `int(string, base)`. Recorded exact expressions, outputs, and verified 100% agreement with manual derivations.
- **Task 5.3 (Interactive Converter Script)**: Developed `number_converter.py` in this mission directory. Tested the program with three distinct positive integers (13, 25, 255), logged the outputs, and explained the internal mechanics of `int()`, `bin()`, and `hex()`.
- **Task 5.4 (Text Encoding Investigation)**: Identified ASCII decimal values for `'A'` (65) and `'a'` (97), articulated why digital computers require mapping standards, and highlighted non-ASCII multibyte Unicode characters (such as the Euro symbol `€` and Devanagari character `अ`).

---

## 3. Commands / tools used
| Tool / Function | Example Syntax | Purpose |
| :--- | :--- | :--- |
| `bin()` | `bin(13)` | Converts an integer to an prefixed binary string (`'0b1101'`). |
| `hex()` | `hex(255)` | Converts an integer to an prefixed hexadecimal string (`'0xff'`). |
| `int(x, base)` | `int('1010', 2)` | Parses a string in specified base into a base-10 integer. |
| `ord()` | `ord('A')` | Returns the integer Unicode/ASCII ordinal value of a character. |
| `chr()` | `chr(65)` | Converts an integer ordinal code point back to its character glyph. |
| `python3` | `python3 number_converter.py` | Executed the standalone converter CLI application. |

---

## 4. My understanding

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
- **Method**: Successive integer division by 2, recording remainders from least significant bit (LSB) to most significant bit (MSB).
  - $13 \div 2 = 6$ with remainder **1** (LSB)
  - $6 \div 2 = 3$ with remainder **0**
  - $3 \div 2 = 1$ with remainder **1**
  - $1 \div 2 = 0$ with remainder **1** (MSB)
- Reading remainders from bottom to top (MSB to LSB):
  $$\mathbf{13_{10} = 1101_2}$$

#### 2. Convert decimal 25 to binary
- **Method**: Successive integer division by 2:
  - $25 \div 2 = 12$ with remainder **1** (LSB)
  - $12 \div 2 = 6$ with remainder **0**
  - $6 \div 2 = 3$ with remainder **0**
  - $3 \div 2 = 1$ with remainder **1**
  - $1 \div 2 = 0$ with remainder **1** (MSB)
- Reading remainders from bottom to top:
  $$\mathbf{25_{10} = 11001_2}$$

#### 3. Convert binary 1010 to decimal
- **Method**: Positional expansion using powers of 2 ($2^3, 2^2, 2^1, 2^0$):
  $$(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$$
  $$= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$$
  $$= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$$

#### 4. Convert binary 1101 to decimal
- **Method**: Positional expansion using powers of 2 ($2^3, 2^2, 2^1, 2^0$):
  $$(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$$
  $$= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$$
  $$= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$$

#### 5. Convert hexadecimal A to decimal
- **Method**: In base-16 notation, the symbols $0\text{--}9$ represent values 0 through 9, and letters $A\text{--}F$ represent 10 through 15.
  $$A_{16} = 10 \times 16^0 = \mathbf{10_{10}}$$

#### 6. Convert hexadecimal 1F to decimal
- **Method**: Positional expansion using powers of 16 ($16^1, 16^0$), where $F = 15$:
  $$(1 \times 16^1) + (F \times 16^0) = (1 \times 16) + (15 \times 1)$$
  $$= 16 + 15 = \mathbf{31_{10}}$$

#### 7. Convert binary 1111 to hexadecimal
- **Method**: Every group of 4 binary bits (one nibble) directly maps to exactly one hexadecimal digit ($2^4 = 16$).
  $$1111_2 = (1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$$
  In hexadecimal, decimal value 15 is designated by the symbol **F**.
  $$\mathbf{1111_2 = F_{16}}$$

---

### Task 5.2 — Verify using Python

#### Python Interactive Verification Table
| Conversion Task | Python Expression Tested | Interactive Output | Matches Manual Calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to Binary | `bin(13)` | `'0b1101'` | Yes (`1101_2`) |
| Decimal 25 to Binary | `bin(25)` | `'0b11001'` | Yes (`11001_2`) |
| Binary 1010 to Decimal | `int('1010', 2)` | `10` | Yes (`10_10`) |
| Binary 1101 to Decimal | `int('1101', 2)` | `13` | Yes (`13_10`) |
| Hexadecimal A to Decimal | `int('A', 16)` | `10` | Yes (`10_10`) |
| Hexadecimal 1F to Decimal | `int('1F', 16)` | `31` | Yes (`31_10`) |
| Binary 1111 to Hexadecimal | `hex(0b1111)` | `'0xf'` | Yes (`F_16`) |

*Note on Python Output Prefixes*: Python prefixes binary string representations with `0b` (e.g. `0b1101`) and hexadecimal representations with `0x` (e.g. `0xf`) to explicitly indicate the numeric base and distinguish them from standard base-10 numerals.

---

### Task 5.3 — Build a small number converter

#### Program Implementation
The script is located in [number_converter.py](number_converter.py). It prompts the user for a decimal integer, parses the input string into a native integer via `int()`, converts it using `bin()` and `hex()`, and outputs both formatted strings.

#### Execution Test Results Table
| Test Number (Decimal) | Binary Output | Hexadecimal Output | Observation |
| :---: | :--- | :--- | :--- |
| **13** | `0b1101` (Raw: `1101`) | `0XD` (Raw: `D`) | Matches Task 5.1 manual calculations exactly. |
| **25** | `0b11001` (Raw: `11001`) | `0X19` (Raw: `19`) | $1 \times 16 + 9 = 25$; binary requires 5 bits. |
| **255** | `0b11111111` (Raw: `11111111`) | `0XFF` (Raw: `FF`) | Complete 8-bit byte saturated (all 1s), maps to double nibble `FF`. |

#### How `bin()` and `hex()` Function
- `bin(x)`: Accepts an integer argument $x$ and returns an exact string representation in base-2 prefixed with `'0b'`. Internally, it extracts the binary bitmask of the integer stored in CPU registers.
- `hex(x)`: Accepts an integer argument $x$ and returns its base-16 equivalent prefixed with `'0x'`. Because four binary bits map directly to one hexadecimal digit ($2^4 = 16$), hexadecimal provides a compact, human-readable shorthand for representing long binary bitstreams and memory addresses.

---

### Task 5.4 — How is text stored?

#### 1. ASCII Decimal Codes for 'A' and 'a'
- Uppercase Letter **`'A'`**: ASCII Decimal **`65`** (Binary: `01000001`, Hex: `0x41`).
- Lowercase Letter **`'a'`**: ASCII Decimal **`97`** (Binary: `01100001`, Hex: `0x61`).
- *Insight*: The difference between uppercase and lowercase letters in ASCII is exactly $97 - 65 = 32$ (which corresponds to setting the 6th bit, $2^5 = 32$).

#### 2. Why does a computer need an encoding standard?
Digital computer processors and electronic memory circuits operate exclusively on binary electrical states—high voltage (1) and low voltage (0). Computers have no inherent physical concept of letters, punctuation, or symbols. Therefore, an agreed-upon encoding standard (such as ASCII or UTF-8) is required to establish a universally consistent translation dictionary that maps each character glyph to a specific numeric integer code, ensuring that text written on one machine is displayed identically on any other machine worldwide without corruption.

#### 3. Character not in basic ASCII
- **Basic ASCII** is a 7-bit encoding standard encompassing only 128 code points (0 through 127), which covers basic English letters, digits, and control characters.
- **Example of non-ASCII character**:
  - The Euro currency symbol: **`€`** (Unicode code point `U+20AC`, represented in UTF-8 by the 3-byte sequence `0xE2 0x82 0xAC`).
  - The Devanagari letter: **`अ`** (Unicode code point `U+0905`, encoded in UTF-8 by `0xE0 0xA4 0x85`).
  - An emoji such as: **`🚀`** (Unicode code point `U+1F680`, encoded in UTF-8 by 4 bytes).

---

## 5. Difficulties faced
- **Reading Order in Division Method**: Remembering that in successive division-by-2, the first remainder calculated represents the Least Significant Bit (LSB / $2^0$) and the last remainder represents the Most Significant Bit (MSB / $2^n$). Reading top-to-bottom instead of bottom-to-top reverses the binary number.
- **Prefix Handling in Python**: Distinguishing between Python's internal prefix formatting (`0b`, `0x`) and mathematical base notation.

---

## 6. How I resolved them
- **Double-checking via Positional Expansion**: Always verified division results by multiplying the resulting bits by their positional powers of 2.
- **Clear String Presentation**: Designed `number_converter.py` to display both the standard Python prefixed string and the clean raw digits (via string slicing `[2:]`).

---

## 7. Evidence / files
- Mission 5 Documentation: [mission-05-numbers-data/README.md](README.md)
- Executable Converter Program: [mission-05-numbers-data/number_converter.py](number_converter.py)
- Root Overview: [README.md](../README.md)

---

## 8. Commit details
- **Commit Message**: `Build number converter and practise data representation`
- **Target Branch**: `main`
- **Remote Visibility**: Staged, committed locally, and pushed to remote GitHub repository `https://github.com/Harshit-2208/digital-detective-8450`.
