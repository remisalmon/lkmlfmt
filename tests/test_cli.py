import os
import shutil

from unittest import TestCase
from unittest.mock import patch, mock_open

from lkmlfmt.cli import cli

FILE_UNFORMATTABLE = "tests/files/unformattable.view.lkml"
FILE_UNFORMATTED = "tests/files/unformatted.view.lkml"
FILE_FORMATTED = "tests/files/formatted.view.lkml"
FILE_TEST = "tests/files/test.view.lkml"


class TestCli(TestCase):
    def tearDown(self):
        try:
            os.remove(FILE_TEST)
        except FileNotFoundError:
            pass

        return

    @patch("sys.argv", new=["lkmlfmt", FILE_TEST])
    def test_cli_view_unformatted(self):
        shutil.copyfile(FILE_UNFORMATTED, FILE_TEST)

        cli()

        with open(FILE_TEST) as file_test, open(FILE_FORMATTED) as file_gold:
            test = file_test.read()
            gold = file_gold.read()

        self.assertEqual(test, gold)

        return

    @patch("sys.argv", new=["lkmlfmt", FILE_TEST])
    def test_cli_view_unformattable(self):
        shutil.copyfile(FILE_UNFORMATTABLE, FILE_TEST)

        with self.assertRaises(SyntaxError):
            cli()

        with open(FILE_TEST) as file_test, open(FILE_UNFORMATTABLE) as file_gold:
            test = file_test.read()
            gold = file_gold.read()

        self.assertEqual(test, gold)

        return

    @patch("sys.argv", new=["lkmlfmt"])
    def test_cli_no_arg(self):
        with self.assertRaises(SystemExit):
            cli()

        return

    @patch("sys.argv", new=["lkmlfmt", "a.view.lkml"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("lkml.load")
    def test_cli_one_arg(self, mock_load, mock_open):
        cli()

        self.assertEqual(mock_open.call_count, 1)
        self.assertEqual(mock_load.call_count, 1)

        return

    @patch("sys.argv", new=["lkmlfmt", "a.view.lkml", "another.view.lkml"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("lkml.load")
    def test_cli_two_arg(self, mock_load, mock_open):
        cli()

        self.assertEqual(mock_open.call_count, 2)
        self.assertEqual(mock_load.call_count, 2)

        return
