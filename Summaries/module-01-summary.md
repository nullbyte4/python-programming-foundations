# Module 1 Summary: Running Programs and Basic Types

> Study summary for [Module 1 of the roadmap](../README.md#module-1-running-programs-and-basic-types).
> It explains the ideas behind the checklist; it does not replace the book or
> the exercises.

| | |
|---|---|
| **Reading** | Eric Matthes, *Python Crash Course*, 3rd Edition, Chapters 1-2 |
| **Deliverable** | [`exercises/module_01.py`](../exercises/module_01.py) |
| **Status** | Module 1 checklist complete in the README (practice sessions: 2026-10-27 and 2026-10-30) |
| **Next module** | Module 2: Collections, Loops, and Decisions (in progress; no summary yet) |

## How to read this document

Each section ends with a source note and is labeled by origin:

- **Book:** a claim checked against the original chapter text.
- **Engineering note:** a clarification or synthesis that goes beyond what the
  book states. It is general Python background, not a book quotation.
- **Original example:** a small example written for this summary, run on
  Python 3, and unrelated to the exercise solution.

## Map from the README checklist to this summary

| README skill | Section |
|---|---|
| Run a saved script; terminal versus `>>>` | [1](#1-running-python-terminal-repl-and-scripts) |
| Assign and reassign variables; names as labels | [2](#2-variables-names-are-labels) |
| Strings, f-strings, case, whitespace, `.strip()` | [3](#3-strings) |
| Integers, floats, arithmetic, rounding | [4](#4-numbers) |
| Read error messages | [5](#5-reading-error-messages) |
| `snake_case`, comments, readable formatting | [6](#6-names-comments-and-readability) |

## 1. Running Python: terminal, REPL, and scripts

**Book (Ch. 1, "Running Snippets of Python Code" and "Running Python Programs from
a Terminal"):** the three angle brackets (`>>>`) are the Python prompt. Code
after `>>>` runs in an interpreter session. A saved `.py` file is run with the
interpreter from the terminal. On Linux and macOS the book says to use
`python3` wherever it prints `python` (the Linux section states this
explicitly).

Two places, two languages:

| Where | What you type | Who reads it |
|---|---|---|
| Terminal prompt (`$`) | `python3 --version`, `python3 exercises/module_01.py` | the operating system's shell |
| Python prompt (`>>>`) | `print("hi")`, `x = 5` | the Python interpreter |

- Typing `print("hi")` at the shell prompt fails, because the shell does not
  speak Python. Typing `python3 --version` after `>>>` fails for the same
  reason in reverse.
- `python3` alone opens the interactive session. Leave it with `exit()` or
  `Ctrl-D`. This session is for short experiments.
- `python3 path/to/file.py` runs the file from the first line to the last. Run
  scripts from the repository root so relative paths behave as the README shows.

**Book (Ch. 2, "What Really Happens When You Run hello_world.py"):** the editor
or terminal passes the file to the Python interpreter, which reads the program and
determines what each word means.

**Engineering note:** use the REPL to ask quick questions ("what does `.strip()`
return?") and a script to keep work that should be repeatable.

## 2. Variables: names are labels

**Book (Ch. 2, "Variables Are Labels"):** variables are often described as boxes
that store values, but the book says it is more accurate to think of variables
as labels assigned to values, so a variable *references* a value. The author
notes this probably will not matter much in the first programs, but it is worth
learning early because it helps when behavior surprises you.

```python
level = "beginner"      # the name `level` refers to a string
level = "intermediate"  # the same name now refers to a different string
```

- Assignment (`=`) does not compare anything. It attaches a name to the value
  produced by the right-hand side.
- The right-hand side is evaluated first. Only then is the name attached.
- Reassignment moves the label. Earlier lines are not undone; code runs from
  top to bottom, so each `print()` shows the value the name has *at that line*.

**Why this matters later (engineering note):** in Module 2 you will meet objects
that can change while keeping the same label. Strings are the opposite case,
which is why the label model is worth learning now.

**Engineering note (naming):** the PEP 8 convention is lowercase words separated
by underscores (`total_minutes`), with names that say what the value means.
See [section 6](#6-names-comments-and-readability). The book's section "Naming
and Using Variables" covers its own rules; that section was not re-read for this
summary.

## 3. Strings

A string is text between quotes. Single or double quotes both work, which lets
you place one kind inside the other:

```python
print("It's fine")
print('He said "hi"')
```

An unmatched quote ends the string too early and causes a `SyntaxError`
(*Original example*: `print('it's')` reports `unterminated string literal`).

### Methods return new strings

**Book (Ch. 2, "Stripping Whitespace"):** `rstrip()` removes the extra space only
temporarily. Asking for the variable again shows the original value, and to
remove the whitespace permanently you assign the stripped value back to the
variable name. Its left-side and both-sides counterparts, `lstrip()` and
`strip()`, follow the same rule.

```python
note = "  rust ownership  "
note.strip()                  # returns 'rust ownership' ... and it is thrown away
print(repr(note))             # '  rust ownership  '  -> unchanged
note = note.strip().title()   # keep the result by reassigning
print(note)                   # Rust Ownership
```

Mental model: a string cannot be edited in place. A method such as `.strip()`,
`.title()`, `.upper()`, or `.lower()` builds a new string. If you do not give it a
name, it is lost.

Methods can be chained from left to right: `note.strip().title()` first strips,
then applies title case to the stripped result.

### f-strings

**Book (Ch. 2, "Using Variables in Strings"):** put the letter `f` immediately
before the opening quote and place variable names in braces; Python replaces
each with its value.

```python
language = "go"
minutes = 25
print(f"Studying {language.title()} for {minutes} minutes")
# Studying Go for 25 minutes
print("{language}")   # without the f prefix the braces are printed literally
```

Braces can also contain method calls such as `{language.title()}`.

**Engineering note:** when `.strip()` is given an argument, it removes any of
those *characters*, not an exact word. The book has a separate section,
"Removing Prefixes", for removing a specific prefix; that section was not
re-read for this summary, so read it before relying on it.

## 4. Numbers

**Book (Ch. 2, "Integers and Floats"):** dividing any two numbers always gives a
float, even when the result is whole (`4 / 2` gives `2.0`). Mixing an integer
with a float in other operations also gives a float.

| Operation | Meaning | Example result |
|---|---|---|
| `+`, `-`, `*` | add, subtract, multiply | `2 * 3.0` gives `6.0` |
| `/` | true division, always a float | `4 / 2` gives `2.0` |
| `**` | exponent | `3.0 ** 2` gives `9.0` |
| `( )` | change the order of evaluation | `(10 + 20) / 2` gives `15.0` |

### Order of operations

Multiplication and division happen before addition and subtraction, unless
parentheses say otherwise. This matters when computing an average or converting
units.

```python
print(10 + 20 / 2)    # 20.0   (divides first)
print((10 + 20) / 2)  # 15.0   (adds first)
```

### Floating-point surprises

**Book (Ch. 2, "Floats"):** `0.2 + 0.1` can give `0.30000000000000004`. The book says
this happens in all languages, is of little concern at this stage, and that it
returns to ways of dealing with it in Part II.

**Engineering note:** floats store binary approximations of most decimal
fractions. Do not rely on exact equality between computed floats, and do not use
plain floats where exact decimal amounts matter. These are cautions from general
Python practice, not a requirement of the book chapter.

### Underscores and constants

- **Book:** `14_000_000_000` is read as `14000000000`. Python ignores the
  underscores, which are only for readability.
- **Book (Ch. 2, "Constants"):** Python has no built-in constant type; programmers
  write the name in capitals (`MAX_CONNECTIONS = 5000`) to signal that it should
  not change.

## 5. Reading error messages

**Book (Ch. 2, "Avoiding Name Errors When Using Variables"):** when a program
cannot run, Python gives a *traceback*: a record of where it ran into trouble.
For a misspelled variable it reports the file, the line, the code that failed,
and the error type (`NameError`), usually with a "Did you mean" suggestion.

How to read one:

1. Read the **last line first**: the error type and message
   (`NameError: name 'x' is not defined`).
2. Find the **line number** and the code the interpreter shows.
3. Ask what is wrong in *that* line: a typo, a missing assignment, an unmatched
   quote.
4. Fix one thing, run again, and read the new message.

**Book (same section):** a name error usually means the value was never set or
the name was misspelled. Python can't identify the variable name provided.

Treat errors as information, not as proof that you failed. The Module 1
readiness test asks you to introduce a misspelled name on purpose and repair it
by reading the message rather than rewriting the program.

## 6. Names, comments, and readability

**Naming (PEP 8 convention, also used in the book's examples):** lowercase words
separated by underscores. For files too, the book suggests lowercase letters and
underscores, such as `simple_message.py`.

**Book (Ch. 2, "Comments"):** `#` starts a comment, and Python ignores everything
after it on that line. The book says the main reason for comments is to explain
what the code is supposed to do and how you made it work, and suggests writing a
comment when you considered several approaches before finding one that works.

**Book (Ch. 2, "The Zen of Python"):** `import this` prints Tim Peters' principles.
The chapter highlights beautiful over ugly, simple over complex, complex over
complicated, and readability counts.

**Engineering note:** comments that only repeat the code (`# add two numbers`)
add little. A good comment saves a future reader from re-deriving a decision.

## 7. Mistakes that appeared during practice

These are recorded from the study sessions, not from the book:

| Mistake or doubt | What clarified it |
|---|---|
| Expecting `.strip()` alone to clean the variable | Strings are immutable; assign the new string back |
| Unsure whether `a + b / 60` means `(a + b) / 60` | Compare `10 + 20 / 2` with `(10 + 20) / 2` |
| Forgetting the study topic in the final printed summary | Re-read the deliverable text before declaring it done |
| A typo in a variable name | Read the `NameError` line and its suggestion |

## 8. Self-check (answer in your own words, then verify in the REPL)

1. Which prompt reads `python3 --version`, and which reads `x = 5`? Why can't
   you swap them?
2. After `title = "  rust "` and `title.strip()`, what does `print(title)` show?
   Which one-line change keeps the cleaned text?
3. What does `10 + 20 / 2` print? What does `(10 + 20) / 2` print? Why do they
   differ, and why are both floats?
4. What happens if you remove the `f` from `print(f"{minutes} minutes")`?
5. A `NameError` mentions `lenght`. Which two places do you check first?
6. Why does the book consider `0.2 + 0.1` to be of little concern for now, and
   what would make it a concern later?

## 9. Connection to the next module

Module 2 builds on three ideas from this one:

- A name is a label, so two names can refer to the same object.
- Strings are immutable. Lists are not, and their methods behave differently
  (see the Module 2 summary when that module is complete).
- The traceback habit transfers directly to `IndexError` and `KeyError`.

## Sources and limits

- Eric Matthes, *Python Crash Course*, 3rd Edition, No Starch Press, 2023,
  Chapter 1 (`c01.xhtml`) and Chapter 2 (`c02.xhtml`). Section titles above
  match the book's headings, and the cited passages were read from the original
  EPUB in the local brain's `raw/` directory (not published here).
- Background and cross-checks:
  [source summary][pcc], [Python Variables and Execution Model][vars],
  [Python Strings and Text Processing][strings],
  [Python Numeric Types and Representation][numbers], and
  [Python Code Style and Philosophy][style]. These are local, private links and
  will not resolve on GitHub.
- The brain's concept pages mention CPython bytecode, garbage collection, and
  advice to comment only on *why*. The book passages read here do not state
  these, so they are excluded from this summary. See the
  [roadmap audit][audit].
- Ingested knowledge is not proof of mastery. Use the README readiness criteria
  and your own explanations to judge whether Module 1 is solid.

[pcc]: ../../../themainframe/wiki/sources/matthes-python-crash-course-2023.md
[vars]: ../../../themainframe/wiki/concepts/python-variables-and-execution-model.md
[strings]: ../../../themainframe/wiki/concepts/python-strings-and-text-processing.md
[numbers]: ../../../themainframe/wiki/concepts/python-numeric-types-and-representation.md
[style]: ../../../themainframe/wiki/concepts/python-code-style-and-philosophy.md
[audit]: ../../../themainframe/wiki/questions/python-phase-1-roadmap-audit.md
