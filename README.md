# Python Programming Foundations

> **Phase 1 of the Software Engineering Roadmap**
>
> Learn to write, explain, debug, and test small Python programs before moving
> on to algorithms, systems, or frameworks.

The core reading is Eric Matthes' **Python Crash Course, 3rd Edition,
Part I: Basics (Chapters 1-11)**. These chapters are recorded as processed in
the local brain, *themainframe*; the book's overall coverage remains `partial`.
Part II and the appendices are not part of this core plan. Ingested knowledge
does **not** mean completed learning: checkboxes track demonstrated skills.

The module sequence follows the book. Deliverables, acceptance criteria, and
sections labeled **Engineering note** or **Practical extension** are original
learning-plan additions, not exercises or recommendations attributed to Matthes.
Book references link to the local brain and will not resolve on GitHub; chapter
and section titles remain usable without it. See [Sources](#sources).

## How to Use This Roadmap

1. Read the assigned chapter sections and write your own small examples.
2. Predict the output, run the program, and investigate differences.
3. Complete the module deliverable, including its edge cases.
4. Check a skill only when you can explain it and reproduce it without copying
   a solution. Use documentation when needed; memorizing APIs is not the goal.

Advance by demonstrated understanding, not a fixed calendar. Start with scripts
and manual checks; introduce automated tests in Module 5.

## Getting Started

Use Python 3 and a text editor. From a terminal, check your interpreter:

```bash
python3 --version
```

Running `python3` without a filename opens the interactive interpreter (REPL).
Use it for short experiments; save reusable programs in `.py` files.
After creating your first exercise, run it from the repository root:

```bash
python3 exercises/module_01.py
```

These commands use Linux/macOS conventions. On Windows, use `py` if `python3`
is unavailable. Follow [PCC, Chapter 1][pcc], "Getting Started", for the
platform-specific setup. The exercises and capstone below are **planned work**,
not implemented programs already included in this repository.

## Module 1: Running Programs and Basic Types

**Read:** [PCC, Chapters 1-2][pcc] - "Getting Started" and
"Variables and Simple Data Types".

- [ ] Run a saved script and distinguish terminal commands from Python code
  entered at the `>>>` prompt.
- [ ] Assign and reassign variables; understand names as labels referring to
  values rather than manually managed memory.
- [ ] Work with strings: quotes, f-strings, case changes, whitespace, and
  `.strip()`. Understand that string methods return new strings.
- [ ] Use integers, floats, arithmetic (`+`, `-`, `*`, `/`, `**`), and parentheses.
  Notice that floating-point calculations can produce small rounding differences.
- [ ] Read error messages and locate a syntax error or an undefined name.
- [ ] Use descriptive `snake_case` names, simple comments, and readable formatting.
  Apply PEP 8 conventions as they become relevant.

**Deliverable:** `exercises/module_01.py` prints a study-session summary using
a topic name and two session lengths in minutes. With 45 and 30 minutes, it
reports 75 minutes and 1.25 hours using arithmetic and an f-string.

**Ready to advance when:** changing the input variables changes the computed
summary correctly, and you can introduce and fix a misspelled variable name
by reading the error rather than rewriting the program blindly.

## Module 2: Collections, Loops, and Decisions

**Read:** [PCC, Chapters 3-6][pcc] - "Introducing Lists", "Working with Lists",
"if Statements", and "Dictionaries".

- [ ] Create lists; use indexing, negative indexes, `len()`, `.append()`,
  `.insert()`, `.pop()`, `.remove()`, and `del`. Recognize invalid indexes.
- [ ] Distinguish `.sort()`, which changes the list, from `sorted()`, which
  returns a new list.
- [ ] Write ordinary `for` loops with correct indentation. Use `range()` and
  simple aggregates such as `sum()`, `min()`, and `max()`.
- [ ] Use slices and distinguish `b = a` from `b = a[:]`. Create tuples,
  including a one-item tuple `(value,)`, and distinguish rebinding from mutation.
- [ ] Use booleans, comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`), membership
  checks, and `and`/`or`/`not`. Write `if`/`elif`/`else` branches and handle
  empty collections deliberately.
- [ ] Create, read, update, and delete dictionary entries. Iterate with
  `.keys()`, `.values()`, and `.items()`; use `.get()` when a missing key is
  expected. Build a list of dictionaries and use a set to remove duplicates.
- [ ] After practicing loops and conditions, write a simple list comprehension,
  then one with a filter. Prefer the loop when it is easier to understand.

**Engineering note:** indentation defines blocks, but an ordinary `for` loop
does not create a new local scope. A slice copies the outer list, not nested
mutable objects. A tuple prevents replacing its elements, but a list inside
it can still change. These distinctions are documented in the brain's
[iteration][iteration], [copying][copying], and [tuple][tuples] notes.

**Deliverable:** `exercises/module_02.py` stores three tasks as dictionaries
with a title and completion flag. Display their titles and a summary of two
pending tasks and one completed task. Repeat with an empty list.

**Ready to advance when:** you can choose a suitable collection, explain
why the empty case works, and demonstrate both a shared-list mutation and the
limits of a shallow copy using your own example.

## Module 3: User Input, Functions, and Modules

**Read:** [PCC, Chapters 7-8][pcc] - "User Input and while Loops" and "Functions".
Pay particular attention to "Passing Arguments", "Default Values", and
"Return Values" before studying arbitrary arguments.

- [ ] Read input with `input()`, which returns text. Convert numeric input with
  `int()` or `float()` and use `%` where appropriate.
- [ ] Write a `while` loop with a clear exit condition. Use flags, sentinels,
  `break`, and `continue`; avoid changing a collection while iterating over it.
- [ ] Define and call functions with parameters and concise docstrings.
  Practice ordinary positional arguments, keyword arguments, and default values.
- [ ] Use `return` to pass results to the caller instead of only printing them.
  Explain that a function without an explicit returned value returns `None`.
- [ ] Distinguish local names, rebinding a parameter, and mutating a passed
  object. Decide whether a function should modify its inputs.
- [ ] Once ordinary calls are comfortable, practice `*args` and `**kwargs`
  in small examples; do not force them into every function.
- [ ] Split reusable functions into modules and use explicit imports or aliases.
  Avoid wildcard imports because they obscure names, not because they are
  formally deprecated.

**Engineering note:** separate `input()` and `print()` from reusable task
operations. Guard the CLI entry point with `if __name__ == "__main__":` so
importing a module does not start an input loop. See the
[functions][functions] and [module organization][modules] notes for these
clarifications.

**Deliverable:** start `capstone/cli.py` and `capstone/tasks.py`. Build an
in-memory menu to add a task, list tasks, complete a task by ID, and quit.
Give each task a unique integer ID. Use functions for task operations and
provide explicit feedback for unknown menu choices.

**Ready to advance when:** the menu can perform each operation repeatedly and
exit normally, and a task function can be called without prompting for input.
Start with valid numeric input; Module 4 adds recovery from conversion errors.

## Module 4: Classes, Files, and Error Handling

**Read:** [PCC, Chapters 9-10][pcc] - "Classes" and "Files and Exceptions".

- [ ] Distinguish a class from an instance. Use `__init__()` to initialize
  instance attributes, `self` to refer to the instance, and methods for behavior.
- [ ] Practice changing state through methods that check a rule, such as
  rejecting an empty task title.
- [ ] Demonstrate inheritance, `super()`, and method overriding in a small
  exercise. Compare this with composition: storing one object inside another.
- [ ] Read and write text with `pathlib.Path`, use `encoding="utf-8"`, and process
  lines with `splitlines()`. Understand that `write_text()` replaces existing
  file contents.
- [ ] Use small `try` blocks and specific `except` handlers. Handle anticipated
  input or file errors with an explanation, rather than silently using `pass`.
  Use `else` for work that should run only after the protected operation succeeds.
- [ ] Save and restore simple records with `json.dumps()` and `json.loads()`.
  Separate file access from task operations.

**Deliverable:** `exercises/module_04.py` demonstrates a small class, independent
instances, and inheritance versus composition. Add `capstone/storage.py` to
save and reload tasks as JSON. Use classes in the capstone only where they
clarify the design; a layered class hierarchy is not a requirement.

**Ready to advance when:** task state survives restarting the CLI; invalid
numeric input produces a useful message; missing storage starts an empty
session with a notice; and malformed JSON or an unexpected record structure
is reported without silently resetting or overwriting the file.

## Module 5: Automated Tests and Safe Refactoring

**Read:** [PCC, Chapter 11][pcc] - "Testing Your Code", especially "A Passing
Test", "Responding to a Failed Test", and "Using Fixtures".

- [ ] Install `pytest`, discover tests in `test_*.py` files, and name test
  functions `test_*`.
- [ ] Write a test that calls a function and checks its result with plain
  `assert`. Read both passing and failing reports.
- [ ] Check normal behavior, empty input, and invalid input. Test observable
  results, not an implementation detail that may change during refactoring.
- [ ] Test class behavior and ensure one test's mutations do not affect another.
- [ ] Introduce `@pytest.fixture` when setup becomes repetitive. Start with
  function-scoped fixtures that create fresh objects, not shared mutable state.
- [ ] Preserve valid expectations when fixing a regression. Change a test only
  when its expectation is wrong or the intended behavior deliberately changes.
  Refactor working code and rerun the suite.

**Practical extension - isolated test environment:** the commands below are
setup guidance for this repository, not a claim that Part I teaches `venv`.
From the repository root, using a Linux/macOS shell:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

On Windows PowerShell, create it with `py -m venv .venv` and activate it with
`.\.venv\Scripts\Activate.ps1`. Reactivate the environment in new terminal
sessions. Keep the environment out of version control.

**Deliverable:** add tests for task operations and JSON storage. Let storage
functions accept a path, and use temporary files rather than real user data
in tests. A temporary-path fixture is a practical extension to the chapter's
introductory fixture examples.

**Ready to advance when:** the capstone cases below have automated checks for
their task/storage behavior, an intentional bug makes a relevant test fail,
and correcting it restores the suite. Manually check the interactive menu.
Passing tests support confidence in the cases tested; they do not prove the
absence of all bugs. TDD is an optional later extension, not this module's
prerequisite.

## Capstone: A Task Tracker You Can Explain

Build the project incrementally in Modules 3-5, using Module 2's records as a
starting point. Each task has an ID, a nonempty title, and a completion flag.
Keep terminal interaction, task operations, and storage separate.

The following are **original acceptance criteria**, not book exercises:

| Scenario | Required behavior |
|---|---|
| Empty state | Display a clear empty-list message and allow adding a task. |
| Add and list | Assign distinct IDs, preserve titles, and display completion status. |
| Complete a task | Change only the selected task; completing it again is harmless. |
| Invalid input | Reject blank titles, invalid numeric IDs, and unknown IDs with an explanation; leave existing tasks unchanged. |
| Save and restart | Restore IDs, titles, and completion flags; new IDs do not collide with restored tasks. |
| Missing file | Explain that no saved data was found and start an empty session. |
| Invalid stored data | Report malformed JSON or invalid records; stop loading without silently overwriting the original file. |
| File access failure | Report a read/write failure; never announce a successful save when writing failed. |
| Quit and import | Exit the menu normally; importing task or storage modules does not prompt for input. |

Start with this **proposed layout**, adding files only as you reach the relevant
module. No packaging tools or `src/` layout are needed for these first scripts:

```text
python-programming-foundations/
├── README.md
├── exercises/
│   ├── module_01.py
│   ├── module_02.py
│   └── module_04.py
└── capstone/
    ├── cli.py
    ├── tasks.py
    ├── storage.py
    └── tests/
        ├── test_tasks.py
        └── test_storage.py
```

Once those files exist and the environment is active, run from the repository
root:

```bash
cd capstone
python cli.py
python -m pytest
```

Document the actual save-file location and how to run your completed program.
Use disposable data while experimenting with file writes.

## Completion and the Broader Phase 1

**Book-based core complete:**

- [ ] Complete all five module deliverables and explain the code in your own words.
- [ ] Meet the capstone acceptance criteria and demonstrate the error cases.
- [ ] Make a small behavior change, add or adjust its test deliberately, and
  explain the result without rewriting the whole application.

**Engineering bridge:** the global Phase 1 roadmap also mentions environment
isolation, dependency management, and argument parsing. These are separate
practical objectives; their coverage is not established by the audited Part I
passages. Do not confuse completing the book-based core with completing this
broader tooling scope.

- [ ] Explain the virtual environment used for tests and install dependencies
  into it with `python -m pip`, rather than into the system environment.
- [ ] Extend the CLI with `argparse`: provide `--help` and add/list/complete
  commands, reuse the same task functions, and report invalid arguments.
  An `input()` menu alone does not meet this argument-parsing objective.

**Optional later work:** `uv`, `pyproject.toml`, packaging, a conventional
`src/<package_name>/` layout, and TDD. CPython bytecode, reference counting,
hash-table internals, and asymptotic analysis should not block these beginner
milestones. Keep algorithm analysis for Phase 2 and deeper runtime details for
later study with suitable evidence.

The global progression remains: **Python foundations (current)** -> data
structures and algorithms -> systems and networking -> practical software
engineering and APIs -> distributed data systems -> specialization.

## Sources

**Primary source:** Eric Matthes, *Python Crash Course*, 3rd Edition, No Starch
Press, 2023. Core scope: Part I, Chapters 1-11 (`c01.xhtml`-`c11.xhtml` in the
local EPUB). The per-module references identify the relevant chapters and
sections; this roadmap is not a replacement for reading and practicing them.

**Local brain references:** [source summary][pcc],
[global roadmap][global-roadmap], and [audit and correction record][audit].
The audit records where generated summaries overreached the book. Treat
engineering clarifications and project choices as synthesis, not verbatim
source content.

These links assume the local `themainframe` directory next to `Coding/`.
They are local references, not public GitHub resources.

[pcc]: ../../themainframe/wiki/sources/matthes-python-crash-course-2023.md
[iteration]: ../../themainframe/wiki/concepts/python-sequence-iteration-and-comprehensions.md
[copying]: ../../themainframe/wiki/concepts/python-slicing-and-memory-aliasing.md
[tuples]: ../../themainframe/wiki/concepts/python-tuples-and-immutable-sequences.md
[functions]: ../../themainframe/wiki/concepts/python-functions-and-parameter-passing.md
[modules]: ../../themainframe/wiki/concepts/python-modules-and-code-organization.md
[global-roadmap]: ../../themainframe/wiki/questions/software-engineering-roadmap.md
[audit]: ../../themainframe/wiki/questions/python-phase-1-roadmap-audit.md
