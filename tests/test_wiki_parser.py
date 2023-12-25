from eswiktionary_parser.fixture_reader import read_and_parse_fixture

def test_can_extract_definitions():
    definitions = read_and_parse_fixture("tests/fixtures/palabra.wiki")
    assert len(definitions) == 7
    assert definitions[0].definition == "Unidad mínima de significado de una lengua o idioma."

def test_removes_unwanted_prefixes():
    # Remove the prefix "Fig."
    definitions = read_and_parse_fixture("tests/fixtures/elemental.wiki")
    assert definitions[1].definition == "Primordial, fundamental."
    # Remove the prefix "Por analogía, "
    definitions = read_and_parse_fixture("tests/fixtures/beber.wiki")
    assert definitions[4].definition == "Adoptar ideas o información de una fuente."
    # Remove the prefix "En especial "
    assert definitions[1].definition == "Beber bebidas alcohólicas."

def test_ignores_synonyms():
    definitions = read_and_parse_fixture("tests/fixtures/uno.wiki")
    assert definitions[6].definition == "Que no posee igual."
    assert definitions[7].definition == "Que se identifica con otra persona o cosa en un plano espiritual, moral o que se siente físicamente unido."

def test_removes_leading_parenthesis():
    definitions = read_and_parse_fixture("tests/fixtures/té.wiki")
    assert definitions[0].definition.startswith("Arbusto de la famila de las cameliáceas, originario de Assam y de Bengala.")

def test_processes_past_simple_templates():
    definitions = read_and_parse_fixture("tests/fixtures/pasasteis.wiki")
    assert definitions[0].definition == "Segunda persona del plural (vosotras, vosotros) del pretérito perfecto simple de indicativo de pasar."

def test_removes_images():
    definitions = read_and_parse_fixture("tests/fixtures/calzado.wiki")
    assert len(definitions) == 1
    assert definitions[0].definition == "Prenda de vestir que se usa para cubrir y proteger el pie."

def test_removes_related_data():
    definitions = read_and_parse_fixture("tests/fixtures/francia.wiki")
    assert len(definitions) == 2
    assert definitions[1].definition == "Nombre de pila de mujer."

def test_process_nouns_acting_as_verbs():
    definitions = read_and_parse_fixture("tests/fixtures/mudanza.wiki")
    assert definitions[0].definition == "Acción o efecto de cambiar, en especial en las ideas o sentimientos."

def test_ignore_non_spanish_definitions():
    definitions = read_and_parse_fixture("tests/fixtures/nombre.wiki")
    assert len(definitions) == 4

def test_can_name_the_person_of_a_conjugation():
    # Second person singular (tú)
    definitions = read_and_parse_fixture("tests/fixtures/provén.wiki")
    assert definitions[0].definition == "Segunda persona del singular (tú) del imperativo de provenir."
    # Second person singular (vos)
    definitions = read_and_parse_fixture("tests/fixtures/andá.wiki")
    assert definitions[0].definition == "Segunda persona del singular (vos) del imperativo de andar."
    # Second person singular (tú, vos)
    definitions = read_and_parse_fixture("tests/fixtures/provinieras.wiki")
    assert definitions[0].definition == "Segunda persona del singular (tú, vos) del imperfecto de subjuntivo de provenir."
    # Second person singular (usted)
    definitions = read_and_parse_fixture("tests/fixtures/véase.wiki")
    assert definitions[0].definition == "Segunda persona del singular (usted) del imperativo de verse."
    # Second person plural (ustedes)
    definitions = read_and_parse_fixture("tests/fixtures/listen.wiki")
    assert definitions[0].definition == "Tercera persona del plural (ellas, ellos), o segunda persona del plural (ustedes) del presente de subjuntivo de listar."

def test_exclude_references_to_scopes():
    definitions = read_and_parse_fixture("tests/fixtures/boy.wiki")
    assert len(definitions) == 3

if __name__ == "__main__":
    test_removes_unwanted_prefixes()
