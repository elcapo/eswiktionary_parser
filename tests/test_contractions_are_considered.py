from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_contractions_are_considered():
    # @link https://es.wiktionary.org/wiki/al
    code = """=== Contracción ===
;1: {{contracción|leng=es|a|el|preposición|artículo}} (masculino singular).
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Contracción de la preposición a y el artículo el (masculino singular)."
