from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_verb_forms_are_considered():
    # @link https://es.wiktionary.org/wiki/aman
    code = """=== Forma verbal ===
;1: {{f.v|amar|p=3p|t=pres|m=ind}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Tercera persona del plural (ellas, ellos), o segunda persona del plural (ustedes) del presente de indicativo de amar."
