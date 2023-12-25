from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_leading_parenthesis_are_ignored():
    # @link https://es.wiktionary.org/wiki/t%C3%A9
    code = """==={{sustantivo masculino|es}}===
;1 {{planta}}: (''[[species:Camellia sinensis|Camellia sinensis]]'') {{ucf|arbusto}} de la famila de las [[cameliácea]]s, originario de Assam y de Bengala.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Arbusto de la famila de las cameliáceas, originario de Assam y de Bengala."
