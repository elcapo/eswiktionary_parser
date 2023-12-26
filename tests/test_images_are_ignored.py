from eswiktionary_parser.wiki_parser import parse_and_get_definitions

def test_images_are_ignored():
    # @link https://es.wiktionary.org/wiki/calzado
    code = """===={{sustantivo masculino|es}}====
[[Image:Ballerinas (Weiss).jpg|thumb|zapatillas de bailar [1]]]
;1 {{Vestimenta}}: [[prenda|Prenda]] de [[vestir]] que se usa para cubrir y proteger el [[pie]]
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 1
    assert definitions[0].definition == "Prenda de vestir que se usa para cubrir y proteger el pie."

def test_trailing_text_in_example_lines_is_ignored():
    # @link https://es.wiktionary.org/wiki/amante
    code = """==== {{adjetivo|es}} ====
;1: Se dice de quien ama, expresa [[amor]] o tiene fuerte [[afición]] por algo o alguien.&lt;ref name=&quot;dle&quot; /&gt;
{{ejemplo}} Es ''amante'' de las telenovelas.
;2: {{plm|estimado}}, [[querido]] (como vocativo afectuoso, especialmente en cartas).&lt;ref name=&quot;dle&quot; /&gt;
{{uso|desusado}}.
{{sinónimo|amado|amada}}.
{{ejemplo}} Mi ''amantísima'' lectora.
"""
    definitions = parse_and_get_definitions(code)
    assert len(definitions) == 2
    assert definitions[0].definition == "Se dice de quien ama, expresa amor o tiene fuerte afición por algo o alguien."
    assert definitions[1].definition == "Estimado, querido (como vocativo afectuoso, especialmente en cartas)."
