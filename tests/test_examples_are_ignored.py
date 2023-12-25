from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_examples_in_bullet_points_are_ignored():
    # @link https://es.wiktionary.org/wiki/pr%C3%B3tesis
    code = """=== {{sustantivo femenino|es}} ===
;1 {{medicina}}: Procedimiento médico mediante el que se repara artificialmente o se sustituye un miembro, un órgano o parte de un órgano, perdidos o dañados.
:*'''Ejemplo:'''
::&quot;En el Hospital Belleveu de N. Y, el médico responsable de haber indicado la ''prótesis'' a un amputado de la extremidad inferior y su correspondiente rehabilitación, fue &quot;felicitado&quot; por el director del hospital porque el citado paciente a mano armada y desplazándose a gran velocidad, había asaltado un banco con todo éxito a dos cuadras de la institución&quot;. José B. Cibeira, ''Bioética y rehabilitación'', Argentina, 1997. [[CREA]]
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Procedimiento médico mediante el que se repara artificialmente o se sustituye un miembro, un órgano o parte de un órgano, perdidos o dañados."

def test_multiline_examples_are_ignored():
    # @link https://es.wiktionary.org/wiki/chasqui
    code = """=== {{sustantivo masculino|es}} ===
;1 {{Historia}}: {{plm|mensajero}} de [[a pie]] que transportaba [[correo]]s y [[mercancía]]s en el sistema de [[posta]]s del [[imperio]] [[inca]]
{{ejemplo
| y que por los caminos dejase puestos postas de media a media legua, a quellos llaman ''chasquis'', por los cuales le avisase por días de lo que sucedía |apellidos=Sarmiento de Gamboa
|nombre=Pedro
|otros=
|título=Historia de los incas
|año= 1572/1943
|editorial= Emecé
|ubicación= Buenos Aires
|páginas= p.107}}
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Mensajero de a pie que transportaba correos y mercancías en el sistema de postas del imperio inca."
