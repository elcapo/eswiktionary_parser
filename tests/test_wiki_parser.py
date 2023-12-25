from eswiktionary_parser.fixture_reader import read_and_parse_fixture

def test_can_extract_definitions():
    definitions = read_and_parse_fixture("tests/fixtures/palabra.wiki")
    assert len(definitions) == 7
    assert definitions[0].definition == "Unidad mínima de significado de una lengua o idioma."

def test_ignores_examples():
    # Remove examples within bullet points
    definitions = read_and_parse_fixture("tests/fixtures/prótesis.wiki")
    assert len(definitions) == 3
    assert definitions[1].definition == "Dispositivo que sirve para sustituir el miembro, órgano o parte del órgano que ha experimentado algún tipo de daño o pérdida."
    # Remove examples in quotes
    definitions = read_and_parse_fixture("tests/fixtures/chasqui.wiki")
    assert len(definitions) == 3

def test_removes_unwanted_prefixes():
    # Remove the prefix "Fig."
    definitions = read_and_parse_fixture("tests/fixtures/elemental.wiki")
    assert definitions[1].definition == "Primordial, fundamental."

def test_ignores_synonyms():
    definitions = read_and_parse_fixture("tests/fixtures/uno.wiki")
    assert definitions[6].definition == "Que no posee igual."
    assert definitions[7].definition == "Que se identifica con otra persona o cosa en un plano espiritual, moral o que se siente físicamente unido."
