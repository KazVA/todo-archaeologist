# TODO Archaeologist

A Python command-line tool that searches Git repositories for forgotten TODOs, FIXMEs, HACKs, and XXX notes, then ranks them by age.

## Features

- Scans tracked files in a Git repository.
- Detects TODO, FIXME, HACK, and XXX markers.
- Uses Git blame to identify the author and date associated with each matching line.
- Calculates how long each note has been around.
- Displays the file path, line number, author, and commit hash.
- Sorts findings from oldest to newest.
- Shows up to 15 findings in the terminal.

## Requirements

- Python 3
- Git installed and available on your PATH

## Usage

Run the script with the path to a local Git repository:

```bash
python todo_archaeologist.py PATH_TO_GIT_REPOSITORY
```

Example:

```bash
python todo_archaeologist.py F:\Projects\expense-tracker
```

## Preview

![TODO Archaeologist terminal output](screenshot.png)

## How It Works

1. Retrieves tracked files using `git ls-files`.
2. Inspects line history using `git blame`.
3. Searches for unfinished-work markers.
4. Calculates the age of each matching line.
5. Sorts and displays the oldest findings first.

## Limitations

- Only Git-tracked files are scanned.
- Results depend on the repository's available Git history.
- Lines that cannot be processed by Git blame are skipped.
- The tool does not modify repository files.
- A maximum of 15 findings is displayed.

## Built With

- Python 3
- Git
- Python standard library: `argparse`, `subprocess`, and `datetime`

## License

MIT