# Vowel & Consonant Counter

Python Programming mini project - Topic 5, Sets & Strings, Project 3.

| Student | Roll number |
| --- | --- |
| Parag Yewale | 12 |
| Om Supe | 11 |

Class / Semester: SY-C / III  
Submitted to: Ashish Mishra  
Academic year: 2026-2027

## Run

Install Python 3. No third-party packages are required. Open a terminal in
this folder and run:

```console
python main.py
```

On Windows, `py -3 main.py` also works when the Python launcher is installed.
Choose **1** to enter a word or sentence, or **2** to exit.

## Features

- Counts every occurrence of English vowels (a, e, i, o, u) and consonants.
- Handles uppercase and lowercase letters equally; y is a consonant.
- Shows total letters, ignored characters, and sorted unique letters.
- Uses sets, strings, loops, functions, dictionaries and conditionals.
- Rejects empty or whitespace-only input and invalid menu choices.
- Handles end-of-input and Ctrl+C without a traceback.

Only English letters A-Z and a-z are classified. Digits, punctuation,
whitespace, accented letters, other scripts and emoji are ignored.
Ignored characters are counted using Python string length, not visual width.

## Example

For `Hello World! 123`:

```text
Vowels            : 3
Consonants        : 7
Total letters     : 10
Ignored characters: 6
Unique vowels     : e, o
Unique consonants : d, h, l, r, w
```

## Tests

```console
python -m unittest -v
```

The 12 tests cover mixed text, case, repeated letters, unique sets,
digits and symbols, empty input, whitespace, non-English characters,
the alphabet, menu validation, exit, EOF and keyboard interruption.

## Files

- `main.py` - complete application.
- `test_main.py` - automated tests.
- `sample_output.txt` - recorded output from actual program runs.
- `output_mixed.png` and `output_validation.png` - execution captures.
- `Project_Report.pdf` - project report in the supplied reference format.

## Repository

https://github.com/omsupe28/vowel-consonant-counter
