import re

class Definition:
    def __init__(self, definition: str, classification: str):
        self.definition = polish(definition)
        self.classification = classification
    
    def __repr__(self):
        return "[{}] {}".format(self.classification, self.definition)

def polish(definition: str) -> str:
    definition = ensure_finishes_with_dot(definition)
    definition = remove_unwanted_prefixes(definition)
    definition = remove_leading_parenthesis(definition)
    return capitalize_first_letter(definition)

def ensure_finishes_with_dot(definition: str) -> str:
    definition = definition.strip()
    if not len(definition) >= 1:
        return definition
    if definition[-1] == ",":
        definition = definition[:-1] + "."
    if definition[-1] != ".":
        definition += "."
    return definition

def remove_unwanted_prefixes(definition: str) -> str:
    by_extension = "Por extensión, "
    if definition.startswith(by_extension):
        return definition[len(by_extension):]
    figure = "Fig. "
    if definition.startswith(figure):
        return definition[len(figure):]
    return definition

def remove_leading_parenthesis(definition: str) -> str:
    return re.sub(r'^\(.*\)', '', definition).strip()

def capitalize_first_letter(definition: str) -> str:
    if len(definition) < 2:
        return definition
    return definition[0].capitalize() + definition[1:]
