from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_nouns_acting_as_verbs_are_processed():
    # @link https://es.wiktionary.org/wiki/mudanza
    code = """=== {{sustantivo femenino|es}} ===
;1: {{sustantivo de verbo|mudar|glosa=cambiar}}, en especial en las [[idea]]s o [[sentimiento]]s
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Acción o efecto de cambiar, en especial en las ideas o sentimientos."
