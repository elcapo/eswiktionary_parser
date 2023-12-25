from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_ignores_examples_with_bullet_points():
    # @link https://es.wiktionary.org/wiki/pr%C3%B3tesis
    code = """=== {{sustantivo femenino|es}} ===
{{inflect.es.sust.invariante}}

;1 {{medicina}}: Procedimiento médico mediante el que se repara artificialmente o se sustituye un miembro, un órgano o parte de un órgano, perdidos o dañados.
:*'''Ejemplo:'''
::&quot;En el Hospital Belleveu de N. Y, el médico responsable de haber indicado la ''prótesis'' a un amputado de la extremidad inferior y su correspondiente rehabilitación, fue &quot;felicitado&quot; por el director del hospital porque el citado paciente a mano armada y desplazándose a gran velocidad, había asaltado un banco con todo éxito a dos cuadras de la institución&quot;. José B. Cibeira, ''Bioética y rehabilitación'', Argentina, 1997. [[CREA]]

;2: Dispositivo que sirve para sustituir el miembro, órgano o parte del órgano que ha experimentado algún tipo de daño o pérdida.
:*'''Ejemplos:'''
::&quot;La implantación de ''prótesis'', tanto de cadera como de rodilla, mejora la movilidad de la articulación y disminuye la intensidad del dolor.&quot; Luis Gutiérrez Serantes, ''365 días para vivir con salud'', España, 2002. [[CREA]]
::&quot;&amp;mdash; ¿Cómo van tus dientes?
::&amp;mdash; Aquí los tengo &amp;mdash; respondió el viejo, llevándose una mano al bolsillo. Desenvolvió un pañuelo descolorido y le enseñó la ''prótesis''.
::&amp;mdash; ¿Y por qué no los usas, viejo necio?
::&amp;mdash; Ahorita me los pongo. No estaba ni comiendo ni hablando. ¿Para qué gastarlos entonces?&quot; Luis Sepúlveda, ''Un viejo que leía novelas de amor'', Chile, 1989.[[CREA]]

;3 {{lingüística}}: Adición de un [[fonema]] o grupo de estos al principio de una palabra
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 3
    assert definitions[0].definition == "Procedimiento médico mediante el que se repara artificialmente o se sustituye un miembro, un órgano o parte de un órgano, perdidos o dañados."
    assert definitions[1].definition == "Dispositivo que sirve para sustituir el miembro, órgano o parte del órgano que ha experimentado algún tipo de daño o pérdida."
    assert definitions[2].definition == "Adición de un fonema o grupo de estos al principio de una palabra."

def test_ignores_examples_in_quotes():
    # @link https://es.wiktionary.org/wiki/chasqui
    code = """=== {{sustantivo masculino|es}} ===
{{inflect.es.sust.reg}}

;1 {{Historia}}: {{plm|mensajero}} de [[a pie]] que transportaba [[correo]]s y [[mercancía]]s en el sistema de [[posta]]s del [[imperio]] [[inca]]
{{hiperónimo|correo}}
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

if __name__ == "__main__":
    test_ignores_examples_with_bullet_points()
    test_ignores_examples_in_quotes()
