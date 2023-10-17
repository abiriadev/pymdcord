from unittest import TestCase, main
from pymdcord.classes import c_HEADER
from ..main import parse
from pathlib import Path
from pprint import pprint

load = lambda filename : (Path(__file__).parent / f"snippets/{filename}.md").read_text()

class ParserTest(TestCase):
    def test_parse(self):
        self.assertEqual(parse(load('header')), [c_HEADER(content="Header\n", lv=1)])

main()
