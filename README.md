# Debugging-Python-Quantic

This repository is part of Quantic's **Managing AI Engineering** section in the **AI-Assisted Software Development** course, specifically the **Debugging** module.

## Overview

This repo documents the Python debugging and troubleshooting work completed during the module before the repository was created. The exercises focused on using AI assistance to identify errors, simplify code, fix environment issues, and complete small automation tasks in Ubuntu.

## Topics Covered

- Python script debugging and cleanup
- Fixing `ModuleNotFoundError` issues
- Working with Python virtual environments (`venv`)
- Resolving Ubuntu `externally managed environment` package installation errors
- Reading files from the correct local directory
- Generating and opening HTML output files
- Basic Git workflows for resetting, restoring, committing, and pushing code
- Building simple automation scripts with Python
- Merging Excel spreadsheets with user-selected columns

## Work Completed

### 1. Website hits mapping script
A Python script was created to:
- Read `website_hits.txt`
- Parse city and website hit values
- Geocode city names
- Generate an interactive HTML map with markers
- Display the hit count when a marker is clicked

The script was later simplified to better match assignment requirements and adjusted to use files stored in the same directory as the script.

### 2. Environment and dependency troubleshooting
Several setup and execution problems were resolved, including:
- `ModuleNotFoundError` for missing packages
- Installing dependencies inside a virtual environment instead of system Python
- Fixing the `externally managed environment` error in Ubuntu
- Correcting a misspelled package name: `openpyx1` -> `openpyxl`

### 3. File path debugging
The exercises included debugging file location issues such as:
- `FileNotFoundError` when a text file was not found in the expected path
- Updating the script to read files from the same folder as the Python file
- Verifying generated HTML output paths and opening them in Ubuntu

### 4. Spreadsheet merge script
A second Python script was created to:
- Ask for the names of two Excel files
- Display the column headers from each file
- Ask the user which columns to merge on
- Save a new merged spreadsheet

This exercise also included debugging incorrect user input, such as entering column numbers instead of column names.

### 5. Git and version control practice
The workflow also included:
- Resetting local changes to match GitHub
- Understanding `HEAD is now at ...` after a hard reset
- Staging, committing, and pushing updated files to GitHub

## Tools and Technologies

- Python 3
- Ubuntu
- `venv`
- pandas
- openpyxl
- folium
- geopy
- Git and GitHub

## Key Takeaways

- Keep scripts simple when the assignment only requires core functionality.
- Use a virtual environment on Ubuntu to avoid system package conflicts.
- Always verify exact filenames and paths when debugging file access issues.
- When prompting users for merge columns, be clear whether the input should be a column name or column number.
- Commit working versions often so it is easy to recover from mistakes.

## Repository Purpose

This repository serves as a record of the debugging exercises, fixes, and Python scripts developed during the module. It highlights practical debugging patterns and AI-assisted problem solving in a local Ubuntu development environment.
