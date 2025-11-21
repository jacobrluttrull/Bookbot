# Bookbot

## Overview

Bookbot is a command-line application written in Python that analyzes the contents of a book (plain text) and generates a statistical report of word and character usage. This project is part of the Boot.dev "Build a Bookbot in Python" course.

## Features

* Load a text file containing a book
* Count total words in the document
* Count occurrences of each character (case-insensitive)
* Sort characters by frequency
* Output a formatted report to the terminal

## Getting Started

### Prerequisites

* Python 3.x
* Git
* Terminal/command-line access

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   cd REPO_NAME
   ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   # Windows: .venv\\Scripts\\activate
   ```
3. (Optional) Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Program

Run Bookbot with a path to a text file:

```bash
python main.py books/frankenstein.txt
```

Replace the file path with any `.txt` file you want to analyze.

## Example Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

e: 46043
t: 30365
a: 26743
...
--- End report ---
```

## Project Structure

```
books/                  # Text files for analysis
main.py                 # Entry point
analysis.py             # Logic for counting words/characters
report.py               # Formatting and printing results
tests/                  # Optional unit tests
requirements.txt        # Optional dependencies
.gitignore              # Ignore venv, book files, etc.
README.md               # Project documentation
```

## Contributing

1. Fork this repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add my feature"`
4. Push: `git push origin feature/my-feature`
5. Open a pull request

## License

This project is released under the MIT License.
