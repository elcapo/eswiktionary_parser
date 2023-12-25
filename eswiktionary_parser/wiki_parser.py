import re
from lxml import html
from mwparserfromhell import parse
from mwparserfromhell.wikicode import Wikicode
from mwparserfromhell.nodes.template import Template
from eswiktionary_parser.definition import Definition

def parse_and_get_definitions(string: str) -> list:
    code = parse(string)
    return get_definitions(code)

def get_definitions(code: Wikicode) -> list:
    definitions = []

    for section in code.get_sections(
        flat = True,
        include_headings = True,
    ):
        if section_is_ignorable(section):
            continue

        if is_not_spanish(section):
            return definitions

        classification = classify_section(section)

        if not classification:
            continue
        
        section = process(section)
        stringified = stringify_and_clean(section)
        found = extract_definitions(stringified)

        if len(found) == 0:
            continue

        for definition in found:
            definitions.append(Definition(definition, classification))

    return definitions

def section_is_ignorable(section: str) -> bool:
    if "= Véase también =" in section:
        return True
    if "= Etimología =" in section or "{{etimología" in section:
        return True
    if "= Información adicional =" in section:
        return True
    if "= Locuciones =" in section:
        return True
    if "= Traducciones =" in section or "{{trad-" in section:
        return True
    if "Referencias y notas" in section:
        return True
    if not contains_letters(section):
        return True
    return False

def is_not_spanish(section: str) -> bool:
    if "{{lengua|" in section and not "{{lengua|es}}" in section:
        return True
    return False

def classify_section(section: str) -> str:
    if "{{verbo transitivo" in section:
        return "verbo transitivo"
    if "{{forma verbo" in section:
        return "conjugación"
    if "{{verbo intransitivo" in section:
        return "verbo intransitivo"
    if "{{preposición" in section:
        return "preposición"
    if "{{artículo determinado" in section:
        return "artículo determinado"
    if "{{pronombre personal" in section:
        return "pronombre personal"
    if "{{adjetivo" in section:
        return "adjectivo"
    if "{{sustantivo propio" in section:
        return "nombre propio"
    if "{{sustantivo femenino" in section:
        return "sustantivo femenino"
    if "{{sustantivo masculino" in section:
        return "sustantivo masculino"
    if "{{sustantivo" in section:
        return "sustantivo"
    if "{{antropónimo femenino" in section:
        return "nombre propio femenino"
    if "{{antropónimo masculino" in section:
        return "nombre propio masculino"
    if "{{interjección" in section:
        return "interjección"
    if "{{pronombre interrogativo" in section:
        return "pronombre interrogativo"
    if "{{adjetivo interrogativo" in section:
        return "adjetivo interrogativo"
    if "{{interjección|es|interrogativo" in section:
        return "interjección interrogativa"
    if "{{adverbio|es|exclamativo" in section:
        return "adverbio exclamativo"

def safe_remove(code: Wikicode, template: Template):
    try:
        code.remove(template)
    except:
        pass

def safe_replace(code: Wikicode, template: Template, value):
    try:
        code.replace(template, value)
    except:
        pass

def safe_strip_html(text: str) -> str:
    stripped = ""
    try:
        stripped = html.fromstring(text).text_content()
    except:
        pass
    return str(stripped)

def process(code: Wikicode) -> Wikicode:
    code = parse_templates(code)
    code = remove_headings(code)
    return process_links(code)

