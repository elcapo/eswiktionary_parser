from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_femenine_plural_adjective_forms_are_considered():
    # @link https://es.wiktionary.org/wiki/ordinarias
    code = """=== Forma adjetiva ===
;1: {{forma adjetivo|leng=es|ordinario|género=femenino|número=plural}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Forma del femenino plural de ordinario."

def test_masculine_plural_adjective_forms_are_considered():
    # @link https://es.wiktionary.org/wiki/abondosos
    code = """=== Forma adjetiva ===
;1: {{forma adjetivo|leng=es|abondoso|género=|número=plural}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Forma del plural de abondoso."
