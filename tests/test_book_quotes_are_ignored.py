from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_book_quotes_are_ignored():
    # @link https://es.wiktionary.org/wiki/vedar
    code = """=== {{verbo transitivo|es}} ===
;1: {{plm|prohibir}} por {{l|es|mandamiento}} de una {{l|es|autoridad}}.&lt;ref name=&quot;drae&quot;&gt;{{DRAE2001}}&lt;/ref&gt;
:*'''Ejemplo:'''
::* &quot;Esta Ley de Extranjeros, muy semejante a la promulgada en Estados Unidos, prueba que Roosevelt va formando escuela. Verdad que en Inglaterra no se ha visto aún lo ocurrido en América del Norte: '''''vedar''''' el desembarco de dos personas por el delito de vivir maritalmente sin ser casadas; pero ya lo veremos, que la púdica Albión no puede quedarse atrás en achaques de hipocresía.&quot;. {{cita libro|
apellidos=Manuel|
nombre=González Prada|
título=En la libre Inglaterra|
año=1906|
URL=https://es.wikisource.org/wiki/En_la_libre_Inglaterra
}}
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Prohibir por mandamiento de una autoridad."