def parse_templates(code: Wikicode) -> Wikicode:
    if not code:
        return
    for template in code.filter_templates():
        # Handle cases where the template name is followed by a line break
        # Example: {{ejemplo\n
        if  template.name.startswith("adjetivo") or \
            template.name.startswith("desambiguación") or \
            template.name.startswith("ejemplo") or \
            template.name.startswith("glotónimos") or \
            template.name.startswith("inflect") or \
            template.name.startswith("lengua") or \
            template.name.startswith("países") or \
            template.name.startswith("pron-graf") or \
            template.name == "sustantivo": # We don't want to remove templates like {{sustantivo de verbo|...
            safe_remove(code, template)
            continue
        
        if template.name == "plm":
            if template.has(1):
                safe_replace(code, template, template.get(1))
            else:
                safe_remove(code, template)
            continue

        if template.name == "ucf":
            if template.has(1):
                safe_replace(code, template, template.get(1))
            else:
                safe_remove(code, template)
            continue
        
        if template.name == "l" or template.name == "l+":
            safe_replace(code, template, template.get(2))
            continue

        if template.name == "impropia":
            safe_replace(code, template, template.get(1))
            continue

        if template.name == "antropónimo masculino":
            safe_replace(code, template, "Nombre de pila de varón")
            continue

        if template.name == "antropónimo femenino":
            safe_replace(code, template, "Nombre de pila de mujer")
            continue
        
        if template.name == "gentilicio":
            origin = parse_templates(parse(str(template.get(1))))
            meaning = "Originario, relativo a, o propio de {}".format(origin)
            safe_replace(code, template, meaning)
            continue
        
        if template.name == "gentilicio2":
            origin = parse_templates(parse(str(template.get(1))))
            meaning = "Persona originaria de {}".format(origin)
            safe_replace(code, template, meaning)
            continue
        
        if template.name == "sustantivo de verbo":
            if template.has("glosa"):
                verb = template.get("glosa").value
            elif template.has(1):
                verb = template.get(1)
            else:
                safe_remove(code, template)
                continue
            meaning = "Acción o efecto de {}".format(verb)
            safe_replace(code, template, meaning)
            continue

        if template.name == "forma verbo":
            if template.has("p"):
                person = template.get("p").value
            elif template.has(2):
                person = template.get(2)
            else:
                person = ""
            
            if template.has("t"):
                time = template.get("t").value
            elif template.has(3):
                time = template.get(3)
            else:
                time = ""
            
            if template.has("m"):
                mode = template.get("m").value
            elif template.has(4):
                mode = template.get(4)
            else:
                mode = ""
            
            if person.startswith("1s") or person == "yo":
                meaning = "Primera persona del singular"
            elif person.startswith("2s") or person == "vos" or person == "usted":
                meaning = "Segunda persona del singular"
            elif person.startswith("3s"):
                meaning = "Tercera persona del singular"
            elif person.startswith("1p") or person == "nosotros":
                meaning = "Primera persona del plural"
            elif person.startswith("2p") or person == "vosotros" or person == "ustedes":
                meaning = "Segunda persona del plural"
            elif person.startswith("3p"):
                meaning = "Tercera persona del plural"
            else:
                meaning = ""

            if time == "pret imp":
                time = "pretérito imperfecto"
            elif time == "pret ind":
                time = "pretérito perfecto simple"

            if person and mode and time:
                meaning += " del {} de {} de {}".format(
                    time,
                    mode,
                    template.get(1))
            elif person and time:
                meaning += " del {} de {}".format(
                    time,
                    template.get(1))
            elif person:
                meaning += " del {} de {}".format(
                    mode,
                    template.get(1))
            else:
                meaning = "{} de {}".format(
                        mode,
                        template.get(1))
            safe_replace(code, template, meaning)
            continue

    return code

def remove_headings(code: Wikicode) -> Wikicode:
    if not code:
        return
    for template in code.filter_headings():
        safe_remove(code, template)
    return code

def process_links(code: Wikicode) -> Wikicode:
    if not code:
        return
    for wikilink in code.filter_wikilinks():
        if  wikilink.title.startswith('Archivo:') or \
            wikilink.title.startswith('Categoría:') or \
            wikilink.title.startswith('Image:'):
            safe_remove(code, wikilink)
            continue
        if wikilink.title.startswith('Wikipedia:'):
            if wikilink.text:
                safe_replace(code, wikilink, wikilink.text)
    return code

def stringify_and_clean(code: Wikicode) -> str:
    stringified = str(code)
    stringified = remove_leading_numbers(stringified)
    stringified = remove_examples(stringified)
    stringified = remove_references(stringified)
    stringified = parse(stringified).strip_code().strip()
    if stringified:
        stringified = safe_strip_html(stringified)
    return stringified

def extract_definitions(stringified: str) -> list:
    definitions = []
    for definition in stringified.split("\n"):
        if not contains_letters(definition):
            continue
        definition = remove_leading_numbers(definition)
        definitions.append(definition)
    return definitions

def contains_letters(string: str) -> bool:
    return re.search("[a-z]{2,}", str(string)) != None

def remove_leading_numbers(definition: str) -> str:
    return re.sub(r'^\d+\s*', '', definition, flags = re.MULTILINE)

def remove_examples(definition: str) -> str:
    return re.sub(r'^("|:|&quot;|{{uso|{{ejemplo|{{sinónimo|{{relacionado).*\n', '', definition, flags = re.MULTILINE)

def remove_references(definition: str) -> str:
    definition = re.sub(r'(?<=&lt;ref&gt;)(.*?)(?=&lt;\/ref&gt;)', '', definition, flags = re.MULTILINE)
    return re.sub(r'(?<=\<ref)(.*?)(?=\<\/ref\>)', '', definition, flags = re.MULTILINE)

def capitalize_first_letter(definition: str) -> str:
    return definition[0].capitalize() + definition[1:]

if __name__ == "__main__":
    file = open("tests/fixtures/palabra.wiki", "r")
    definitions = parse_and_get_definitions(file.read())
    print(definitions)
