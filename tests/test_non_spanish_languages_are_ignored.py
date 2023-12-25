from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_non_spanish_languages_are_ignored():
    # @link https://es.wiktionary.org/wiki/nombre
    code = """== {{lengua|es}} ==
==={{sustantivo masculino|es}}===
;1: En general, palabra que [[designar|designa]] una [[entidad]] o [[condición]].
==Véase también==
* [[Wikcionario:Categorías gramaticales]]
{{FR-ES||1}}
==={{sustantivo masculino|fr}}===
;1: [[número|Número]] (especialmente en {{Gramática|leng=fr}} y {{Matemáticas|leng=fr}}).
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "En general, palabra que designa una entidad o condición."
