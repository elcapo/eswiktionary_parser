from eswiktionary_parser.fixture_reader import read_fixture
from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_can_extract_definitions():
    wikitext = read_fixture("tests/fixtures/palabra.wiki")
    definitions = parse_and_get_definitions(wikitext)
    assert len(definitions) == 7
    assert definitions[0].definition == "Unidad mínima de significado de una lengua o idioma."

def test_ignores_examples():
    wikitext = read_fixture("tests/fixtures/prótesis.wiki")
    definitions = parse_and_get_definitions(wikitext)
    assert len(definitions) == 3
    assert definitions[1].definition == "Dispositivo que sirve para sustituir el miembro, órgano o parte del órgano que ha experimentado algún tipo de daño o pérdida."
