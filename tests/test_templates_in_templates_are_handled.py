from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_templates_in_templates_are_handled():
    # @link https://es.wiktionary.org/wiki/el
    code = """
=== {{artículo determinado|es}} ===
;1: {{impropia|{{plm|artículo determinado}} masculino singular}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Artículo determinado masculino singular."
