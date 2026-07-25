# Debugging Section

This section contains Python debugging exercises focused on reading tracebacks, fixing broken imports, restoring overwritten files, and verifying that programs run correctly. A strong README should explain what the project does, how to install dependencies, and how to run it with copy-paste-ready commands.[1][2][3]

## Purpose

The goal of this section is to practice finding and fixing common coding problems in small Python programs. Debugging in Python centers on identifying bugs, reading error messages, and correcting the underlying cause rather than just silencing the symptom.[4]

## Prerequisites

- Python 3 installed on your system.
- A virtual environment for isolated package management.
- The project files for the `debugging` folder, including any `.py` scripts and data files such as `airfares.txt`.

README guidance recommends stating required runtime versions and keeping setup instructions short and scannable.[1][2]

## Setup

Create and activate a virtual environment, then install any needed packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
```

If a script uses Wikipedia data, install the package it imports. For `import wikipediaapi`, install `wikipedia-api`; for `import wikipedia`, install `wikipedia`.

```bash
python3 -m pip install wikipedia-api
```

## How to Run

From the `debugging` directory, run a script with:

```bash
python3 coffees.py
```

Or run the airfare optimizer with:

```bash
python3 airfares.py
```

Good READMEs use fenced code blocks for commands and keep examples easy to copy and paste.[1][3]

## Debugging Workflow

1. Read the full traceback carefully.
2. Identify the file name, line number, and error type.
3. Fix one issue at a time.
4. Run the script again after each change.
5. Confirm that the program now produces the expected output or updates the correct file.

This matches standard debugging practice: use the error message to locate the failure, then test again after each fix.[4]

## Common Issues

- `ModuleNotFoundError`: the needed package is not installed in the active virtual environment.
- Wrong import name: package install names and Python import names do not always match.
- File path problems: the script expects a data file in the current working directory.
- Silent success: the program runs without terminal output because it writes results to a file instead.

## Notes

- Keep edits small so mistakes are easy to reverse.
- Commit working versions often if you are using Git.
- If a file is accidentally overwritten, GitHub file history can help restore an earlier version.
