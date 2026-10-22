"""Run with: python -m unittest -v"""

import contextlib
import io
import unittest
from unittest.mock import patch

from main import count_letters, main


class CounterTests(unittest.TestCase):
    def assert_counts(self, text, vowels, consonants, ignored):
        result = count_letters(text)
        self.assertEqual(result["vowels"], vowels)
        self.assertEqual(result["consonants"], consonants)
        self.assertEqual(result["ignored"], ignored)
        self.assertEqual(vowels + consonants + ignored, len(text))

    def test_mixed_sentence(self):
        self.assert_counts("Hello World! 123", 3, 7, 6)

    def test_uppercase_and_lowercase_vowels(self):
        self.assert_counts("AEIOUaeiou", 10, 0, 0)

    def test_consonants_including_y(self):
        self.assert_counts("Rhythm", 0, 6, 0)

    def test_digits_and_symbols(self):
        self.assert_counts("123 !?", 0, 0, 6)

    def test_empty_string(self):
        self.assert_counts("", 0, 0, 0)

    def test_whitespace(self):
        self.assert_counts(" \t\n", 0, 0, 3)

    def test_non_english_characters(self):
        self.assert_counts("caf\u00e9 \u03a9 \U0001f642\u212a", 1, 2, 6)

    def test_repetition_and_unique_sets(self):
        result = count_letters("AaBbAa")
        self.assertEqual(result["vowels"], 4)
        self.assertEqual(result["consonants"], 2)
        self.assertEqual(result["unique_vowels"], {"a"})
        self.assertEqual(result["unique_consonants"], {"b"})

    def test_alphabet(self):
        self.assert_counts("abcdefghijklmnopqrstuvwxyz", 5, 21, 0)

    def test_menu_validation_analysis_and_exit(self):
        stream = io.StringIO()
        with patch("builtins.input", side_effect=["9", "1", "  ",
                                                 "1", "Hello", "2"]):
            with contextlib.redirect_stdout(stream):
                main()
        output = stream.getvalue()
        self.assertIn("Invalid choice!", output)
        self.assertIn("Please enter at least one", output)
        self.assertIn("Vowels            : 2", output)
        self.assertIn("Consonants        : 3", output)
        self.assertIn("Thank you for using the counter!", output)

    def test_end_of_input(self):
        with patch("builtins.input", side_effect=EOFError):
            with contextlib.redirect_stdout(io.StringIO()) as stream:
                main()
        self.assertIn("Counter closed.", stream.getvalue())

    def test_keyboard_interrupt(self):
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            with contextlib.redirect_stdout(io.StringIO()) as stream:
                main()
        self.assertIn("Counter closed.", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
