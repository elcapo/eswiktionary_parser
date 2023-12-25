from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_related_articles_are_ignored():
    # @link https://es.wiktionary.org/wiki/Francia
    code = """=== {{sustantivo propio|es|género=femenino}} ===
;1 {{países}}: {{plm|país}} de {{l|es|Europa}} {{l|es|occidental}}, que forma parte de la {{l|es|Unión Europea}}.
{{relacionado|tit=Gentilicio|francés}}.
{{relacionado|tit=Capital|París}}.
{{relacionado|tit=Idioma oficial|francés}}.
{{relacionado|tit=Moneda|euro}} (antes era el {{l|es|franco}}).
;2: {{antropónimo femenino}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 2
    assert definitions[0].definition == "País de Europa occidental, que forma parte de la Unión Europea."
    assert definitions[1].definition == "Nombre de pila de mujer."
