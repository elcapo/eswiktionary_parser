from dataclasses import dataclass
import re
from bigxml import Parser, xml_handle_element, xml_handle_text
from mwparserfromhell import parse
from eswiktionary_parser import defaults
from eswiktionary_parser.downloader import download
from eswiktionary_parser.wiki_parser import parse_and_get_definitions

@xml_handle_element("mediawiki", "page")
class Page:
    title: str = ""

    def __repr__(self):
        return self.title

    @xml_handle_element("title")
    def handle_title(self, node):
        self.title = node.text

    @xml_handle_element("revision", "text")
    def handle_text(self, node):
        if not self.is_definition:
            return
        
        self.definitions = parse_and_get_definitions(node.text)

    @xml_handle_element("ns")
    def handle_ns(self, node):
        self.is_definition = node.text == "0"

def pages_iterator(dump_filename: str = None):
    compressed_filename, dump_filename = defaults.target_filename_or_default(dump_filename)
    with open(dump_filename, "rb") as file:
        for page in Parser(file).iter_from(Page):
            if not page.is_definition:
                continue
            if len(page.definitions):
                yield page

if __name__ == "__main__":
    download()
    for page in pages_iterator():
        for definition in page.definitions:
            print("{};{};{}".format(
                page.title,
                definition.classification,
                definition.definition))
