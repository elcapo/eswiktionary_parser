from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_figurative_prefix_is_removed():
    # @link https://es.wiktionary.org/wiki/elemental
    code = """=== {{adjetivo|es}} ===
;1: Fig. [[Primordial]], [[fundamental]].
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Primordial, fundamental."

def test_by_analogy_prefix_is_removed():
    # @link https://es.wiktionary.org/wiki/beber
    code = """=== {{verbo intransitivo|es}} ===
;1: Por analogía, [[adoptar]] [[idea]]s o [[información]] de una fuente
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Adoptar ideas o información de una fuente."

def test_in_special_prefix_is_removed():
    # @link https://es.wiktionary.org/wiki/beber
    code = """=== {{verbo intransitivo|es}} ===
;1: En especial, beber{{-sub|1}} [[bebida alcohólica|bebidas alcohólicas]]
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Beber bebidas alcohólicas."
