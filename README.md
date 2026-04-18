Tokenizer Project

🧪 Example
Given the sample input:
`"This is a int sum=a+b=20;"
`

Output:

- IDENTIFIER: This
- IDENTIFIER: is
- IDENTIFIER: a
- KEYWORD: int
- IDENTIFIER: sum
- OPERATOR: =
- IDENTIFIER: a
- OPERATOR: +
- IDENTIFIER: b
- OPERATOR: =
- INT: 20
- SYMBOL: ;

---

📖 Overview
This project is a simple tokenizer implemented in Python.  
It scans through a source string and breaks it down into tokens such as:
- Keywords (int, float, if, else, return)
- Operators (=, +, -, *, /)
- Identifiers (variable names)
- Integers (numeric values)
- Symbols (other characters)

The tokenizer uses regular expressions to identify tokens and classify them.

---

🛠 Features
- Detects keywords and identifiers.
- Differentiates operators from other symbols.
- Handles integers correctly.
- Prints tokens in a structured format.

---
