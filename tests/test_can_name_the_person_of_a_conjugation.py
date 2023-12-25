from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_first_singular_person_tu_is_well_named():
    # @link https://es.wiktionary.org/wiki/prov%C3%A9n
    code = """=== Forma verbal ===
;1: {{forma verbo|provenir|p=tú|t=imperativo|afirmativo=s|enclítico=|pencl=}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Segunda persona del singular (tú) del imperativo de provenir."

def test_first_singular_person_vos_is_well_named():
    # @link https://es.wiktionary.org/wiki/and%C3%A1
    code = """=== Forma verbal ===
;1: {{forma verbo|andar|p=2sv|t=imperativo|afirmativo=sí}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Segunda persona del singular (vos) del imperativo de andar."

def test_first_singular_person_tu_vos_is_well_named():
    # @link https://es.wiktionary.org/wiki/provinieras
    code = """=== Forma verbal ===
;1: {{forma verbo|provenir|p=2stv|t=imperfecto|m=subjuntivo}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Segunda persona del singular (tú, vos) del imperfecto de subjuntivo de provenir."

def test_second_singular_person_usted_is_well_named():
    # @link https://es.wiktionary.org/wiki/v%C3%A9ase
    code = """=== Forma verbal ===
;1: {{forma verbo|verse|p=usted|t=imperativo|afirmativo=s|enclítico=s|pencl=se}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Segunda persona del singular (usted) del imperativo de verse."

def test_second_plural_person_vosotras_vosotros_is_well_named():
    # @link https://es.wiktionary.org/wiki/pasasteis
    code = """=== Forma verbal ===
;1: {{forma verbo|pasar|p=2p|t=pret ind|m=indicativo}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Segunda persona del plural (vosotras, vosotros) del pretérito perfecto simple de indicativo de pasar."

def test_third_plural_person_ellas_ellos_is_well_named():
    # @link https://es.wiktionary.org/wiki/listen
    code = """=== Forma verbal ===
;1: {{forma verbo|listar|p=3p|t=presente|m=subjuntivo}}.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Tercera persona del plural (ellas, ellos), o segunda persona del plural (ustedes) del presente de subjuntivo de listar."
