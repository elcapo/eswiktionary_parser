from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_images_are_ignored():
    # @link https://es.wiktionary.org/wiki/calzado
    code = """===={{sustantivo masculino|es}}====
[[Image:Ballerinas (Weiss).jpg|thumb|zapatillas de bailar [1]]]
;1 {{Vestimenta}}: [[prenda|Prenda]] de [[vestir]] que se usa para cubrir y proteger el [[pie]]
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Prenda de vestir que se usa para cubrir y proteger el pie."
