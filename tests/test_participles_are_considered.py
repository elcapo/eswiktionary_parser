from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_contractions_are_considered():
    # @link https://es.wiktionary.org/wiki/amado
    code = """=== {{forma verbal|es}} ===
;1: {{participio|amar}}
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Participio de amar."