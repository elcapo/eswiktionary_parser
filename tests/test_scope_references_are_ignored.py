from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_scope_references_are_ignored():
    # @link https://es.wiktionary.org/wiki/boy
    code = """=== {{sustantivo masculino|es}} ===
;1: Chico del cuerpo de baile en las revistas y espectáculos musicales.
:*'''Ejemplo''': ''se despedía siempre del grupo como si fuera Celia Gámez en la apoteosis final, del brazo del primer boy (Pedro) y nos quedábamos con un palmo de narices.'' (Fuente: José María Guelbenzu: ''El río de la luna''. España, 1981. [[Wikcionario:Fuentes#CREA|CREA]].)
{{ámbito|España}}
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Chico del cuerpo de baile en las revistas y espectáculos musicales."
