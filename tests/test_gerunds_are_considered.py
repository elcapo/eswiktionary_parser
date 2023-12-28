from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_gerunds_are_considered():
    # @link https://es.wiktionary.org/wiki/amando
    code = """=== Forma verbal ===
;1: {{gerundio|amar}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Gerundio de amar."
