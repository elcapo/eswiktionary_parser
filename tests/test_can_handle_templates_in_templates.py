from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_can_handle_templates_in_templates():
    # @link https://es.wiktionary.org/wiki/el
    code = """
=== {{artículo determinado|es}} ===
;1: {{impropia|{{plm|artículo determinado}} masculino singular}}.
"""
    definitions = parse_and_get_definitions(code)
    assert definitions[0].definition == "Artículo determinado masculino singular."

if __name__ == "__main__":
    test_can_handle_templates_in_templates()
