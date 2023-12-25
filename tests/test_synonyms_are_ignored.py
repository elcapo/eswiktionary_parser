from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_synonyms_are_ignored():
    # @link https://es.wiktionary.org/wiki/uno
    code = """==={{adjetivo|es}}===
;1: Que no se encuentra [[dividido]] o [[separado]].
{{uso|Con este significado, no tiene plural}}.
{{sinónimo|cabal|entero|indiviso|íntegro}}.
;2: Que no posee [[igual]].
{{sinónimo|único}}, sin [[par]]
;3: Que se identifica con otra persona o cosa en un plano espiritual, moral o que se siente físicamente unido.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 3
    assert definitions[0].definition == "Que no se encuentra dividido o separado."
    assert definitions[1].definition == "Que no posee igual."
    assert definitions[2].definition == "Que se identifica con otra persona o cosa en un plano espiritual, moral o que se siente físicamente unido."
