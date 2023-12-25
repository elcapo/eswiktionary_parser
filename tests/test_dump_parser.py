from eswiktionary_parser.dump_parser import pages_iterator

def test_can_extract_definitions():
    for page in pages_iterator("tests/fixtures/palabra.xml"):
        assert page.title == "palabra"
        assert page.is_definition == True
        assert len(page.definitions) == 7
        assert page.definitions[0].definition == "Unidad mínima de significado de una lengua o idioma."

def test_remove_references():
    for page in pages_iterator("tests/fixtures/asocar.xml"):
        assert page.definitions[3].definition == "Moler la yerba mate en mortero."
    # Handle cases in which the ref is opened with attributes
    # Example: <ref name="novísimo">...</ref>
    for page in pages_iterator("tests/fixtures/traducción.xml"):
        assert page.definitions[2].definition == "Figura retórica de que se usa, reptiendo una palabra en diversos sentidos."

if __name__ == "__main__":
    test_remove_references()