from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def read_fixture(filename: str) -> str:
    with open(filename, "r") as file:
        content = file.read()
    return content

def read_and_parse_fixture(filename: str) -> list:
    content = read_fixture(filename)
    return parse_and_get_definitions(content)
